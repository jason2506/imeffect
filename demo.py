# -*- coding: utf-8 -*-

import pyximport

import numpy as np
import matplotlib.pyplot as plt

pyximport.install(setup_args={'include_dirs': np.get_include()})

import imeffect.preset as ime


def main():
    img = plt.imread('lena.png')

    plt.figure(figsize=(7.5, 4.6))
    plt.subplots_adjust(left=0.02, right=0.98, bottom=0.02, top=0.94,
                        wspace=0.1, hspace=0.2)

    for idx, name in enumerate(ime.__all__):
        print 'Rendering filter: {}....'.format(name)

        Filter = ime.__dict__.get(name)
        f = Filter()
        fimg = f(np.copy(img))

        plt.subplot(3, 6, idx + 1)
        plt.title(name, fontsize=10)
        plt.axis('off')
        plt.imshow(fimg)

    plt.savefig('result.png')


if __name__ == '__main__':
    main()
