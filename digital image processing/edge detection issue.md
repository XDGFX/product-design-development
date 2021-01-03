# What is a major issue with all edge detection algorithms? How can it be overcome? [4]

Scale
Many processing techniques work on an individual pixel level, but then what counts as an edge?

Is a white stripe a single ridge edge or two step edges?
What is the direction of a jagged line which mostly goes in one direction?

By blurring the image first it can help merge noisy or small edges and only focus on the larger edges. Addressed in Canny; larger gaussian radius (sigma) the larger the scale of the edge detection.