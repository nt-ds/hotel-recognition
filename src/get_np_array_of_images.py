#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


# In[2]:


def get_np_array_of_images(image_folder_in_int, is_training=True, image_type="unoccluded"):
    
    '''
    Load all .jpg files from a specified folder (inside the main data folder) and append them to a numpy array
    
    Arguments
    ---------
    image_folder_in_int: the image folder's name in integer
    
    Optional Arguments
    ------------------
    is_training:         the dataset to which the images belong
                         True (default) means training set
                         False means test set
    
    image_type:          type of images, only used in test set case
                         "unoccluded" (default) means images are unoccluded
                         "low_occlusions" means images have low occlusions
                         "medium_occlusions" means images have medium occlusions
                         "high_occlusions" means images have high occlusions
                         
    Return
    ------
    A numpy array of image arrays (image dimensions: (128, 128, 3))
    
    '''
    
    
    if is_training:
        path = f"../data/raw/training/{image_folder_in_int}"
    else:
        path = f"../data/raw/test/{image_type}/{image_folder_in_int}"
    
    image_files = []
    
    # r=root, d=directories, f=files
    for r, d, f in os.walk(path):
        for file in f:
            if ".jpg" in file:
                # plt.imread reads an image from a file into an array
                # cv2.resize resizes an image
                # INTER_AREA – resampling using pixel area relation.
                #              It may be a preferred method for image decimation,
                #              as it gives moire’-free results.
                #              But when the image is zoomed,
                #              it is similar to the INTER_NEAREST method (a nearest-neighbor interpolation)
                img = cv2.resize(plt.imread(os.path.join(r, file)),
                                 dsize=(128, 128), # to resize to (128, 128)
                                 interpolation=cv2.INTER_AREA)
                
                # to make sure only RGB images are used
                if img.shape == (128, 128, 3):
                    image_files.append(img)
                
                # to limit to 5,000 images
                if len(image_files) == 5000:
                    return np.array(image_files)
                
    return np.array(image_files)


# Source: [Python – How to list all files in a directory?](https://www.mkyong.com/python/python-how-to-list-all-files-in-a-directory/)
