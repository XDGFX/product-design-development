# What is one of the algorithms for snake feature extraction? [3]

Greedy algorithm (iterative)
Each iteration, enery point on the snake contour will look at neighbouring pixels and calculate if somewhere nearby would minimise it's energy, and move there if so.
Iteration is repeated until all minimum energy