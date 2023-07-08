#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import math
import folium

x = pd.read_csv("/Users/jakobperivolotis/Desktop/dataFM/resultsWorld/worldDataCoverage.csv")





def get_cords(latitude, longitude, radius):
    R = 6378 
    
    lat_rads = math.radians(latitude)
    lon_rads = math.radians(longitude)
    
    cent_lat = math.degrees(lat_rads)
    cent_lon = math.degrees(lon_rads)
    
    radius_rads = radius / R
    
    num_points = 400
    circle_points = []
    for i in range(num_points):
        angle = math.radians(float(i) / num_points*360)
        dx = radius_rads * math.cos(angle)
        dy = radius_rads * math.sin(angle)
        
        point_lat = cent_lat + math.degrees(dy)
        point_lon = cent_lon + math.degrees(dx)
        
        circle_points.append((point_lat, point_lon))
        
        
    return circle_points

def visualize_circles(cent_lat, cent_lon, radius):

    map = folium.Map(location = [circles[0][0], circles[0][1]], zoom_start=10)
    
    for circle in circles:
        cent_lat, cent_lon, radius = circle[0], circle[1], circle[2]

    cent_marker = folium.Marker([cent_lat, cent_lon], popup = "Circle Center")
    map.add_child(cent_marker)

    circle_points = get_cords(cent_lat, cent_lon, radius)
    for point in circle_points:
        circle_marker = folium.CircleMarker(point, radius=point_size, color="blue", fill=True, fill_color="blue")
        map.add_child(circle_marker)
    
    file_path = "/Users/jakobperivolotis/desktop/" + "circle_map.html"
    map.save(file_path)
    print("Circle map is saved to:", file_path)
    
    
circles = [(25, -30, 1600), (25, -60, 1600), (25, -90, 1600)]

point_size = 1
output_directory = "/Users/jakobperivolotis/desktop/"

visualize_circles(circles, point_size, output_directory)





# In[ ]:




