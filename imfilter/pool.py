# -*- coding: utf-8 -*-

from itertools import chain

__all__ = ('FilterProxy',
           'FilterPool')


def _convert(*args, **kwargs):
    c = chain(args, kwargs.iteritems())
    return frozenset(c)


class FilterProxy(object):

    def __init__(self, cls, args, kwargs):
        self._cls = cls
        self._args = args
        self._kwargs = kwargs
        self._instance = None

    def __call__(self, img):
        if self._instance is None:
            self._instance = self._cls(*self._args, **self._kwargs)

        return self._instance(img)


class FilterPool(object):

    def __init__(self):
        self._proxies = {}

    def register(self, cls, *args, **kwargs):
        key = _convert(cls, *args, **kwargs)
        if key not in self._proxies:
            self._proxies[key] = FilterProxy(cls, args, kwargs)

        return self._proxies[key]
