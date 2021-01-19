# process url and take the image object
# -> returns -> image(), metadata()[sent to image], index file of basic image info
### in future the process function will take all images from a webpage DOM when loading

# images are counted and a loop is set to this length

# while true [i.e. no. img = no. threads + extra processes threads]
# -> begin process of image analysis
# -----> this is a series of abstracted classes performing on the same object
# -----> the superclass is imageanalysis()
# -> each image is processed on a separate thread
# -----> at each level when a positive is made it writes to the corresponding image file
# -----> once all levels are complete the image file personal report is complete
# -----> thread stops
####### same process for threaded processes but through different levels

# when all threads are complete the report and text directory should be full of info
# this will be the basis for generating information
# the last stage will be displaying it as a chrome extension and running in the
# background when enabled and a url is freshly visited

'''
Date: 14/12/2020
Author: Kristoffer Hansen
Module -> takes URLs as input produces report in shared access area of program
          threading enabled
          subprocesses to be thrown in
'''
import io
import PIL
from src._Utils.util_dissect_image import *
from src._Analysis.ImageAnalysis import analyse_img_integrity
from PIL import Image
import os
import numpy as np
import sys
import feedparser
import string
import time
import threading
import requests

IMAGE_TYPE_OS_PROGRAM = {
    "png": ["common", "all"],
    "jpeg": ["common", "all"],
    "bitmap": ["common", "microsoft"],
    "psd": ["common", "all", "photoshop"]
}

HTML_ESCAPE_DECODE_TABLE = {"#39": "\'",
                            "quot": "\"",
                            "#34": "\"",
                            "amp": "&",
                            "#38": "&",
                            "lt": "<",
                            "#60": "<",
                            "gt": ">",
                            "#62": ">",
                            "nbsp": " ",
                            "#160": " "}

COLOR_CHANNEL = {
    "RGB": "color 3 channels",
    "L": "grey scale"
}

# IMG_PRC_RES_ALL = {}  # Will contain the results of all analysis

IMG_PATHS = []

TEST_IMG_URLS = []

IMG_OBJS = []

IMAGE_PATHS = []

# Set usable directories
THIS_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
# os.chdir("..")
# os.chdir("test_images_dom_origin")
# IMG_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = THIS_DIRECTORY.split('/')
del IMG_DIR[-1:]
IMG_DIR = '/'.join(IMG_DIR) + '/test_images_dom_origin/'


def clean_directory():
    for file in os.listdir(IMG_DIR):
        print("Removing file: ", file)
        os.remove(IMG_DIR + file)


def process_url(URLs):
    # clean up target directory
    clean_directory()
    IMG_PRC_RES_ALL = {}
    TEST_IMG_URLS = URLs

    # iterate through list of urls
    for url in URLs:
        filename = url.split('/')[-1]
        extension = os.path.splitext(filename)
        r = requests.get(url)

        if r.status_code == 200:
            img_bytes = io.BytesIO(r.content)
            img = PIL.Image.open(img_bytes)
            print(extension[-1])

            if extension[-1] == '' or extension[-1] is None:
                filename = filename + "." + img.format.lower()

            filepath = os.path.join(IMG_DIR, filename)

            img.save(filepath)

            print('Image successfully Downloaded: ', filename)
        else:
            print('Image Could not be retrieved ...')


def build_image_objects(result_dict):
    """
    iterate through images
    strip image and metadata
    construct objects from images data
    :return:
    """

    for file in os.listdir(IMG_DIR):
        print("Current image -> ", file)
        image_obj = construct_image_object(IMG_DIR + file)
        meta_obj = construct_meta_object(IMG_DIR + file)

        image_obj.file_path = IMG_DIR + "/" + file
        image_obj.metadata = meta_obj

        # add image object to the object list for later iteration
        IMG_OBJS.append(image_obj)
        IMG_PATHS.append(image_obj.file_path)
        result_dict[file] = []

    return result_dict
    # show_obj_prop_debug()


