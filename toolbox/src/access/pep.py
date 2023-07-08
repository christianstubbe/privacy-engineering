from . import enforcer
import logging
from fastapi import HTTPException, Request

logger = logging.getLogger(__name__)


def control_access():
    def _middleware(request: Request):  
        sub = request.query_params.get("subject")
        obj = request.query_params.get("object")
        act = request.query_params.get("action")

        if not enforcer.enforce(sub, obj, act):
            raise HTTPException(status_code=403, detail="Access denied")
        return request

    return _middleware
