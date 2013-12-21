Welcome to imfilter
=======================

Image filter implementations written in Python (with `scikit-image <http://scikit-image.org/>`_).

The algorithm of filters are ported from `CamanJS <http://camanjs.com/>`_.

Quick Start
-----------

.. code-block:: python

    from skimage import imread, imshow, show

    import imfilter

    img = imread('lena.png')

    # applies the filter
    f = filter.Lomo()
    f(img)

    # displays the filtered image
    imshow(img)
    show()

.. _demo:

Demonstration
-------------

.. image:: https://raw.github.com/jason2506/imfilter/master/result.png
    :width: 100%
    :alt: demonstration

API Reference
-------------

Filter Base
```````````

.. automodule:: imfilter.base

    .. autoclass:: FilterBase
        :members:
        :undoc-members:

        .. automethod:: __call__(img)

    .. autoclass:: BasicFilter
        :members:
        :undoc-members:

        .. automethod:: _process(img)

    .. autoclass:: LayeredFilter
        :members:
        :undoc-members:

        .. autoattribute:: _LAYERS

Filter Layer
````````````

.. automodule:: imfilter.layer

    .. autofunction:: filter_as_layer

    .. autoclass:: FilterLayer
        :members:
        :undoc-members:

        .. automethod:: __call__(parent, img)

.. _blenders:

Blenders
````````

.. automodule:: imfilter.blender
    :members:
    :undoc-members:

Basic Filters
`````````````

.. automodule:: imfilter.basic
    :members:
    :undoc-members:

Pre-defined Filters
```````````````````

.. automodule:: imfilter.preset
    :members:
    :undoc-members:

.. seealso:: :ref:`Demonstration <demo>`

Filter Pool
```````````

.. autoclass:: imfilter.pool.FilterPool
    :members:
    :undoc-members:
