import hashlib
from io import BytesIO
from PIL import Image


def calculate_image_hash(image: Image) -> str:
    with BytesIO() as output:
        image.save(output, format='JPEG')
        data = output.getvalue()
    hash_object = hashlib.sha256(data)
    hex_dig = hash_object.hexdigest()
    return hex_dig

