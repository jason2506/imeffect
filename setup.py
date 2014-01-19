#!/usr/bin/env python

"""
imeffect
--------

Image filter implementations written in Python (with scikit-image).
"""

from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import numpy

setup(
    name='imeffect',
    version='0.1.0',
    url='http://jason2506.github.io/imeffect/',
    license='The BSD 3-Clause License',
    author='Chi-En Wu',
    author_email='',
    description='Image filter implementations written in Python (with scikit-image).',
    long_description=__doc__,
    packages=['imeffect'],
    zip_safe=False,
    platforms='any',
    install_requires=['scikit-image', 'scipy', 'numpy'],
    cmdclass={'build_ext': build_ext},
    ext_modules=[
        Extension('imeffect._util', ['imeffect/_util.pyx'],
                  include_dirs=[numpy.get_include()])],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
