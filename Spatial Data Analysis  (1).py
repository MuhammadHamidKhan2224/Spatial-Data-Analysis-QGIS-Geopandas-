#!/usr/bin/env python
# coding: utf-8

# # ----------------------------------------Portfolio Project 01-------------------------------------------

# # ------------------------------Geopandas: Spatial Data Analysis--------------------------------

# In[31]:


import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


pak.head()


# In[33]:


pak = gpd.read_file(r"D:\QGIS\QGIS dataset\Google Earth\pak_admbnda_adm0_ocha_pco_gaul_20181218.shp")


# In[34]:


pak.plot()
plt.title('Map of Pakistan')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()  
plt.show()  


# In[35]:


prov = gpd.read_file(r"D:\QGIS\QGIS dataset\Google Earth\pak_admbnda_adm1_ocha_pco_gaul_20181218.shp")


# In[6]:


prov.head()


# In[7]:


fig, ax = plt.subplots(figsize=(12, 6))  
prov.plot(ax=ax, cmap='twilight_shifted', column='ADM1_EN', legend=True, 
          legend_kwds={'title': "Provinces", 'loc': 'upper left', 'bbox_to_anchor': (1, 1)}) 
plt.title('Provinces of Pakistan')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()  
plt.show()  


# In[8]:


district = gpd.read_file(r"D:\QGIS\QGIS dataset\Google Earth\pak_admbnda_adm2_ocha_pco_gaul_20181218.shp")


# In[9]:


district.head()


# In[10]:


district.plot()
plt.title('Districts of Pakistan')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()  
plt.show()  


# In[11]:


tehsil = gpd.read_file(r"D:\QGIS\QGIS dataset\Google Earth\pak_admbnda_adm3_ocha_pco_gaul_20181218.shp")


# In[12]:


tehsil.plot()
plt.title('Tehsils of Pakistan')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()  
plt.show()  


# In[13]:


roads = gpd.read_file(r"D:\QGIS\QGIS dataset\QGIS 3d\MajorRoads.shp")


# In[14]:


roads.plot()
plt.title('Roads structure of Pakistan')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.tight_layout()  
plt.show()  


# In[15]:


railway = gpd.read_file(r"D:\QGIS\QGIS dataset\QGIS 3d\PAK_rails.shp")


# In[16]:


railway.plot()
plt.title('Railway Stations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()



# In[17]:


fig, ax = plt.subplots(figsize=(10, 10))
district.plot(ax=ax, color='lightblue', edgecolor='black', alpha=0.5)
roads.plot(ax=ax, color='red', linewidth=1, label='Roads')
railway.plot(ax=ax, color='black', linewidth=1, label='Railways')
plt.legend()
plt.title('Spatial Analysis of Districts, Roads, and Railways')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# In[18]:


intersections = gpd.overlay(district, roads, how='intersection', keep_geom_type=False)


# In[19]:


import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10))
district.plot(ax=plt.gca(), color='none', edgecolor='blue', linewidth=0.5)
intersections.plot(ax=plt.gca(), color='red', markersize=5)
plt.title('Districts and Road Intersections')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()



# In[36]:





# In[ ]:




