# Describe the vector median filter. [4]

A median filter but for multi-channel images (e.g. colour images). Median cannot be found for separate channels, because the result may be different values for each channel.

The vector median puts each value into space (e.g. a 2D plot for two channels, 3D plot for three channels), and finds the point which is the lowest total distance from all other points (in the filter window).

For example, for each point, the distances to all other points are summed, and the point with the lowest value is the vector median.