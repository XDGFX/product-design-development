# Describe different kinds of pseudo colour image processing. [6]

Grey level slicing:
Different grey levels go to different colours

Single grey level to colour transformations:
The grey level goes to three independent transforms (red, green, blue), which then output in colour

Multiple gray level to colour transformations:
Different grey levels transform differently with separate transformations, then combined into three channels with additional processing (e.g. colour balancing)

Frequency filtering approach:
Fourier transform of image
Filter in the frequency domain
Inverse FFT
Additional processing in the spatial domain
Combine to give one colour display
