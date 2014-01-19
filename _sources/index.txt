Welcome to imeffect
=======================

Image filter implementations written in Python (with `scikit-image <http://scikit-image.org/>`_).

The algorithm of filters are ported from `CamanJS <http://camanjs.com/>`_.

Quick Start
-----------

.. code-block:: python

    from skimage.io import imread, imshow, show

    import imeffect

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

.. image:: https://raw.github.com/jason2506/imeffect/master/result.png
    :width: 100%
    :alt: demonstration

API Reference
-------------

Filter Base
```````````

.. automodule:: imeffect.base

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

.. automodule:: imeffect.layer

    .. autofunction:: filter_as_layer

    .. autoclass:: FilterLayer
        :members:
        :undoc-members:

        .. automethod:: __call__(parent, img)

.. _blenders:

Blenders
````````

.. automodule:: imeffect.blender
    :members:
    :undoc-members:

Basic Filters
`````````````

.. automodule:: imeffect.basic
    :members:
    :undoc-members:

Pre-defined Filters
```````````````````

.. automodule:: imeffect.preset
    :members:
    :undoc-members:

.. seealso:: :ref:`Demonstration <demo>`

Filter Pool
```````````

.. autoclass:: imeffect.pool.FilterPool
    :members:
    :undoc-members:
