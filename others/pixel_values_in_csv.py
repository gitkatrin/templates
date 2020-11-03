#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:42:23 2020

@author: bhtcsuperuser
"""
import csv
import glob
import os
import numpy as np
from numpy import asarray
from PIL import Image

img_names = []
img_pixels = []
img_data = []

with open("./pixel_values.csv", 'w') as myfile:
    csvwriter = csv.writer(myfile, delimiter=' ', quoting=csv.QUOTE_NONE)
    #csvwriter.writerow(img_arr)
    for infile in glob.glob("./*.jpg"):
        img = Image.open(infile)
        
        # create image name list
       # img_name = infile.split('/')[-1]
        #img_names.append(img_name)
        
        
        # create image pixel list
        img_pixel = asarray(img)
        img_arr = img_pixel.flatten(order="C")
        csvwriter.writerow(img_arr)
      #  img_pixels.append(img_pixel)
        
       # img_data_ = [img_name, img_pixel]
      #  img_data.append(img_data_)

#img_name_array = np.array(img_names)
##print(img_pixel)
#img_pixel_array = np.array(img_pixels)
##print(img_pixel_array)
#img_data_array = np.array(img_data)
#print(img_data_array)