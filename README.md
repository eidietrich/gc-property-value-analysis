# Gallatin County parcel analysis

Analysis of GIS data for Gallatin County, Montana available through the state cadastral system, looking at property ownership and value patterns. Portions of this analysis formed the basis of a major feature package published by the Bozeman Daily Chronicle on Nov. 8, 2015.

## Tools used
1. [Montana Cadastral parcel database](svc.mt.gov/msl/mtcadastral/) - State-maintained system that allows for both interactive exploration of property at the parcel level and downloading data on a county-by-county basis.
2. iPython notebooks/pandas - Respectively a web-based computational platform and Python data analysis library. Available through the [Anacaonda Python distribution](https://www.continuum.io/downloads). Used for the for bulk of project data cleaning and analysis.
3. [QGIS](http://qgis.org/en/site/) - Open-source GIS system (comparative to ArcGIS, except free). Used for translating GIS shapefiles to/from pandas-compatible .csv formats, as well as visual data exploration and production of mapping products for print package. 
4. [CartoDB](https://cartodb.com/) - Web mapping service used for the creation of an interactive graphic displaying data.

## Data source files:
1. gc-parcels-current-2015 (folder w/ .shp and .csv) - File downloaded from Montana Cadastral in Sept. 2015 (includes 2014 assessment cycle property values; current values as of 2015). Base data for most of analysis.
2. gc-parcels-june-2015 (folder w/ .shp and .csv) - File downloaded from Montana Cadastral system in June 2015 (includes property values for 2008 assessment cycle; current values as of 2014), trimmed to relevant data only.
3. gc-parcels-current-geocode-only (folder w/ .shp) - Shapefile data for current Gallatin County parcels stripped of all attribute data except geocodes. Merged with parsed/analyzed parcel data.
4. owner-name-corrections-reviewed.txt - json-style text file of {'name' : 'cleaned name'} pairings for cleaning ownername column in (e.g. 'Forest Service' & 'U.S. Forest Service' --> 'UNITED STATES OF AMERICA').
5. gc-parcels-inside-bzn.csv - List of geocodes for parcels inside Bozeman city limits, prepared by using QGIS to overlay a 5/1/15 map of city boundaries over GallatinOwnerParcel_shp file current as of Sept. 2015 for select by location function, then cleaning up selection by hand.
6. gc-parcels-inside-ncod.csv - List of geocodes for parcels inside Bozeman's neighborhood conservation overlay district (roughly, the city's historic core). Prepared similarly to (4). 

## Data analysis scripts
1. gc-parcel-asessment-parser.ipynb - iPython notbook that cleans and processes raw data downloaded from Montana Cadastral system to prepare data for further analysis. Adds in property value for a previous assessment cycle, standardizes property owner names, sorts properties into major land use type categories, adds flags for properties inside Bozeman and the city's historic preservation district, calculates property-by-property value change stats and adds columns designating the total ownership extent for each property owner. See file for inline documentation. Produces the following files:
    - gc-parcels-for-gis.csv/.csvt - Outputs geocodes and select data columns to a file for import into QGIS. This data was merged with shapefile data for each parcel to allow mapping presentations through QGIS and CartoDB.
    - gc-parcels-complete.csv - Complete cleaned/processed dataset for further non-spatial analysis.
    - gc-owner-list.csv - A simple list of the distinct owner names recorded (post-standardization) in the property dataset. Used primarily to iteratively fine-tune the owner name corrections file.
2. gc-parcel-assessment-analyzer.ipynb - iPython notebook used to explore cleaned data, outputting ranking lists and distribution figures based on gc-parcels-complete.csv file. Also exports top-30 lists for land owner rankings by total size and value (gc-parcels-30-by-value.csv and gc-parcels-30-by-size.csv).
3. gc-parcel-rank-display-output.py - Quick and dirty script to convert .csv-formatted ranking information into HTML for easier import of rankings into content management system (piping ranking data into print and web publication workflows). Used with tabluated data that had been hand-refined in Google Sheets from the gc-parcels-30 .csvs.

## Outputs
1. gc-parcel-w-analysis - folder/shapefile with output from gc-parcel-asessment-parser.ipynb, recombined with parcel shape data in QGIS. Zipped version uploaded to CartoDB for online interactive.
2. gc-parcels-30-by-value.csv - ranking of top 30 Gallatin County propery owners by total value of owned land.
3. gc-parcels-30-by-size.csv - ranking of top 30 Gallatin County property owners by total acreage owned.
4. gc-county-major-owners.pdf - QGIS-generated map of major county land owners, developed for use in Nov. 2015 print package.