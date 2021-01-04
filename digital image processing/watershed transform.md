# Describe the watershed transform for image segmentation. [3]

Morphological approach to segmentation; a combination of edge and region based.

You have the surface, drill holes at the minima (bottom of catchment basins), then lower the surface into water

Keep lowering, and you get to a point where to catchment basins merge, this is the edge of two regions. Build a wall at this point to prevent merging, and keep going until the entire model is sunk.

The walls then represent boundaries between two different regions.