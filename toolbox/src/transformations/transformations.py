import cv2
from PIL import Image
import numpy as np


def erosion(image: Image):
    """It returns an eroded version of the input image"""

    img_array = np.array(image)
    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    # Perform morphological operations (i.e. erosion)
    kernel = np.ones((5, 5), np.uint8)
    eroded_image = cv2.erode(img, kernel, iterations=15)

    return Image.fromarray(cv2.cvtColor(eroded_image, cv2.COLOR_BGR2RGB))


def remove_background(image: Image):
    """It returs the version of the input image without background"""

    img_array = np.array(image)
    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

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
    return Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))


def downsize(image: Image, width: int = 640, height: int = 360):
    """It returs a downsized version of the input image"""

    img_array = np.array(image, dtype=np.uint8)
    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
    size = (width, height)
    downsized_image = cv2.resize(img, size)

    return Image.fromarray(cv2.cvtColor(downsized_image, cv2.COLOR_BGR2RGB))


def blur(image: Image):
    """It returs a blurred version of the input image"""

    # decode uri in img
    img_array = np.array(image)
    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # median blurring
    # k must be an odd number
    k = 45
    blurred_image = cv2.medianBlur(img, k)

    return Image.fromarray(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))


def black_white(image: Image):
    """It returs a black and white version of the input image"""

    # decode uri in img
    img_array = np.array(image)
    img = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    # black_white
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return Image.fromarray(gray_image)
