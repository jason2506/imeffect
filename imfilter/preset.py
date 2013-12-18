# -*- coding: utf-8 -*-

from . import basic, blender
from .layer import FilterLayer, LayeredFilter
from .pool import FilterPool

__all__ = ('Vintage',
           'Lomo',
           'Clarity',
           'SinCity',
           'Sunrise',
           'CrossProcess',
           'OrangePeel',
           'Love',
           'Grungy',
           'Jarques',
           'Pinhole',
           'OldBoot',
           'GlowingSun',
           'HazyDays',
           'HerMajesty',
           'Nostalgia',
           'Hemingway',
           'Concentrate')

_register = FilterPool().register
_L = FilterLayer


def _P(*args, **kwargs):
    proxy = _register(*args, **kwargs)

    def wrapper(img, origin_img):
        return proxy(img)

    return wrapper


class Vintage(LayeredFilter):

    _LAYERS = (_P(basic.Greyscale),
               _P(basic.Contrast, 5),
               _P(basic.Noise, 3),
               _P(basic.Sepia, 100),
               _P(basic.Channels, 8, 2, 4),
               _P(basic.Gamma, 0.87),
               _P(basic.Vignette, 40, 30))

    def __init__(self, vignette=True):
        self._layers = self._LAYERS if vignette else self._LAYERS[:-1]


class Lomo(LayeredFilter):

    _LAYERS = (_P(basic.Brightness, 15),
               _P(basic.Exposure, 15),
               _P(basic.Curves, (0, 1, 2),
                   ((0, 0), (200, 0), (155, 255), (255, 255))),
               _P(basic.Saturation, -20),
               _P(basic.Gamma, 1.8),
               _P(basic.Vignette, 50, 60),
               _P(basic.Brightness, 5))

    def __init__(self, vignette=True):
        if vignette:
            self._layers = self._LAYERS
        else:
            self._layers = self._LAYERS[:5] + self._LAYERS[6:]


class Clarity(LayeredFilter):

    _LAYERS = (_P(basic.Vibrance, 20),
               _P(basic.Curves, (0, 1, 2),
                  ((5, 0), (130, 150), (190, 220), (250, 255))),
               _P(basic.Sharpen, 15),
               _P(basic.Vignette, 45, 20),
               _P(basic.Greyscale),
               _P(basic.Contrast, 4))

    def __init__(self, grey=False):
        if grey:
            self._layers = self._LAYERS
        else:
            self._layers = self._LAYERS[:-2]


class SinCity(LayeredFilter):

    _LAYERS = (_P(basic.Contrast, 100),
               _P(basic.Brightness, 15),
               _P(basic.Exposure, 10),
               _P(basic.Posterize, 80),
               _P(basic.Clip, 30),
               _P(basic.Greyscale))


class Sunrise(LayeredFilter):
    _LAYERS = (_P(basic.Exposure, 3.5),
               _P(basic.Saturation, -5),
               _P(basic.Vibrance, 50),
               _P(basic.Sepia, 60),
               _P(basic.Colorize, (0xe8, 0x7b, 0x22), 10),
               _P(basic.Channels, red=8, blue=8),
               _P(basic.Contrast, 5),
               _P(basic.Gamma, 1.2),
               _P(basic.Vignette, 55, 25))


class CrossProcess(LayeredFilter):

    _LAYERS = (_P(basic.Exposure, 5),
               _P(basic.Colorize, (0xe8, 0x7b, 0x22), 4),
               _P(basic.Sepia, 20),
               _P(basic.Channels, blue=8, red=3),
               _P(basic.Curves, (2,),
                   ((0, 0), (100, 150), (180, 180), (255, 255))),
               _P(basic.Contrast, 15),
               _P(basic.Vibrance, 75),
               _P(basic.Gamma, 1.6))


class OrangePeel(LayeredFilter):

    _LAYERS = (_P(basic.Curves, (0, 1, 2),
                  ((0, 0), (100, 50), (140, 200), (255, 255))),
               _P(basic.Vibrance, -30),
               _P(basic.Saturation, -30),
               _P(basic.Colorize, (0xff, 0x90, 0x00), 30),
               _P(basic.Contrast, -5),
               _P(basic.Gamma, 1.4))


class Love(LayeredFilter):

    _LAYERS = (_P(basic.Brightness, 5),
               _P(basic.Exposure, 8),
               _P(basic.Contrast, 4),
               _P(basic.Colorize, (0xc4, 0x20, 0x07), 30),
               _P(basic.Vibrance, 50),
               _P(basic.Gamma, 1.3))


class Grungy(LayeredFilter):

    _LAYERS = (_P(basic.Gamma, 1.5),
               _P(basic.Clip, 25),
               _P(basic.Saturation, -60),
               _P(basic.Contrast, 5),
               _P(basic.Noise, 5),
               _P(basic.Vignette, 50, 30))


class Jarques(LayeredFilter):

    _LAYERS = (_P(basic.Saturation, -35),
               _P(basic.Curves, (2,),
                  ((20, 0), (90, 120), (186, 144), (255, 230))),
               _P(basic.Curves, (0,),
                  ((0, 0), (144, 90), (138, 120), (255, 255))),
               _P(basic.Curves, (1,),
                  ((10, 0), (115, 105), (148, 100), (255, 248))),
               _P(basic.Curves, (0, 1, 2),
                  ((0, 0), (120, 100), (128, 140), (255, 255))),
               _P(basic.Sharpen, 20))


