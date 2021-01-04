# How can you speed up template matching for feature recognition? [4]

Multi resolutional search: start at low res and only focus in on the most feasible areas with more resolution

Frequency domain: As convolutions in the spatial domain are multiplications in the frequency domain, it may be less computationally intensive to FFT of image and template, multiply the two, and then inverse FFT.