# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 17:11:58 2018

@author: imana
"""

import numpy as np
import cv2
from skimage import io
from skimage.color import*

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   1, # max
                   myfunc) # callback func


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):

    ret, frame = cap.read()
    if not ret: continue


    v = cv2.getTrackbarPos('value',  # get the value
                           'title')  # of the win

    ## do something by using v
    if v!=0:
        frame=rgb2hsv(frame)

    cv2.imshow('title', frame)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()