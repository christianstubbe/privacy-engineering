from . import enforcer
import logging
from fastapi import Request
from exceptions import InvalidPurposeException
from PIL import Image
from utils import calculate_image_hash

logger = logging.getLogger(__name__)


def control_access():
    def _middleware(request: Request):
        sub = request.query_params.get("subject")
        obj = request.query_params.get("object")
        act = request.query_params.get("action")
        purp = request.query_params.get("purpose")

        if not enforcer.enforce(sub, obj, act, purp):
            raise InvalidPurposeException(purp)
        return request

    return _middleware


def tag_content(content: Image, sub: str = "", act: str = "", purp: str = ""):
    obj = calculate_image_hash(content)
    logger.info(f"Adding a new policy rule with sub: {sub}, obj: {obj}, act: {act}, purp: {purp}")
    enforcer.add_policy(sub, obj, act, purp)
