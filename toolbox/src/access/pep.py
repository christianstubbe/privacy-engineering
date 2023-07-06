import casbin
import logging
from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
# from exceptions.exceptions import InvalidPurposeException

from adapters.mongo_casbin import adapter

logger = logging.getLogger(__name__)


class AccessControlMiddleware(BaseHTTPMiddleware):
    # Dependency to enforce access control
    async def dispatch(self, request, call_next):
        # TODO depending on the path, enforce a different
        model = request.headers.get("model")
        # Initialize Casbin enforcer with model and policy files
        # enforcer = create_enforcer()
        enforcer = casbin.Enforcer(
            "./access/models/rbac_model.conf", adapter
        )
        # Get the subject, object, and action from request headers (or any other source)
        sub = request.headers.get("subject")
        obj = request.headers.get("object")
        act = request.headers.get("action")

        enforcer.enforce(sub, obj, act)

        response = await call_next(request)
        return response

    def create_enforcer(self, model: str):
        if not ["abac", "pbac", "rbac"] in model:
            raise HTTPException(status_code=400, detail="Bad Request")
        return casbin.Enforcer(
            f"models/{model}_model.conf", f"rules/{model}_rules.conf"
        )
