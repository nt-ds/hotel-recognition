#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import os
import matplotlib.pyplot as plt


# In[2]:


def load_images(image_folder_in_int, is_training=True, image_type="unoccluded"):
    '''
    Load all .jpg files from a specified folder (inside the main data folder) and append them to a list
    
    Parameter
        image_folder_in_int: the image folder's name in integer   
    Optional Parameters
        is_training: the dataset to which the images belong
                     True (default) means training set
                     False means test set
        image_type: type of images, only used in test set case
                    unoccluded (default) means images are unoccluded
                    low_occlusions means images have low occlusions
                    medium_occlusions means images have medium occlusions
                    high_occlusions means images have high occlusions
    Return
        a numpy array of image arrays
    '''
    
    if is_training:
        path = f"/content/drive/My Drive/hotel-recognition/data/training/{image_folder_in_int}"
    else:
        path = f"/content/drive/My Drive/hotel-recognition/data/test/{image_type}/{image_folder_in_int}"
    image_files = []
    
    # r=root, d=directories, f=files
    for r, d, f in os.walk(path):
        for file in f:
            if ".jpg" in file:
                # plt.imread reads an image from a file into an array
                image_files.append(plt.imread(os.path.join(r, file)))
                
    return np.array(image_files)


# Source: [Python – How to list all files in a directory?](https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/)
