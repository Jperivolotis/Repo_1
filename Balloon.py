#!/usr/bin/env python
# coding: utf-8

# In[75]:


import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.colors import LogNorm 
import pandas as pd 
from matplotlib.cm import ScalarMappable
from PIL import Image

dx = pd.read_csv('/Users/jakobperivolotis/Desktop/NZL.csv')
x = dx.iloc[1:,:1]
#print(x)
t = [0]*200


def convert_strings_to_int(df):
    for index, row in df.iterrows():
        for column in df.columns:
            try:
                value = float(row[column])
                rounded_value = round(value)
                row[column] = int(rounded_value)
            except ValueError:
                row[column] = None
    return df


converted_data = convert_strings_to_int(x)
my_list = x.values.tolist()
data = list(np.concatenate(my_list).flat)
#print(data)

for number in data:
    t[number] +=1
print(t)

