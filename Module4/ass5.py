#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 19:01:56 2017

@author: dipanjan
"""
import pandas as pd

from scipy import misc
#from mpl_toolkits.mplot3d import Axes3D
import matplotlib
#import matplotlib.pyplot as plt

# Look pretty...
matplotlib.style.use('ggplot')
import os

samples = []

for file in os.listdir('Datasets/ALOI/32'):
        a = os.path.join('Datasets/ALOI/32', file)
        img = misc.imread(a)
        #samples.append((img[::2,::2]/255.0).reshape(-1))
        samples.append(img.reshape(-1))
#print len(samples) # 72, as expected since there 72 files in the folder

df = pd.DataFrame(samples)

print(df)