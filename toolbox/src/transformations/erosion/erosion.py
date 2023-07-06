import cv2
import urllib.request
import numpy as np

def erosion(uri: str):
    """It returs an eroded version of the input image"""

    # decode uri in img
    uri_response = urllib.request.urlopen(uri)
    img_array = np.array(bytearray(uri_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # write img (save)
    # cv2.imwrite("path", img)

   # Perform morphological operations (i.e. erosion)
    kernel = np.ones((5, 5), np.uint8)
    eroded_image = cv2.erode(img, kernel, iterations=15)

    return eroded_image