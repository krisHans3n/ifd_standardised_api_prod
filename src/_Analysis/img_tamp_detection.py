# import os
# import numpy as np
# # from image_slicer import slice, save_tiles
# import slicer
# from scipy.ndimage import gaussian_filter
# from skimage import io
# from skimage import img_as_float
# from skimage.morphology import reconstruction
# from skimage.io import imread
# from itertools import combinations
#
# """
# module t
# Image manipulation detection module
# """
#
# image_path = "sample-image.png"
# N = 12  # number of slices
# dir = "./data"
#
#
# def read_image(image_path):
#     image = imread(image_path)
#     return image
#
#
# def gaussian_filter1(image):
#     image = img_as_float(image)
#     image = gaussian_filter(image, 1)
#
#     seed = np.copy(image)
#     seed[1:-1, 1:-1] = image.min()
#     mask = image
#
#     dilated = reconstruction(seed, mask, method='dilation')
#     return dilated
#
#
# def filtered_image(image):
#     image1 = image
#     image2 = gaussian_filter1(image)
#     img3 = image1 - image2
#     io.imsave("out.png", img3)
#     return "out.png"
#
#
# # sliced_images = slice(filtered_image(read_image(image_path)),N, save=False)
#
# # save_tiles(sliced_images, directory=dir, prefix='slice')
#
# list_files = []
# for file in os.listdir(dir):
#     list_files.append(file)
# for i in combinations(list_files, 2):
#     img1 = read_image(dir + '/' + i[0])
#     img2 = read_image(dir + '/' + i[1])
#     diff = img1 - img2
#
#     diff_btwn_img_data = np.linalg.norm(diff, axis=1)
#     print("diff between " + str(i) + " two images is " + str(np.mean(diff_btwn_img_data)))
#
# """
# END
# """
