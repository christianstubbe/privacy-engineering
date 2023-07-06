import cv2
import urllib.request
import numpy as np

def downsize(uri: str, width: int, height:int):
    """It returs a downsized version of the input image"""

    # decode uri in img
    uri_response = urllib.request.urlopen(uri)
    img_array = np.array(bytearray(uri_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # write img (save)
    # cv2.imwrite("path", img)

    # resize
    size = (width, height)
    downsized_image = cv2.resize(img, size)

    return downsized_image