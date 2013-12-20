# -*- coding: utf-8 -*-

import numpy as np

__all__ = ('filter_as_layer',
           'FilterLayer')


def filter_as_layer(f):
    def wrapper(img, origin_img):
        return f(img)

    return wrapper


class FilterLayer(object):

    def __init__(self, opacity, blender, filters):
        self._opacity = opacity * 0.01
        self._blender = blender
        self._filters = filters

    def __call__(self, parent, img):
        layer = np.copy(img)
        for f in self._filters:
            f(layer, img)

        result = self._blender(parent, layer)
        parent -= (parent - result) * self._opacity
        parent[parent > 1] = 1
        parent[parent < 0] = 0
        return parent
