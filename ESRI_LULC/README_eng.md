# Downloading Global Landuse Landcover dataset of Your Area of Interest in QGIS

Impact Observatory, Microsoft and ESRI have collaborated to produce Global landcover datasets from Sentinel 2 imagery using machine learning classification model. I saw such dataset as ESRI's living atlas dataset but not much interested as it was an ESRI's imagery layer that QGIS users cannot use much. Later I found that these datasets were available on Amazon cloud service as cloud optimized geotif dataset. These COG dataset were named according to UTM zones and latitude bands။ Generally these are 6 deg x 8 deg size datasets.Being in COG format, they are easy to download via QGIS.

ESRI has published a  ![feature layer](https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/LULC_2020_Download_Scenes/FeatureServer/0) for 2020 Landcover dataset

Abdul Raheem Siddiqui published a ![medium article]( https://ar-siddiqui.medium.com/visualize-download-and-use-esri-10m-global-land-use-dataset-in-qgis-using-qgis-actions-and-cogs-71667c623311) in which  he mentioned how these landcover datasets can be downloaded using QGIS layer action. But it was for just 2020 Landcover only

Later I found some articles about this LU datasets and learned that the datasets since 2017 are available on https://lulctimeseries.blob.core.windows.net (I think it is on amazon cloud). So I modified Siddiqui's script to include following..

 - 1 Layer action script for each year
 - 2 Symbolize the layer same as original style publised by ESRI
 - 3 Add class labels along with class id in the legend
 - 4 Add class label descriptions in the metadata abstract

I created a [Layer definition file (qlr)](https://raw.githubusercontent.com/knwin/qgis/master/ESRI_LULC/ESRI_LULC-downloadable-layers_and_OSM-Basemap.qlr) which includes ESRI LU grid (feature layer) and OSM basemap (for easy reference)![Get it here](ESRI_LULC-downloadable-layers_and_OSM-Basemap.qlr) and open in QGIS. Do following steps

 - 1 Make *ESRI LULC Download Scense (Symbolized)* layer active
 - 2 Select Identify tool
![](images/esri_lu_qlr_opened.png)
 - 3 On the desired grid, right click and popup menu will appear 
![](images/esri_lu_rightclick_menu.png)
 - 4 Select the year of your interest. The COG file will be streamed shortly.
![](images/esri_lu_loaded.png)
![](images/esri_lu_meta.png)
 - 5 You can export the COG layer as GeoTif or Layer Definition File (qlr). Otherwise you can save them in a project file.

----
Kyaw Naing Win

13 Apr 2023