def flatten_md_2d(L):
    res = []
    count = 0
    while len(L) > 0:
        count += 1
        ar = L.pop(0)
        if count > 200:
            break
        print(type(ar[0]))
        if type(ar[0]) == list:
            L.append(ar.pop(0))
            if len(ar) >= 1:
                L.append(ar)
        else:
            res.append(ar)
    return res


def compress_common_lst(arr):
    fin = []
    strings_seen = []
    for i in arr:
        if i[0] not in strings_seen:
            fin.append(i)
            strings_seen.append(i[0])
    return fin


def compile_results(dict2):
    for key, value in dict2.items():
        if key in dict2:
            dict2[key] = compress_common_lst(dict2[key])
    return dict2


def coordinate_main(return_d):
    compile_results(analyse_img_integrity(IMG_PATHS, return_d))

    # Note: if faces are detected this flags the GAN generated img det procedure

    # after procs sort multidimensional arrays to 2d
    print("Converting to 2d array")
    print("Current dict -> ", return_d)
    for k, v in return_d.items():
        return_d[k] = flatten_md_2d(v)

    return return_d


def show_obj_prop_debug():
    for each in IMG_OBJS:
        print(each.__dict__)


def find_build_for_category(img_type):
    """
    TODO: needs placed into object as a wrapper
    search image type against list of type index -> class process
    add list of class names in order to execute and add to array
    return array for instantiating classes in list [type list]
    """


class MainInterface:
    def __init__(self):
        pass

    def main_process(self, urls):
        print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        IMG_PRC_RES_ALL = {}
        process_url(urls)
        IMG_PRC_RES_ALL = build_image_objects(IMG_PRC_RES_ALL)
        IMG_PRC_RES_ALL = coordinate_main(IMG_PRC_RES_ALL)

        return IMG_PRC_RES_ALL

# if __name__ == "__main__":
#     print("program execute")
#     TEST_IMG_URLS = [
#         "https://www.w3schools.com/howto/img_mountains.jpg",
#         "https://www.oxforduniversityimages.com/images/rotate/Image_Spring_17_4.gif",
#         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7ZBKhOuWBc_W4--iBAAB3OMPTSVCfci5T9g&usqp=CAU",
#         "https://www.kaggleusercontent.com/kf/36125641/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..EMToG8RKngKqAHeiAM7-1Q.FuFIazG68eOMgtVC8G6gDg2WPAPl3urywbAvB9KNH4_uupRdm5j2jPhilexlCMnHR2YgmfU9S_5GI5PR6U_zjwggdo5fvjXT2r2JEpdMCTZUWj04UV8rdiHdFV7W8SiBAcOIXgWdCXWiCRPM9AxOGaLgsdb58z17r3x3w_yE5MHdureyPCqsv_-eb6uMAHRw4YtYalgAIO7rCjZ1Tp3KFulV2oNol14dM_Pq6S33Cg8BU6obZa-wMZpQFSx5EdPzR4RScSn44YXZF0oN_Qvrv0zejhmpzlaevAFwpIzbvieHPHv5rkNRK21lCnhy0XrHzcOHLi8VN7PbsMdRRiYcnf8mZOywMU1z3dLusaENqjbQlCydvRnZn5-z5LTavjot-J87OEyTbV10uSrsHUUuTNjD0veNPb1umBAdIDiictN6PE5EIV1ZIR41qb5j0Omk7aTAUsGwsFVUwCf9qsuu0MChHOHnRGKrnFUZywirkaocDw-jLdKJJ-F5kP99VZw_fLr251W3wcZcTvV04vv9mwJGjDOYtiA9DpRCx_lJFSbl4t7VrJxP_6Vf9ymJ8d08eB6lRz5h9scb8zjMP_UZVwwLnopHQ12GXfIuyWkM6vNBMuwPp_EmKwfDVpdHQozhI_ezRFUZLIDRrwr90ostYlfXuOd0suMbPsGizYIMA34.YzVvjpIvCDAhma1wDx23nQ/__results___files/__results___9_0.png"
#
#     ]
#     main_process(TEST_IMG_URLS)
# else:
#     print("program failed")
