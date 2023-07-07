import cv2
import numpy as np
from PIL import Image


def downsize(image: Image, width: int, height: int):
    """It returs a downsized version of the input image"""

    img_array = np.array(image, dtype=np.uint8)
    img = cv2.imdecode(img_array, 1)

    # write img (save)
    # cv2.imwrite("path", img)

    # resize
    size = (width, height)
    downsized_image = cv2.resize(img, size)

    return downsized_image
