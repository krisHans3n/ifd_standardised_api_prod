import os
import cv2


def add_img_file_to_dir(directory, img, fn=''):
    if fn != '':
        directory = directory + fn
    cv2.imwrite(directory, img)
    cv2.waitKey(0)


def process_directory_and_image(current_dir='', new_dir_sfx='', n_chdirs=None, image=None,):
    tmp_lst = current_dir.split('/')
    if n_chdirs is not None:
        del tmp_lst[-n_chdirs:]
    # new_dir_sfx needs the format -> /directory/directory.../filename
    forge_img_dir = '/'.join(tmp_lst) + new_dir_sfx
    if image is not None:
        add_img_file_to_dir(forge_img_dir, image)
    else:
        return forge_img_dir


class FileHandler(object):
    def __innit__(self, fn, dir):
        self.f_name = fn
        self.dir = dir

    def add_file_to_dir(self):
        pass

    def traverse_directory(self):
        pass
