# Describe how you can determine the zero crossings of a second derivative output? [4]

Binary edge map

For a 3x3 window, you add up all four quadrants

[
    1   2   3
    4   5   6
    7   8   9
]

to get

A = [
    1   2
    4   5
]

B = [
    2   3
    5   6
]

etc...

This will give
[
    A   B
    C   D
]

If any of these values have a different sign, then the centre pixel is an edge point. Note: after the LoG function, the values in the image will not be 0-255, they can be negative and this is why this works.