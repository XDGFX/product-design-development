# What different parameters can be used for image energy with snakes? [8]

- Line functional: E_line = +/- f(x, y)
The energy is a function of plus or minus the image value
In other words, the energy is proportional or inversely proportional to the brightness of the image at a particular point

- Edge functional: E_edge = -(delta f(x, y))^2 or
                   E_edge = -|delta f(x, y)|
The energy is a function of the change in intensity; or the edges in the image. First derivative of the gradient approximation.

- Termination functional: E_term is some hectic function I don't want to type out
Used as we often interpret shapes from the ends or corners of lines.
\ | /
-   -  Kind of looks like a square inside?
/ | \

- Other functionals:
Texture

Scale based edge (LoG / Marr Hildreth), where smoothing can be used to turn complex shapes (e.g. cog) into simple shapes (circle), which can be found first

External conditional terms E_conditional
e.g. can have energy of 0 if the snake is inside the image, or 1 if the snake is outside the image (or outside the desired area)