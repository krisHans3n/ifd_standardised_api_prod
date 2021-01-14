from sklearn.cluster import DBSCAN
import numpy as np
import cv2


class DetectCopyMove(object):
    def __init__(self, image_r):
        self.image = image_r
        self.key_points = None
        self.descriptors = None

    def sift_detector(self):
        sift = cv2.SIFT_create()
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return sift.detectAndCompute(gray, None)

    def show_sift_features(self):
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        sift_image = cv2.drawKeypoints(self.image, self.key_points, self.image.copy())
        return sift_image

    def locate_forgery(self, eps_=40, min_sample=2):
        if self.image is None:
            return None
        else:
            self.key_points, self.descriptors = self.sift_detector()
            print(len(self.key_points))
            clusters = DBSCAN(eps=eps_, min_samples=min_sample).fit(self.descriptors)
            size = np.unique(clusters.labels_).shape[0] - 1
            forge = self.image.copy()
            if (size == 0) and (np.unique(clusters.labels_)[0] == -1):
                print('No Forgery Found!!')
                return None
            if size == 0:
                size = 1
            cluster_list = [[] for i in range(size)]
            for idx in range(len(self.key_points)):
                if clusters.labels_[idx] != -1:
                    cluster_list[clusters.labels_[idx]].append(
                        (int(self.key_points[idx].pt[0]), int(self.key_points[idx].pt[1])))
            for points in cluster_list:
                if len(points) > 1:
                    for idx1 in range(1, len(points)):
                        cv2.line(forge, points[0], points[idx1], (255, 0, 0), 5)
            return forge
