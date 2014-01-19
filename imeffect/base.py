# -*- coding: utf-8 -*-

import numpy as np

__all__ = ('FilterBase',
           'BasicFilter',
           'LayeredFilter')


class FilterBase(object):
    """Abstract base class for filters."""

    def __call__(self, img):
        """Applies filter effect to the given image (in place).

        Derived class should override this method to implement the filter
        effect.

        .. warning:: This method will modify the passed image directly.
        """
        return img


class BasicFilter(FilterBase):
    """Abstract base class for basic filters.

    The :meth:`__call__` method will restrict all pixel values between 0 to 1.
    """

    def __call__(self, img):
        img = self._process(img)
        img[img > 1] = 1
        img[img < 0] = 0
        return img

    def _process(self, img):
        """Applies filter effect to the given image.

        Derived class should override this method (instead of :meth:`__call__`) to implement the filter
        effect.
        """
        return img


class LayeredFilter(FilterBase):
    """Abstract base class for layered filters.
    """

    #: A list of filter layers.
    #:
    #: Derived class should override this attribute.
    #:
    #: .. seealso::
    #:    :func:`filter_as_layer <imfilter.layer.filter_as_layer>`,
    #:    :class:`FilterLayer <imfilter.layer.FilterLayer>`
    _LAYERS = ()

    def __init__(self):
        self._layers = self._LAYERS

    def __call__(self, img):
        origin_img = np.copy(img)
        for l in self._layers:
            l(img, origin_img)

        return img
