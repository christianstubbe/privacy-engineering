import cv2
from PIL import Image
import numpy as np


def erosion(image: Image):
    """It returns an eroded version of the input image"""

    img_array = np.array(image, dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)
    # Perform morphological operations (i.e. erosion)
    kernel = np.ones((5, 5), np.uint8)
    eroded_image = cv2.erode(img, kernel, iterations=15)

    return eroded_image
