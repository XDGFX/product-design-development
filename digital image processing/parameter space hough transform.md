# What is a potential issue with general Hough transform, when using discreet radii values? How can it be helped? [5]

Assume a circle but this applies to any shape.

If the object radii is in between two test radii, the most votes for the centre point can be a ring around the actual centre point (because that is the best estimate for a slightly too large or slightly too small circle).

Filtering the parameter space (the vote table) may improve the result, for example using the mode (truncated median filter) will find the 'most common value' i.e. the one which has been most voted for, even if the discreet votes are not high enough resolution for this.