# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:30:40 2024

@author: Geoffrey Chemwa
"""

import cv2

#cv2.imread('cat.jfif',0)
img = cv2.imread('cat.jfif',0) #rad image file and store image in img variable; 0-grayscale; 1-color RGB; -1-image as is from file.
print(img)

cv2.imshow('image',img)   #show thw image in a window whose title is window 
cv2.waitKey(5000)         #show the window for 5 seconds on the screen
cv2.destroyAllWindows()   #destroy the created window
