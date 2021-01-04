# What are the features of a snake (active contour model)? [4]

A snake is an energy minimising spline:
- it's energy depends on its shape and position in image
- seeks local energy minima, rather than global
- local minima correspond to desired image properties
- works on paradigm that presence of edge depends not only on gradient at specific point but also the spatial distribution of the gradient