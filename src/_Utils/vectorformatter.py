import os, io, sys
from PIL import Image
import numpy as np
import cv2
import base64

THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = THIS_DIRECTORY.split('/')
del IMG_DIR[-2:]
IMG_DIR = '/'.join(IMG_DIR) + '/image_forgeries/'


class VectorLoader:
    def __init__(self, file_name: str = "", path: str = ""):
        self.file_name = file_name
        self.path = path

    def image_base64(self, file):
        directory = os.listdir(IMG_DIR)
        for fname in directory:
            if file in fname:
                content = open(IMG_DIR+'/'+fname, 'rb')
                return base64.b64encode(content.read()).decode('utf-8')

    def appendB64toJSON(self, dict_):
        for k in list(dict_):
            dict_[k].append(["img_result", self.image_base64(os.path.splitext(k)[0])])
        return dict_





