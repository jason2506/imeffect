# -*- coding: utf-8 -*-

import numpy as np

__all__ = ('filter_as_layer',
           'FilterLayer')


def filter_as_layer(f):
    """Wraps the given filter as a pseudo-layer."""

    def wrapper(img, origin_img):
        return f(img)

    return wrapper


class FilterLayer(object):
    """Filter layer which can apply some filter effects to the given image,
    and then blended back into the parent layer.

    :param opacity: opacity of this layer.
    :param blender: blender function.
    :param filters: a list of filters to be applied to the image.

    .. seealso:: :ref:`blenders`
    """

    def __init__(self, opacity, blender, filters):
        self._opacity = opacity * 0.01
        self._blender = blender
        self._filters = filters

    def __call__(self, parent, img):
        """Applies filter effects to the original image and blends it back to
        the parent layer.

        :param parent: the parent layer.
        :param img: the original image.
        """
        layer = np.copy(img)
        for f in self._filters:
            f(layer, img)

        result = self._blender(parent, layer)
        parent -= (parent - result) * self._opacity
        parent[parent > 1] = 1
        parent[parent < 0] = 0
        return parent
