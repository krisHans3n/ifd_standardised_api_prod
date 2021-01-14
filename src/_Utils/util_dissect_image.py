from src._Image_Env.Image import ImageSolid
from src._Image_Env.MetaData import MetaData
from src._Image_Env.EXIFTypeMeta import *
#import exiftool
import PIL
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS, GPSTAGS
import numpy as np

'''
processes a digital image format to separate into categories
called in main program [initialise_image_process.py]
returns Image() and MetaData() objects
'''




def construct_meta_object(img):
    pil_img = Image.open(img)

    meta_return = MetaData()

    # pull out the necessary metadata
    # perhaps use exifread to avoid obstacle of protected members
    #meta_return.data_raw = pil_img._getEXIF()

    return meta_return


def construct_image_object(img):
    image_return = ImageSolid()
    pil_img = Image.open(img)

    image_return.filetype = pil_img.format
    image_return.width, image_return.height = pil_img.size
    image_return.size = image_return.width * image_return.height
    return_pixel_ratio()
    image_return.pixel_vector = return_pixel_vector(pil_img)
    image_return.pixel_format = return_pixel_format(pil_img)
    return_color_type()

    return image_return


def return_filetype(pil_img):
    return pil_img.format()


def return_filetype_info():  # string of info about the file medium
    return None


def return_pixel_count(pil_img):
    return pil_img.size()


def return_pixel_format(pil_img):
    return pil_img.mode


def return_pixel_ratio():  # dictionary of string and int
    return True


def return_pixel_vector(pil_img):
    return np.array(pil_img)


def return_color_type():
    return True


def brightness_vector_scale():
    return True


def return_hashed_image(hash_alg):
    # takes alg name as string
    # switch case
    # return varchar string
    return True

"""
=
=
=
=
=
=
=
=
"""
