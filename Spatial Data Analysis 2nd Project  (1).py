#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = gpd.read_file(r"D:\QGIS\QGIS dataset\QGIS 3d\SDA shapefile\places.shp")


# In[3]:


df.head()


# In[50]:


df['population'].unique()


# In[69]:


df['type'].unique()


# In[51]:


df['name'].unique()


# In[11]:


df.describe().T


# # Ploting the Shape File

# In[93]:


fig, ax = plt.subplots(figsize=(4, 4))
df.plot(ax=ax, color='blue', edgecolor='black') 
ax.set_title('Spatial Data Visualization', fontsize=15)
ax.set_xlabel('Longitude', fontsize=12)
ax.set_ylabel('Latitude', fontsize=12)


# # Basic Exploration

# In[57]:


print(df.head())
print(['type'].value_counts())


# In[ ]:





# # Create a Choropleth Map for Population

# In[92]:


df.plot(column='population', scheme="quantiles", figsize=(4, 4), legend=True)


# # Visualize Place Types

# In[89]:


fig, ax = plt.subplots(1, 1, figsize=(6, 8))
for place_type in df['type'].unique():
    sub_df = df[df['type'] == place_type]
    sub_df.plot(ax=ax, label=place_type)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))  
plt.tight_layout()  
plt.show()



# # Count the Occurrence of Each Type

# In[65]:


type_counts = df['type'].value_counts()
type_counts


# # Plot the Counts

# In[87]:


type_counts.plot(kind='bar', figsize=(8, 6))
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Count of Each Type')
plt.show()


# In[84]:


df['population'] = pd.to_numeric(df['population'], errors='coerce')
fig, ax = plt.subplots(1, 1, figsize=(4, 8))
df.plot(column='population', ax=ax, legend=True,
         legend_kwds={'label': "Population by Area",
                      'orientation': "horizontal"},
         cmap='viridis') 
plt.show()


#  # Population Size vs. Place Type

# In[83]:


df['population'] = pd.to_numeric(df['population'], errors='coerce')
df['x'] = df.geometry.centroid.x
df['y'] = df.geometry.centroid.y
fig, ax = plt.subplots(figsize=(5, 7))

for place_type in df['type'].unique():
    subset = df[df['type'] == place_type]
    ax.scatter(subset['x'], subset['y'], s=subset['population']/1000, label=place_type, alpha=0.2, edgecolors='w')

ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Population Size vs. Place Type')
plt.show()


# # Hotspot Analysis

# In[81]:


import folium
from folium.plugins import HeatMap
base_location = [df['y'].mean(), df['x'].mean()]
m = folium.Map(location=base_location, zoom_start=5)
heat_data = [[row['y'], row['x'], row['population']] for index, row in df.iterrows() if row['population'] > 0]
HeatMap(heat_data).add_to(m)
m


# In[23]:


print(df.crs)


# # Reproject to UTM zone 42N for western Pakistan (EPSG:32642). If your area of interest is more towards the east, consider using EPSG:32643 instead.

# In[32]:


df_projected = df.to_crs(epsg=32642, inplace=True)


# In[27]:


print(df.crs)


# In[ ]:




