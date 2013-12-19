# -*- coding: utf-8 -*-

from itertools import chain

__all__ = ('FilterPool')


def _convert(*args, **kwargs):
    c = chain(args, kwargs.iteritems())
    return frozenset(c)


class FilterPool(object):

    def __init__(self):
        self._filters = {}

    def register(self, cls, *args, **kwargs):
        key = _convert(cls, *args, **kwargs)
        if key not in self._filters:
            self._filters[key] = cls(*args, **kwargs)

        return self._filters[key]

    def register_as_layer(self, cls, *args, **kwargs):
        f = self.register(cls, *args, **kwargs)

        def wrapper(img, origin_img):
            return f(img)

        return wrapper
