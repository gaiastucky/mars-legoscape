# Mars LEGO Mapping

Tools for creating geological and topographic maps of Mars for LEGO model building.

## Setup

### Install Dependencies

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) if you don't have it already.

2. Create the environment from the provided file:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment:
   ```bash
   conda activate mars-lego-env
   ```

### Running the Scripts

#### Generate Topographic and Geologic Maps

```bash
# Move to the scipts directory where all the action is
cd ./scripts

# Make the generic mapping tools (GMT) scripts executable
chmod u+x plot_topo_map.gmt
chmod u+x plot_geo_map.gmt

# Run the scripts
./plot_topo_map.gmt
./plot_geo_map.gmt
```
These scripts allow us to project the data nicely onto a PNG file, and add on a grid to facilitate the building of the legoscape by using reference lines. *Note that the map is given a new lego-mapping coordinate system (1-96 horizontally, A-Z, a-v vertically).* 

#### Count LEGO Pieces

After generating the maps, count the LEGO plates/bricks needed for each map:

```bash
# Within the script below, make sure you set the topo_or_geo variable (it only does one of the other)
python count_plates.py
```

#### Querying lat/long locations

Note that there is the option (in the ) for querying the location of specific lat/long locations. In the `plot_topo_map.gmt` script mentioned above, you can inpur a coordinate (as the variable coords = 0 0, for example), and it will plot this point on the map, allowing you to find its location in the Lego Coordinate System. 


## File Descriptions
- `scripts/`: Directory for all scripts (bash/gmt for plotting, python for calcualtions)
- `plot_XXX_map.gmt`: GMT script to create topographic or geological map of Mars
- `count_plates.py`: Python script to count LEGO pieces needed
- `mars_XXX.cpt`: Color palette files for selection plot colors (https://docs.generic-mapping-tools.org/6.5/reference/cpts.html)
- `environment.yml`: Conda environment definition
- `input_data/`: Directory with global dataset inputs for making the maps
- `figures/`: Output directory for maps and plots
- `XXX_map_mars.png`: Figures showing geological and topographic data on a grid for Lego building
- `XXX_map_mars_bins.tif`: Additional output tiff file in projected format that allows us to calculate number of pixels for Lego building (required for count_plates.py)

## Data Sources & Processing
### Mars Geological Data:
- Map obtained from Tanaka et al. (2014)
- Simplified manually into 10 major geological units using QGIS Merge tool
- Converted ESRI polygons into tif raster using QGIS Rasterize tool (units 1-10)
- Downsampled (to 96x48 px) and projected (to ESRI:104971) to "Lego Resolution" using gdal "mode" resampling
- Data download source: https://www.arcgis.com/apps/webappviewer/index.html?id=fc004c3d21b64c398ed5458580ab7c58
- Citation: https://pubs.usgs.gov/publication/sim3292

### Mars Topographic Data: 
- Global digital elevation model (DEM) from Mars Orbiter Laser Altimeter (MOLA)
- Downsampled and projected as above (but using "nearest neighbour" resampling)
- Converted to km,
- Data download source: https://astrogeology.usgs.gov/search/map/mars_mgs_mola_dem_463m
- Citation: https://doi.org/10.1029/2000JE001364

