# Gallatin County parcel analysis

An analysis of GIS data for Gallatin County, Montana, looking at property ownership and value patterns.

Data sources:
1) GallatinOwnerParcel_shp file downloaded from Montana Cadastral system in June 2015 (includes property values for 2008 assessment cycle; current values as of 2014)
2) GallatinOwnerParcel_shp file downloaded from Montana Cadastral in Sept. 2015 (includes 2014 assessment cycle property values; current values as of 2015)
3) owner-name-corrections-reviewed.txt - json-style text file (intended for import as a dict) of 'name' : 'cleaned name' pairings for cleaning OwnerName column (e.g. 'Forest Service' & 'U.S. Forest Service' --> 'US Forest Service')
4) gc-parcels-inside-bzn.csv - List of geocodes for parcels inside Bozeman city limits, prepared by using QGIS to overlay a 5/1/15 map of city boundaries over GallatinOwnerParcel_shp file current as of Sept. 2015 for select by location function, then cleaning up selection by hand.
5) gc-parcels-inside-ncod.csv - List of geocodes for parcels inside Bozeman's neighborhood conservation overlay district (roughly, the city's historic core). Prepared similarly to (4). 


Questions this is trying to answer:
- How did property values in Gallatin County change between this assessment cycle and last?
- Where is the most valuable property in the county?
- What other interesting trends are there in this data?


Approx Workflow:
1) Datasets (1) and (2) joined in QGIS (redo this to make sure it's clean, limited to parcels that exist as of 2015)
2) Export tabluar data from merged shapefile to csv (gc-parcels-wvalues)
3) Data cleaning/analysis with ipython notebook (gc-parcel-assessment-parser.ipynb), new columns exported to gc-parcels-prop-cat.csv (& .csvt) for merging back into QGIS (see file for inline documentation)
4) Export as shapeful from QGIS, upload to cartodb for presentation


Keywords to signify business ownership as part of business owner names:
LLC, L P, LP, LIMITED PARTNERSHIP, CONDO MASTER, COND MAST, HOA, INC, ASSOCIATION, BANK, CORP, ESTATES

Publishable products:
- Overall trends in property ownership. Commercial versus residential
- How much of Bozeman/Gallatin county is owned by out-of-state landowners? (all property versus residential properties) & How much residential property inside city limits is owned by people who reside at the property address?
- What are the most valuable properties in Gallatin County (overall and per square foot)?
- 