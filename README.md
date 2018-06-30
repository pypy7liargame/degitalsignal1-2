# degitalsignal1-2
トーンカーブ,カラー色調,フィルタリング

- gamma.py
```python
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
    
    
    look_up_table = np.ones((256, 1), dtype = 'uint8' ) * 0   #lookuptableの定義
    
    for i in range(256):
        if v==0:  #vで割るのでvが0のときの例外処理
            look_up_table[i][0] = 0
        else:
            look_up_table[i][0] = 255 * pow(float(i) / 255, 1.0 / (v*0.1))  #ガンマ関数の計算
    img_gamma = cv2.LUT(frame, look_up_table)    

    cv2.imshow('title', img_gamma)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
```

- hue.py
```python

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
        frame=rgb2hsv(frame)  #rgb画像をhsv画像に変換

    cv2.imshow('title', frame)  # vが0のときはrgb画像が表示されvを1にするとhsv画像が表示される

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
```

- filtering.py
```python
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 21:14:06 2018

@author: imana
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt


def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('value', # name of value
                   'title', # win name
                   0, # min
                   100, # max
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
    if v!=0:  # vが0意外の時は普通に適応
        kernel = np.ones((v,v),np.float32)/(v**2)
        frame2 = cv2.filter2D(frame,-1,kernel)  #kernelフィルタを使ってカラー画像をフィルタリングする関数
    else:     # vが0のときは1と同じ処理を適応
        kernel = np.ones((1,1),np.float32)
        frame2 = cv2.filter2D(frame,-1,kernel)

    cv2.imshow('title', frame2)  # show in the win

    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break



cap.release()
cv2.destroyAllWindows()
```

- 参考にしたサイト

[Python OpenCV3でガンマ変換 (輝度、色彩の調整)](https://www.blog.umentu.work/python-opencv3%E3%81%A7%E3%82%AC%E3%83%B3%E3%83%9E%E5%A4%89%E6%8F%9Bgamma-conversion-2/)

[Pythonの学習の過程とか](http://peaceandhilightandpython.hatenablog.com/entry/2016/02/05/004445)

[OpenCV 画像の平滑化](http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_filtering/py_filtering.html)
