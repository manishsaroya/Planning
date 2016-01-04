# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 18:49:49 2015
@author: manish
 email: manishsaroya@gmail.com

@discription: Converts the binary image map to Distance transform image map.
Note: the binary image should be in the same folder as this file.
"""

import Image
import numpy as np
from scipy import ndimage

# open the binary image
img = Image.open('map.png').convert('L')
arr_img = np.asarray(img, np.uint8)
arr_img = np.invert(arr_img) / 255
# taking distance transform of the binary image data
b = ndimage.distance_transform_edt(arr_img)
b = np.uint8(b)
b = np.invert(b)
transformed_img = Image.fromarray(b * 255)
# Saving the image
transformed_img.save('map_distance_tranceform.png')
