# -*- coding: utf-8 -*-

import numpy as np

__all__ = ('FilterBase',
           'BasicFilter',
           'LayeredFilter')


class FilterBase(object):

    def __call__(self, img):
        return img


class BasicFilter(FilterBase):

    def __call__(self, img):
        img = self._process(img)
        img[img > 1] = 1
        img[img < 0] = 0
        return img

    def _process(self, img):
        return img


class LayeredFilter(FilterBase):

    _LAYERS = ()

    def __init__(self):
        self._layers = self._LAYERS

    def __call__(self, img):
        origin_img = np.copy(img)
        for l in self._layers:
            l(img, origin_img)

        return img
