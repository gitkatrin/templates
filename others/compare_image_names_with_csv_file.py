#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:39:52 2020

@author: bhtcsuperuser
"""


import csv
import glob
import os
import numpy as np
from numpy import asarray
from PIL import Image
#import cv2

#------------------------------------------------------------------------------
# read data from .csv file (Imagename and Framekey Pixel)

with open("./name_of_csv_file.csv") as csvdatei:
    csv_reader_object = csv.reader(csvdatei)
    zeilennummer = 1
    image_names = []
    data = []
    csv_data = []
    for row in csv_reader_object:
        
        # create name list
        image_name = row[0] 
        image_names.append(image_name)
        
        # create data list
        xmin = row[4]
        ymin = row[5]
        xmax = row[6]
        ymax = row[7]
        data_ = [xmin, ymin, xmax, ymax]
        data.append(data_)

        csv_data_ = [image_name, xmin, ymin, xmax, ymax]
        csv_data.append(csv_data_)
        
        zeilennummer += 1
        
    print(f'Anzahl Datensätze: {zeilennummer-1}')


#------------------------------------------------------------------------------
# read images names from folder and as arrays

img_names = []
img_pixels = []
img_data = []
for infile in glob.glob("./*.jpg"):
    img = Image.open(infile)
    
    # create image name list
    img_name = infile.split('/')[-1]
    img_names.append(img_name)
    
    
    # create image pixel list
    img_pixel = asarray(img)
    img_pixels.append(img_pixel)
    
    img_data_ = [img_name, img_pixel]
    img_data.append(img_data_)

#img_name_array = np.array(img_names)
##print(img_pixel)
#img_pixel_array = np.array(img_pixels)
##print(img_pixel_array)
img_data_array = np.array(img_data)
#print(img_data_array)

#------------------------------------------------------------------------------
# compare image names in image folder and image names in csv file

del image_names[0]
x=0
pixel_label = []
while x < len(image_names): # length = 13397
    
    for i in range(len(img_names)):   # lenght = 4320
        if image_names[x] in img_names[i]:
            print(image_names[x], x, "gefunden in item", img_names[i], i) # Bildname aus .csv gefunden in Ordner  
    x += 1
        
            
            
            
            
            
            
            
            
            
            
            
            