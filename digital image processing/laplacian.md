# What are the two mask shapes for the second derivative laplacian edge detector? What is a major issue with this? What is a better alternative function? [4]

4 nearest neighbour
[
        -1   
    -1   4  -1
        -1  
]

8 nearest neighbour
[
    -1  -1  -1
    -1   8  -1
    -1  -1  -1
]

No smoothing; noise will create lots of edges. Can use Laplacian of a Gaussian (LoG) which has built in smoothing.