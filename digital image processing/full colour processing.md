# Describe two different kinds of full colour image processing. [6]

Approach 1:
Convert from RGB to HSL
Process the L component (effectively working in grayscale)
Convert back to RGB

Approach 2:
Process in original colour domain:
    - Process each channel independently and then combine
    - Directly process colour pixels
Depending on the operation, the results of the two options may or may not be identical