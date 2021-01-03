# What are the steps of the Canny edge detector? [4]

1. Convolve gaussian mask with image (gaussian blur)
2. Differenciate using 1st derivative edge detector (sobel)
3. Non maximal suppression (edges give rise to ridges, a thin edge can be produced by setting all pixels not on ridge top to zero)
4. Thresholding with hysteresis (reduces streaking, two thresholds to hold an edge line)