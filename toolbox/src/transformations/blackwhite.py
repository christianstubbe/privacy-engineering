import cv2
import numpy as np
from PIL import Image


def black_white(image: Image):
    """It returs a black and white version of the input image"""

    # decode uri in img
    img_array = np.array(image, dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # black_white
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray_image
