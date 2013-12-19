# -*- coding: utf-8 -*-

import numpy as np
from numpy.linalg import norm
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d
from skimage.color import rgb2hsv, hsv2rgb

from .base import BasicFilter

__all__ = ('FillColor',
           'Brightness',
           'Saturation',
           'Vibrance',
           'Greyscale',
           'Contrast',
           'Hue',
           'Colorize',
           'Invert',
           'Sepia',
           'Gamma',
           'Noise',
           'Clip',
           'Channels',
           'Curves',
           'Exposure',
           'Posterize',
           'Vignette',
           'Sharpen',
           'GaussianBlur')


def _lerp(a, b, t):
    return a * (1 - t) + b * t


def _fill_missing_values(values, end):
    result = np.zeros(end + 1)
    for i in xrange(end + 1):
        if i in values:
            result[i] = values[i]
        else:
            left = (i - 1, result[i - 1])
            right = None
            for j in xrange(i, end + 1):
                if j in values:
                    right = (j, values[j])
                    break

            if right is None:
                result[i:end + 1] = result[i - 1]
                break

            offset = (right[1] - left[1]) / (right[0] - left[0]) * (i - left[0])
            result[i] = left[1] + offset

    return result.astype(np.int32)


def _bezier(cps, lower=0, upper=255):
    bezier = {}
    for i in xrange(1000):
        t = i * 0.001
        p = np.copy(cps)
        for j in xrange(p.shape[0] - 1, 0, -1):
            for k in xrange(j):
                p[k, 0] = _lerp(p[k, 0], p[k + 1, 0], t)
                p[k, 1] = _lerp(p[k, 1], p[k + 1, 1], t)

        idx = int(round(p[0, 0]))
        val = min(max(p[0, 1], lower), upper)
        bezier[idx] = round(val)

    end = cps[-1][0]
    return _fill_missing_values(bezier, end)


class FillColor(BasicFilter):

    def __init__(self, rgb):
        self._rgb = np.array(rgb).reshape((1, 1, 3)) / 255.0

    def _process(self, img):
        img[:, :, :] = self._rgb
        return img


class Brightness(BasicFilter):

    def __init__(self, adjust):
        self._adjust = adjust * 0.01

    def _process(self, img):
        img += self._adjust
        return img


class Saturation(BasicFilter):

    def __init__(self, adjust):
        self._adjust = adjust * -0.01

    def _process(self, img):
        max = np.amax(img, axis=2)
        img += (np.atleast_3d(max) - img) * self._adjust
        return img


class Vibrance(BasicFilter):

    def __init__(self, adjust):
        self._adjust = adjust * -0.01

    def _process(self, img):
        max = np.amax(img, axis=2)
        avg = np.mean(img, axis=2)
        amt = 2 * abs(max - avg) * self._adjust
        img += (np.atleast_3d(max) - img) * np.atleast_3d(amt)
        return img


class Greyscale(BasicFilter):

    def _process(self, img):
        r = img[:, :, 0]
        g = img[:, :, 1]
        b = img[:, :, 2]
        grey = 0.299 * r + 0.587 * g + 0.114 * b
        img[:, :, 0] = grey
        img[:, :, 1] = grey
        img[:, :, 2] = grey
        return img


class Contrast(BasicFilter):

    def __init__(self, adjust):
        self._adjust = ((adjust + 100) * 0.01) ** 2

    def _process(self, img):
        img *= self._adjust
        img += 0.5 * (1 - self._adjust)
        return img


class Hue(BasicFilter):

    def __init__(self, adjust):
        self._adjust = adjust * 0.01

    def _process(self, img):
        hsv = rgb2hsv(img)
        h = hsv[:, :, 0] + self._adjust
        h[h > 1] -= 1
        hsv[:, :, 0] = h
        img[:, :, :] = hsv2rgb(hsv)
        return img


class Colorize(BasicFilter):

    def __init__(self, rgb, level):
        self._offset = np.array(rgb).reshape((1, 1, 3)) / 255.0
        self._level = level * 0.01

    def _process(self, img):
        img -= (img - self._offset) * self._level
        return img


class Invert(BasicFilter):

    def _process(self, img):
        img -= 1
        img *= -1
        return img


class Sepia(BasicFilter):

    def __init__(self, adjust):
        adjust = adjust * 0.01
        self._sr = np.array([[[1 - 0.607 * adjust,
                               0.769 * adjust,
                               0.189 * adjust]]])
        self._sg = np.array([[[0.349 * adjust,
                               1 - 0.314 * adjust,
                               0.168 * adjust]]])
        self._sb = np.array([[[0.272 * adjust,
                               0.534 * adjust,
                               1 - 0.869 * adjust]]])

    def _process(self, img):
        img[:, :, 0] = np.sum(img * self._sr, axis=2)
        img[:, :, 1] = np.sum(img * self._sg, axis=2)
        img[:, :, 2] = np.sum(img * self._sb, axis=2)
        return img


