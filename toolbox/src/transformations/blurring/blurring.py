import cv2
import urllib.request
import numpy as np

def blur(uri: str):
    """It returs a blurred version of the input image"""

    # decode uri in img
    uri_response = urllib.request.urlopen(uri)
    img_array = np.array(bytearray(uri_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # median blurring
    # k must be an odd number
    k = 45
    blurred_image = cv2.medianBlur(img, k)

    return blurred_image