# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 23:27:31 2020

@author: samet.arslanturk
"""

import numpy as np
import cv2 
 
foto = cv2.imread('kenar.jpg')  #lena resmini okuduk. RGB uint8 
griFoto = cv2.cvtColor(foto,cv2.COLOR_BGR2GRAY) #foto grey yapıldı. Grey
griTon = np.float32(griFoto) #foto 32 bite donusturuldu float32
koseler1 = cv2.goodFeaturesToTrack(griTon, 100, 0.06, 10)

koseler = np.int0(koseler1) #int64 e donusturuldu 


for kose in koseler:
    x,y = kose.ravel()
    cv2.circle(foto, (x,y), 5,255, -1) #r=3

cv2.imshow('koseler',foto)
cv2.waitKey(0)