class Gamma(BasicFilter):

    def __init__(self, adjust):
        self._adjust = adjust

    def _process(self, img):
        img **= self._adjust
        return img


class Noise(BasicFilter):

    def __init__(self, adjust):
        self._adjust = abs(adjust) * 0.01

    def _process(self, img):
        noisy = np.random.rand(*img.shape) * 2 * self._adjust - self._adjust
        img += noisy
        return img


class Clip(BasicFilter):

    def __init__(self, adjust):
        self._adjust = abs(adjust) * 0.01

    def _process(self, img):
        img[img > 1 - self._adjust] = 1
        img[img < self._adjust] = 0
        return img


class Channels(BasicFilter):

    def __init__(self, red=0, green=0, blue=0):
        self._adjust = np.array([red, green, blue]) * 0.01

    def _process(self, img):
        for dim in xrange(3):
            adjust = self._adjust[dim]
            if adjust > 0:
                img[:, :, dim] += (1 - img[:, :, dim]) * adjust
            elif adjust < 0:
                img[:, :, dim] -= img[:, :, dim] * abs(adjust)

        return img


class Curves(BasicFilter):

    def __init__(self, chans, cps):
        self._chans = chans
        self._cps = np.array(cps, dtype=np.int32)
        self._curve = None

    def _get_bezier(self):
        if self._curve is None:
            bezier = _bezier(self._cps, 0, 255)

            start = self._cps[0]
            bezier[:start[0]] = start[1]

            end = self._cps[-1]
            self._curve = np.concatenate((bezier, [end[1]] * (255 - end[0])))

        return self._curve

    def _process(self, img):
        bezier = self._get_bezier()
        idx = np.around(img * 255)
        for c in self._chans:
            channel = img[:, :, c]
            channel_idx = idx[:, :, c]
            for v in xrange(256):
                channel[channel_idx == v] = bezier[v] / 255.0

            img[:, :, c] = channel

        return img


class Exposure(Curves):

    def __init__(self, adjust):
        p = abs(adjust) * 0.01
        if adjust > 0:
            ctrl1 = (0, p * 255)
            ctrl2 = ((1 - p) * 255, 255)
        else:
            ctrl1 = (p * 255, 0)
            ctrl2 = (255, (1 - p) * 255)

        chans = (0, 1, 2)
        cps = ((0, 0), ctrl1, ctrl2, (255, 255))
        super(Exposure, self).__init__(chans, cps)


class Posterize(BasicFilter):

    def __init__(self, adjust):
        self._adjust = float(adjust)

    def _process(self, img):
        img[:, :, :] = np.round(img * self._adjust) / self._adjust
        return img


class Vignette(BasicFilter):

    _curve = None

    def __init__(self, scale, strength=60):
        self._scale = scale * 0.01
        self._strength = strength * 0.01
        if Vignette._curve is None:
            cps = np.array(((0, 1), (30, 30), (70, 60), (100, 80)))
            Vignette._curve = _bezier(cps)

    def _process(self, img):
        h, w, d = img.shape
        size = min(h, w) * self._scale
        center = (h * 0.5, w * 0.5)
        start = norm(center)
        end = start - size

        dx = np.array(range(h)).reshape((h, 1)) - center[0]
        dy = np.array(range(w)).reshape((1, w)) - center[1]
        dx = np.tile(dx, (1, w))
        dy = np.tile(dy, (h, 1))
        d = np.sqrt(dx ** 2 + dy ** 2)

        b = d > end
        idx = np.round((d[b] - end) / size * 100).astype(np.int32)

        p = np.zeros(idx.shape, dtype=np.float)
        for i in xrange(101):
            p[idx == i] = Vignette._curve[i]

        p *= 0.1 * self._strength
        p[p < 1] = 1.0
        for i in xrange(3):
            channel = img[:, :, i]
            channel[b] **= p
            img[:, :, i] = channel

        return img


class Sharpen(BasicFilter):

    def __init__(self, adjust):
        adjust = adjust * 0.01
        self._kernel = np.array([[0, -adjust, 0],
                                 [-adjust, 4 * adjust + 1, -adjust],
                                 [0, -adjust, 0]])

    def _process(self, img):
        img[:, :, 0] = convolve2d(img[:, :, 0], self._kernel, mode='same')
        img[:, :, 1] = convolve2d(img[:, :, 1], self._kernel, mode='same')
        img[:, :, 2] = convolve2d(img[:, :, 2], self._kernel, mode='same')
        return img


class GaussianBlur(BasicFilter):

    def __init__(self, radius):
        self._sigma = radius / 3.0

    def _process(self, img):
        for c in xrange(3):
            channel = img[:, :, c]
            gaussian_filter(channel, output=channel, sigma=self._sigma)
            img[:, :, c] = channel

        return img
