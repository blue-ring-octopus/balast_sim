# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 16:07:11 2023

@author: hibad
"""

from pupil_apriltags import Detector
import cv2 


at_detector = Detector(
   families="tag36h11",
   nthreads=1,
   quad_decimate=1.0,
   quad_sigma=0.0,
   refine_edges=1,
   decode_sharpening=0.25,
   debug=0
)

img=cv2.load("")
at_detector.detect(img, estimate_tag_pose=True)