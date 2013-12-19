# -*- coding: utf-8 -*-

import pyximport

import numpy as np
import matplotlib.pyplot as plt

pyximport.install(setup_args={'include_dirs': np.get_include()})

import imfilter.preset as imf


def main():
    plt.figure()
    img = plt.imread('lena.png')
    for idx, name in enumerate(imf.__all__):
        print 'Rendering filter: {}....'.format(name)

        Filter = imf.__dict__.get(name)
        f = Filter()
        fimg = f(np.copy(img))

        plt.subplot(3, 6, idx)
        plt.title(name)
        plt.axis('off')
        plt.imshow(fimg)

    plt.show()


if __name__ == '__main__':
    main()
