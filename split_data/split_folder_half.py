#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 16:03:56 2021

@author: bhtcsuperuser
"""


import os
import shutil

source = r'./brightness'
destination = r'./brightness2'
files = os.listdir(source)

i=0
while i < len(files):
    new_path = shutil.move(f"{source}/{files[i]}", destination)
    print(files[i])
    i+=2