class Pinhole(LayeredFilter):

    _LAYERS = (_P(basic.Greyscale),
               _P(basic.Sepia, 10),
               _P(basic.Exposure, 10),
               _P(basic.Contrast, 15),
               _P(basic.Vignette, 60, 35))


class OldBoot(LayeredFilter):

    _LAYERS = (_P(basic.Saturation, -20),
               _P(basic.Vibrance, -50),
               _P(basic.Gamma, 1.1),
               _P(basic.Sepia, 30),
               _P(basic.Channels, red=-10, blue=5),
               _P(basic.Curves, (0, 1, 2),
                  ((0, 0), (80, 50), (128, 230), (255, 255))),
               _P(basic.Vignette, 60, 30))


class GlowingSun(LayeredFilter):

    _LAYERS = (_P(basic.Brightness, 10),
               _L(80, blender.multiply,
                  (_P(basic.Gamma, 0.8),
                   _P(basic.Contrast, 50),
                   _P(basic.Exposure, 10))),
               _L(80, blender.softlight,
                  (_P(basic.FillColor, (0xf4, 0x96, 0x00)),)),
               _P(basic.Exposure, 20),
               _P(basic.Gamma, 0.8),
               _P(basic.Vignette, 45, 20))

    def __init__(self, vignette=True):
        self._layers = self._LAYERS if vignette else self._LAYERS[:-1]


class HazyDays(LayeredFilter):

    _LAYERS = (_P(basic.Gamma, 1.2),
               _L(60, blender.overlay,
                  (_P(basic.Channels, red=5),
                   _P(basic.GaussianBlur, 15))),
               _L(40, blender.addition,
                  (_P(basic.FillColor, (0x68, 0x99, 0xba)),)),
               _L(35, blender.multiply,
                  (_P(basic.Brightness, 40),
                   _P(basic.Vibrance, 40),
                   _P(basic.Exposure, 30),
                   _P(basic.Contrast, 15),
                   _P(basic.Curves, (0,),
                      ((0, 40), (128, 128), (128, 128), (255, 215))),
                   _P(basic.Curves, (1,),
                      ((0, 40), (128, 128), (128, 128), (255, 215))),
                   _P(basic.Curves, (2,),
                      ((0, 40), (128, 128), (128, 128), (255, 215))),
                   _P(basic.GaussianBlur, 5))),
               _P(basic.Curves, (0,),
                  ((20, 0), (128, 158), (128, 128), (235, 255))),
               _P(basic.Curves, (1,),
                  ((20, 0), (128, 128), (128, 128), (235, 255))),
               _P(basic.Curves, (2,),
                  ((20, 0), (128, 108), (128, 128), (235, 255))),
               _P(basic.Vignette, 45, 20))


class HerMajesty(LayeredFilter):

    _LAYERS = (_P(basic.Brightness, 40),
               _P(basic.Colorize, (0xea, 0x1c, 0x5d), 10),
               _P(basic.Curves, (2,),
                  ((0, 10), (128, 180), (190, 190), (255, 255))),
               _L(50, blender.overlay,
                  (_P(basic.Gamma, 0.7),
                   _L(60, blender.normal,
                      (_P(basic.FillColor, (0xea, 0x1c, 0x5d)),)))),
               _L(60, blender.multiply,
                  (_P(basic.Saturation, 50),
                   _P(basic.Hue, 90),
                   _P(basic.Contrast, 10))),
               _P(basic.Gamma, 1.4),
               _P(basic.Vibrance, -30),
               _L(10, blender.normal,
                  (_P(basic.FillColor, (0xe5, 0xf0, 0xff)),)))


class Nostalgia(LayeredFilter):

    _LAYERS = (_P(basic.Saturation, 20),
               _P(basic.Gamma, 1.4),
               _P(basic.Greyscale),
               _P(basic.Contrast, 5),
               _P(basic.Sepia, 100),
               _P(basic.Channels, red=8, blue=2, green=4),
               _P(basic.Gamma, 0.8),
               _P(basic.Contrast, 5),
               _P(basic.Exposure, 10),
               _L(55, blender.overlay,
                  (_P(basic.GaussianBlur, 10),)),
               _P(basic.Vignette, 50, 30))


class Hemingway(LayeredFilter):

    _LAYERS = (_P(basic.Greyscale),
               _P(basic.Contrast, 10),
               _P(basic.Gamma, 0.9),
               _L(40, blender.multiply,
                  (_P(basic.Exposure, 15),
                   _P(basic.Contrast, 15),
                   _P(basic.Channels, green=10, red=5))),
               _P(basic.Sepia, 30),
               _P(basic.Curves, (0, 1, 2),
                  ((0, 10), (120, 90), (180, 200), (235, 255))),
               _P(basic.Channels, red=5, green=-2),
               _P(basic.Exposure, 15))


class Concentrate(LayeredFilter):

    _LAYERS = (_P(basic.Sharpen, 40),
               _P(basic.Saturation, -50),
               _P(basic.Channels, red=3),
               _L(80, blender.multiply,
                  (_P(basic.Sharpen, 5),
                   _P(basic.Contrast, 50),
                   _P(basic.Exposure, 10),
                   _P(basic.Channels, blue=5))),
               _P(basic.Brightness, 10))
