"""

The functions of this program range from basic image manipulaiton detection to more refined techniques
This program is by no means an exhaustive list of techniques but provide a reasonable tool kit

Please note:
When expanding and refining this module keep in mind that this program may need to be
translated into a more resource efficient language
"""

import os
import sys
import cv2
from src._Utils.util_file_handler import *
from src._Analysis.copy_move_det import DetectCopyMove
import numpy as np
import slicer
from scipy.ndimage import gaussian_filter
from skimage import io
from skimage import img_as_float
from skimage.morphology import reconstruction
from skimage.io import imread
from itertools import combinations

# file_name = "/home/kris/Dev/softw_const/img_det_phase2/img_det_ext/test_images_dom_origin/tstimg-vinyl.png"

eps = 60
min_samples = 2


def analyse_img_integrity(file_paths, IMG_Results):
    # Main loop for all stored image paths in question
    for fp in file_paths:
        print(">>>>>>>>>>>> Analysing images from URL list")
        image = cv2.imread(fp)
        f_name = os.path.basename(fp)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        tmp_lst = current_dir.split('/')
        del tmp_lst[-2:]
        forge_img_dir = '/'.join(tmp_lst) + '/image_forgeries/' + f_name

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        Copy-move forgery detection 
        """
        print(">>>>>>>>>>>>>>> Copy move forgery detection started")
        detect = DetectCopyMove(image)
        forgery = detect.locate_forgery(eps, min_samples)

        if forgery is not None:
            IMG_Results[f_name].append(["DBSCAN_CPY_MOVE", 1])
            # store forgery for use in client for image overlay
            cv2.imwrite(forge_img_dir, forgery)
            cv2.waitKey(0)
        else:
            IMG_Results[f_name].append(["DBSCAN_CPY_MOVE", 0])

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                Image splicing detection
                IMG_Results[f_name].append(["IMG_SPLICING", 0])
        """
        
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                Image Location  [default value ""]
                IMG_Results[f_name].append(["IMG_Location", "Location Info"])
        """
        
        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                Image retouching detection
                IMG_Results[f_name].append(["RETOUCHING", 0])
        """

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                Image lighting reconditioning detection
                IMG_Results[f_name].append(["LIGHT_RECONDITION", 0])
        """

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                Detect faces in Image
                IMG_Results[f_name].append(["FACE_DETECTION", 0])
        """

        """
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                Detect faces in Image
                if FACE_DETECTION = 1 ->IMG_Results[f_name].append(["GAN_MANIPULATED_IMAGE", 0])
        """

    return IMG_Results
