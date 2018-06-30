# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 10:53:25 2018

@author: imana
"""

import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   50, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)


while(True):

    ret, frame = cap.read()
    if not ret: continue


    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

    ## do something by using v
    
    
    look_up_table = np.ones((256, 1), dtype = 'uint8' ) * 0
    
    for i in range(256):
        if v==0:
            look_up_table[i][0] = 0
        else:
            look_up_table[i][0] = 255 * pow(float(i) / 255, 1.0 / (v*0.1))
    img_gamma = cv2.LUT(frame, look_up_table)    

    cv2.imshow('title', img_gamma)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()