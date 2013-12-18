# -*- coding: utf-8 -*-

import numpy as np

__all__ = ('normal',
           'multiply',
           'screen',
           'overlay',
           'difference',
           'addition',
           'exclusion',
           'softlight',
           'lighten',
           'darken')


def normal(parent, layer):
    return layer


def multiply(parent, layer):
    return layer * parent


def screen(parent, layer):
    return 1 - (1 - layer) * (1 - parent)


def overlay(parent, layer):
    gt_idx = parent > 0.5
    lt_idx = ~gt_idx

    result = np.zeros(parent.shape)
    result[gt_idx] = 1 - 2 * (1 - layer[gt_idx]) * (1 - parent[gt_idx])
    result[lt_idx] = layer[lt_idx] * parent[lt_idx] * 2
    return result


def difference(parent, layer):
    return layer - parent


def addition(parent, layer):
    return layer + parent


def exclusion(parent, layer):
    return 0.5 - 2 * (layer - 0.5) * (parent - 0.5)


def softlight(parent, layer):
    gt_idx = parent > 0.5
    lt_idx = ~gt_idx

    result = np.zeros(parent.shape)
    result[gt_idx] = 1 - ((1 - (layer[gt_idx] - 0.5)) * (1 - parent[gt_idx]))
    result[lt_idx] = (layer[lt_idx] + 0.5) * parent[lt_idx]
    return result


def lighten(parent, layer):
    return np.maximum(parent, layer)


def darken(parent, layer):
    return np.minimum(parent, layer)
