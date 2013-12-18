# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = ('FilterBase',
           'BasicFilter')


class FilterBase(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self, img):
        return img


class BasicFilter(FilterBase):

    __metaclass__ = ABCMeta

    def __call__(self, img):
        img = self._process(img)
        img[img > 1] = 1
        img[img < 0] = 0
        return img

    @abstractmethod
    def _process(self, img):
        return img
