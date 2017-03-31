#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Testing the package pySaliencyMap
#
# Author:      Akisato Kimura <akisato@ieee.org>
#
# Created:     May 4, 2014
# Copyright:   (c) Akisato Kimura 2014-
# Licence:     All rights reserved
#-------------------------------------------------------------------------------
import os

import cv2
import pySaliencyMap
import numpy as np

def HueScale(v):
    """
    v: float (0-1)

    return: (r,g,b) : 0-255, int
    """

    # red
    if(v > 0.67):
        r = 255
    elif(v<0.5):
        r = 0
    elif(0.5<=v<=0.67):
        r = (255/(0.67-0.5))*(v-0.5)
    else:
        raise ValueError("HueScale(v) : v = {} is out of range".format(v))

    # Blue
    if(v < 0.33):
        b = 255
    elif(0.5 < v):
        b = 0
    elif(0.33 <= v <= 0.5):
        b = (-255/(0.5-0.33))*(v - 0.33)
    else:
        raise ValueError("HueScale(v) : v = {} is out of range".format(v))

    # Green
    g = 255. - 1020*(v-0.5)**2

    return (int(r),int(g),int(b))

assert HueScale(0.0) == (0,0,255), HueScale(0.0)

def HueScaleArray(X):
    """
    X: 2Dary (float 0-1)
    """

    w,h = X.shape
    H = np.zeros((w,h,3))

    R = np.array(X)
    G = np.array(X)
    B = np.array(X)
    
    # Green
    G = 255 - 1020 * ((X - 0.5) **2)

    # Red
    R[0.67<R] = 255
    R[R<0.5] = 0
    bin = (0.5<=R) * (R<=0.67)
    if (R[bin].size > 0):
        R = R + (255/(0.67-0.5))*((R*bin)-0.5)

    # Blue    
    B[B<0.33] = 255
    B[0.5<B] = 0
    bin = (0.33<=B) * (B<=0.5)
    if B[bin].size > 0:
        B = B + (-255/(0.5-0.33))*((B*bin)-0.33)

    H[:,:,0]=R[:,:]
    H[:,:,1]=G[:,:]
    H[:,:,2]=B[:,:]

    return H


X = np.zeros((3,2))
H = HueScaleArray(X)





class Saliency:
    def __init__(self, img_path):
        basename = os.path.basename(img_path)
        dirname = os.path.dirname(img_path)
        name, ext = os.path.splitext(basename)

        # ---------------------------------------------
        # read
        # ---------------------------------------------
        img = cv2.imread(img_path)

        # ---------------------------------------------
        # initialize
        # ---------------------------------------------
        imgsize = img.shape
        img_width  = imgsize[1]
        img_height = imgsize[0]
        sm = pySaliencyMap.pySaliencyMap(img_width, img_height)

        # ---------------------------------------------
        # computation
        # ---------------------------------------------
        self.saliency_map = saliency_map = sm.SMGetSM(img) # 顕著度スコア
        self.binarized_map = binarized_map = sm.SMGetBinarizedSM(img) # 01のマスク
        self.salient_region = salient_region = sm.SMGetSalientRegion(img) # 切り抜かれた画像


        # ---------------------------------------------
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.img_sl_map_gray = cv2.cvtColor(saliency_map*255, cv2.COLOR_GRAY2RGB)
        

        # ---------------------------------------------
        # OUTPUT
        # ---------------------------------------------
        # normalize
        saliency_map = (saliency_map/saliency_map.max())
        img[:,:,0]=  (1-saliency_map) * img[:,:,0] # B
        img[:,:,1]=  (1-saliency_map) * img[:,:,1] # G
        # img[:,:,2]=  (saliency_map) * img[:,:,2] # R

        self.output_file=output = os.path.join(dirname, name+"_slmap"+ext)
    
        ret = cv2.imwrite(output, img); #BGR
        if(ret is False):
            raise IOError("cv2.write is Failed {}".format(output))

        self.region_file = region_file = os.path.join(dirname, name+"_reg"+ext)
        ret = cv2.imwrite(region_file, self.salient_region); #BGR

        self.slgray_file = slgray_file = os.path.join(dirname, name+"_slgray"+ext) 
        ret = cv2.imwrite(slgray_file, self.img_sl_map_gray); #BGR
        
        
        # ---------------------------------------------

