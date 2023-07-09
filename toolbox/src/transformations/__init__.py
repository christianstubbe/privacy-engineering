from transformations.blurring import *
from transformations.erosion import *
from transformations.blackwhite import *
from transformations.remove_background import *
from transformations.downsize import *
from enum import Enum
from PIL import Image


class Transformations(Enum):
    NONE = 0,
    EROSING = 1,
    BLACKWHITE = 2,
    RM_BACKGROUND = 3,
    DOWNSIZE = 4,
    BLURRING = 5


def transform(img: Image, transformation=Transformations.NONE) -> Image:
    if not isinstance(img, Image.Image):
        raise ValueError
    if transformation == Transformations.BLURRING:
        return blur(img)
    elif transformation == Transformations.EROSING:
        return erosion(img)
    elif transformation == Transformations.BLACKWHITE:
        return black_white(img)
    elif transformation == Transformations.RM_BACKGROUND:
        return remove_background(img)
    elif transformation == Transformations.DOWNSIZE:
        return downsize(img)
    else:
        return img
