import cv2
import urllib.request
import numpy as np

def black_white(uri: str):
    """It returs a black and white version of the input image"""

    # decode uri in img
    uri_response = urllib.request.urlopen(uri)
    img_array = np.array(bytearray(uri_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # black-white
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return gray_image