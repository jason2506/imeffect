# -*- coding: utf-8 -*-

__all__ = ('FilterBase',
           'BasicFilter')


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
