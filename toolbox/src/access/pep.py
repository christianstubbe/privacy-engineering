import casbin
import logging
from fastapi import HTTPException, Request
from .adapters.mongo import adapter

logger = logging.getLogger(__name__)


def control_access():
    def _middleware(request: Request):
        model = request.path_params.get("model")
        # Initialize Casbin enforcer with model and policy files
        # enforcer = create_enforcer()
        enforcer = casbin.Enforcer(
            "./access/models/rbac_model.conf", adapter
        )
        # Get the subject, object, and action from request headers (or any other source)
        sub = request.path_params.get("subject")
        obj = request.path_params.get("object")
        act = request.path_params.get("action")

        if not enforcer.enforce(sub, obj, act):
            pass
            # raise HTTPException(status_code=403, detail="Access denied")
        return request

    return _middleware


def create_enforcer(model: str):
    if not ["abac", "pbac", "rbac"] in model:
        raise HTTPException(status_code=400, detail="Bad Request")
    return casbin.Enforcer(
        f"models/{model}_model.conf", adapter
    )
