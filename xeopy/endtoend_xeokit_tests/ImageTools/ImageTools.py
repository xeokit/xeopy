import numpy
import cv2

class ImageTools:
    @staticmethod
    def calculate_mean_squared_error(first_image, second_image):
        height, width, *_ = first_image.shape
        difference = cv2.subtract(first_image, second_image)
        return numpy.sum(difference ** 2) / (float(height * width))
