#!/usr/bin/env python
# coding: utf-8

# # ----------------------------------------Portfolio Project 03-------------------------------------------

# # ------------------------------USA Airports Spatial Data Analysis-------------------------------
# 

# # Import Basic Libraries 

# In[68]:


import geopandas as gbd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


from shapely.geometry import Point


# # Load the Data Set 

# In[24]:


airport_data = pd.read_csv('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/us_airports.csv')


# In[6]:


airport_data.head()


# # Data Preprocessing/ Ferturing Engineering 

# In[8]:


airport_data.shape


# In[ ]:


# For Numeric Data 


# In[81]:


airport_data.describe().T


# In[ ]:


# For Non-numeric Data 


# In[82]:


airport_data.describe(include='object').T


# In[9]:


airport_data.columns


# In[21]:


airport_data.isnull().sum()


# In[17]:


type(geometry)


# # Importing the state ESRI ShapeFile of the USA 

# In[28]:


us_states = gbd.read_file('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/us_states.shp')


# # Import 2ns CSV file

# In[29]:


airport_data = pd.read_csv('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/us_airports.csv')


# In[30]:


airport_data.head()


# # Data Preprocessing For Spatial Data Analysis

# In[47]:


geometry = [Point(xy) for  xy in zip(airport_data['LONGITUDE'],airport_data['LATITUDE'])]


# In[49]:


airport_us= gbd.GeoDataFrame(airport_data, geometry = geometry, crs=us_states.crs)


# In[50]:


airport_data.plot()
plt.show()


# In[51]:


airport_data.head()


# # Attribute Joins 

# In[36]:


# Importing the CSV which consists of state names and codes 


# In[52]:


state_names_codes = pd.read_csv('D:/QGIS/QGIS dataset/QGIS 3d/RainFall data set (Interpolation Technique)/Python Spatial DA/state names and codes.csv')


# In[53]:


state_names_codes.head(10)


# In[40]:


# Renaming the column heading


# In[41]:


airport_data.rename(columns={'STATE':'state_code'}, inplace=True)


# In[42]:


airport_data.columns


# In[43]:


# Join attributes 


# In[54]:


airport_us = airport_us.merge(state_names_codes, on= 'state_code')


# In[55]:


airport_us.head()


# # Spatial Joins 

# In[58]:


us_states.plot()
plt.show()


# In[61]:


us_states.head(15)


# In[62]:


airport_us = airport_us[['AIRPORT','geometry']]


# In[65]:


airport_us


# In[70]:


fig, ax = plt.subplots(figsize=(8, 8)) 
us_states.plot(ax=ax, color='gray', edgecolor='black') 
airport_data.plot(ax=ax, markersize=2, color='red')


# In[71]:


# Pefroming Special Join 


# In[74]:


airport_us = gbd.sjoin(airport_us,us_states, how= 'inner', op= 'intersects')


# In[75]:


airport_us


# In[ ]:




