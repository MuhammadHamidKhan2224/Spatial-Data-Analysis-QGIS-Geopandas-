#!/usr/bin/env python
# coding: utf-8

# # ----------------------------------------Portfolio Project 02-------------------------------------------

# # -------------------------------Vector Geoprocessing Tools---------------------------------------

# # Import Basic Libraries 

# In[3]:


import geopandas as gbd 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# # Load Shape Files (shp)

# In[21]:


sa1 = gbd.read_file('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/Study_Area_1.shp')


# In[20]:


sa1.plot()
plt.show()


# In[9]:


sa2= gbd.read_file('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/Study_Area_2.shp')


# In[10]:


sa2.plot()
plt.show()


# In[11]:


river = gbd.read_file('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/river.shp')


# In[12]:


river.plot()
plt.show()


# In[25]:


fig, ax = plt.subplots()
sa1.plot(ax = ax, color = 'blue', edgecolor = 'black')
sa2.plot(ax = ax, color = 'none', edgecolor = 'black')
river.plot(ax = ax)


# # Intersection of Polygons

# In[27]:


intersection = gbd.overlay(sa1, sa2, how='intersection')
intersection.plot()


# In[32]:


intersection.head()


# # Union of Polygons

# In[30]:


union = gbd.overlay(sa1, sa2, how='union')
union.plot()
plt.show()


# In[31]:


union.head()mm


# # Symmetric Difference of Polygons 

# In[33]:


sy_diff = gbd.overlay(sa1, sa2, how='symmetric_difference')
sy_diff.plot()
plt.show()


# In[34]:


sy_diff.head()


# # Difference of Polygons

# In[35]:


difference = gbd.overlay(sa1,sa2,how='difference')
difference.plot()
plt.show()


# In[36]:


difference.head()


# # Dissolveing a polygon

# In[38]:


union = gbd.overlay(sa1, sa2, how='union')
union.plot()


# In[39]:


union['common_column'] = 1


# In[40]:


union.head()


# In[42]:


dissolved_sa = union.dissolve(by = 'common_column')
dissolved_sa.plot()
plt.show()

dissolved_sa.head()
# # Buffer in Polygons

# In[45]:


river.crs


# # Reprojecting the river GeoPandas GeoDataFrame into a projected CRS 

# In[47]:


river_pro = river.to_crs(epsg=24547)


# In[48]:


river.plot()


# In[49]:


river_pro.plot()


# In[50]:


river_pro.head()


# In[51]:


type(river_pro)


# In[53]:


type(river_pro['geometry'])


# In[55]:


buffer_500m = (river_pro['geometry']).buffer(distance = 500)


# In[57]:


buffer_500m.plot(figsize = (7,7))


# # Obtained the centroid 

# In[62]:


union = gbd.overlay(sa1,sa2,how='union')
union.plot(edgecolor = 'black')
plt.show()


# In[64]:


centroid = union['geometry'].centroid
centroid.plot(figsize = (7,7))


# In[66]:


fig1, ax1 = plt.subplots()
union.plot(ax = ax1, color = 'gray', edgecolor = 'black')
centroid.plot(ax = ax1, color = 'black')


# In[ ]:




