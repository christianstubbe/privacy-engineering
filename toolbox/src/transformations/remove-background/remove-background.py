import cv2
import urllib.request
import numpy as np

def remove_background(uri: str):
    """It returs the version of the input image without background"""

    # decode uri in img
    uri_response = urllib.request.urlopen(uri)
    img_array = np.array(bytearray(uri_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # calculates the h and w of the img
    hh, ww = img.shape[:2]

    # Create a mask to mark the areas of the image
    mask = np.zeros(img.shape[:2], np.uint8)

    # Create background and foreground models
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Define the bounding box of the object (foreground)
    rect = (10, 10, ww, hh)

    # Apply GrabCut algorithm to segment foreground and background
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Create a mask with the probable foreground regions
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # Apply the mask to the image to remove the background
    result = img * mask2[:, :, np.newaxis]

    # shows img to screen with label "Image"
    # scv2.imshow("Result Image", result)

    return result

