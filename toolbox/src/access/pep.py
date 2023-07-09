from . import enforcer
import logging
from fastapi import Request
from exceptions import InvalidPurposeException

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
