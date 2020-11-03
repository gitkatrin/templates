# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:57:30 2020
@author: katrin
"""

import glob, os
from PIL import Image
from numpy import asarray


def grayscale():  
    # create new folder
    os.makedirs("./new_foldername_grayscale")
    
    for infile in glob.glob("./filename/*.jpg"):
    
        # grayscale
        img_file = Image.open(infile).convert('L') #grayscale
        
        # convert image to array
        data = asarray(img_file)
            
        print("Datatype: " + str(type(data)))            
        print("Shape: " + str(data.shape)) # Channel
        
        # convert array to image
        image = Image.fromarray(data)
            
        print("Mode: " + str(image.mode))
        print("Size: " + str(image.size)) # Bildgröße
        
        # split the file, to get the name of the image
        file = infile.split('/')[-1]
        name = file.split('.')[-2] # Name des Bildes ohne file und .jpg
        print(str(name))
        
        #safe grayscale image in new folder
        img_file.save("./new_foldername_grayscale/" + str(name) + "_grayscale" + ".jpg" , "JPEG")
        
grayscale()
