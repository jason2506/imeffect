# imfilter

Image filter implementations written in Python (with [scikit-image](http://scikit-image.org/)).

The algorithm of filters are ported from [CamanJS](http://camanjs.com/).

## Basic Filters

* `FillColor(rgb)` fills the image with a single RGB color.
  * `rgb` is a (_R_, _G_, _B_) tuple. _R_, _G_, and _B_ are integers range from 0 to 255.
* `Brightness(adjust)` changes the brightness of the image.
  * `adjust` is range from -100 to 100.
* `Saturation(adjust)` adjusts the color saturation of the image.
  * `adjust` is range from -100 to 100.
* `Vibrance(adjust)` increases the intensity of the more muted colors and leaves the already well-saturated colors alone.
  * `adjust` is range from -100 to 100.
* `Greyscale()` computes luminance of an RGB image.
* `Contrast(adjust)` increases or decreases the contrast of the image.
  * `adjust` is range from -100 to 100.
* `Hue(adjust)` adjusts the hue of the image.
  * `adjust` is range from 0 to 100.
* `Colorize(rgb, level)` uniformly shifts the colors in an image towards the given color.
  * `rgb` is a (_R_, _G_, _B_) tuple. _R_, _G_, and _B_ are integers range from 0 to 255.
  * `level` is range from 0 to 100.
* `Invert()` inverts color in the image.
* `Sepia(adjust)` applies sepia effect to the image.
  * `adjust` is range from 0 to 100.
* `Gamma(adjust)` adjusts gamma value of the image.
  * `adjust` is range from 0 to infinity.
* `Noise(adjust)` adds random noise to the image.
  * `adjust` is range from 0 to 100. The bigger the number the stronger the noise.
* `Clip(adjust)` clips color falls outside of the specified range.
  * `adjust` is range from 0 to 100.
* `Channels(red=0, green=0, blue=0)` modifies the intensity of any color channels individually.
  * `red`, `green`, and `blue` are range from 0 to 100.
* `Curves(chans, cps)` maps one color value to another by using the Bezier curve equation.
  * `chans` is a list of indices represents the channels to modify with the filter.
  * `cps` is a list of (_X_, _Y_) tuple represents the point coordinates. _X_ and _Y_ are integers range from 0 to 255.
* `Exposure(adjust)` adjusts the exposure of the image.
  * `adjust` is range from -100 to 100.
* `Posterize(adjust)` converts a continuous gradation of tone to several regions of fewer tones.
  * `adjust` is range from 0 to 100. The smaller the number the fewer the tones.
* `Vignette(scale, strength=60)` applies vignette effect to the image.
  * `scale` is range from 0 to 100.
  * `strength` is range from 0 to 100.
* `Sharpen(adjust)` emphasizes the edges in the image.
  * `adjust` is range from -100 to 100.
* `GaussianBlur(radius)` applies Gaussian blur to the image.
  * `radius` is range from 0 to infinity.

## Demonstration

![Generated Result](https://github.com/jason2506/imfilter/raw/master/result.png)