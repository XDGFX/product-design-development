# When calculating the magnitude for a colour edge detector using vector order statistics, what are two possible alternative features to find to minimise noise influence? [4]

1. For each value in the window, calculate the sum of distances to all other values (same as vector median)

2. To calculate the vector range, subtract the original value with the highest distance with the original value with the lowest distance (which is also the vector median)

However, to provide a more robust solution to impulsive (long tailed) noise:
Don't use the value with the highest distance, instead use a predefined lower value (e.g. for a 5x5 mask, instead of using the 25th value, use the 19th value [k=6])

To provide a more robust solution to gaussian (short tailed) noise:
Don't use the value with the lowest distance, instead use the mean of the l lowest values (e.g. for a 5x5 mask, use the 10 lowest values and average them)