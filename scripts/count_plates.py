import rasterio
import numpy as np
from collections import Counter

# Calculate plates needed for the map depending on the type of map
####################
geo_or_topo = "geo" #change this to "geo" or "topo"
####################

if geo_or_topo == "geo":
    file = "../figures/geo_map_mars_bins.tif"
else:   
    file = "../figures/topo_map_mars_bins.tif"

# Open the GeoTIFF file and remove NaNs
with rasterio.open(file) as src:
    data = src.read(1)
valid_data = ~np.isnan(data)
filtered_data = data[valid_data]

# Count occurrences of each value
bins = Counter(filtered_data.flatten())

# Sort the bins by key for ordered output
total_plates = 0
for b in sorted(bins.keys()):
    count = bins[b]
    if geo_or_topo == "topo":
        total_plates += b * count #want to accumulate height in plates if it's the topography
        print(f"{int(b)}-Plate Height: {count} pixels")

    elif geo_or_topo == "geo":
        total_plates += count
        print(f"Unit {int(b)}: {count} pixels")

print(f"\nTotal plates needed: {total_plates}")
print("\nFor geologic bins/plates: individual bins matter more since each unit is a different color)")
print("Topographic bins/plates: total amount matters more since they are all the same color(?))")