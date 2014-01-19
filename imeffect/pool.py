# -*- coding: utf-8 -*-

from itertools import chain

__all__ = ('FilterPool',)


def _convert(*args, **kwargs):
    c = chain(args, kwargs.iteritems())
    return frozenset(c)


class FilterPool(object):
    """Filter pool which can hold a collection of filters."""

    def __init__(self):
        self._filters = {}

    def register(self, cls, *args, **kwargs):
        """Registers the filter with class type and its arguments.

        :param cls: the class of registered filter.
        """

        key = _convert(cls, *args, **kwargs)
        if key not in self._filters:
            self._filters[key] = cls(*args, **kwargs)

        return self._filters[key]

    def register_as_layer(self, cls, *args, **kwargs):
        """Registers the filter and returns a pseudo-layer for the filter.

        .. seealso::
            :meth:`FilterPool.register <imfilter.pool.FilterPool.register>`,
            :func:`filter_as_layer <imfilter.layer.filter_as_layer>`
        """

        f = self.register(cls, *args, **kwargs)

        def wrapper(img, origin_img):
            return f(img)

        return wrapper
