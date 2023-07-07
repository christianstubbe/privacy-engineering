import cv2
import numpy as np
from PIL import Image


def blur(image: Image):
    """It returs a blurred version of the input image"""

    # decode uri in img
    img_array = np.array(image, dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # median blurring
    # k must be an odd number
    k = 45
    blurred_image = cv2.medianBlur(img, k)

    return blurred_image
