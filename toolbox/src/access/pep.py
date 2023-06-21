import casbin, logging
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from exceptions.exceptions import InvalidPurposeException

MODEL_PATH = "models/"
RULE_PATH = "rules/"

logger = logging.getLogger(__name__)

class AccessControlMiddleware(BaseHTTPMiddleware):
    # Dependency to enforce access control
    async def enforce_access_control(self, request: Request, call_next: RequestResponseEndpoint):
        # TODO depending on the path, enforce a different 
        model = request.headers.get("model")
        # Initialize Casbin enforcer with model and policy files
        # enforcer = create_enforcer()
        enforcer = casbin.Enforcer("models/rbac_model.conf", "rules/rbac_policy.csv")
        # Get the subject, object, and action from request headers (or any other source)
        sub = request.headers.get("subject")
        obj = request.headers.get("object")
        act = request.headers.get("action")

        # Check if access is allowed using Casbin enforcer
        if not enforcer.enforce(sub, obj, act):
            raise InvalidPurposeException(act)

        response = await call_next(request)
        return response
    
    def create_enforcer(self, model: str):
        if not ["abac", "pbac", "abac"] in model:
            raise HTTPException(status_code=400, detail="Bad Request")
        return casbin.Enforcer(f"models/{model}_model.conf", f"rules/{model}_policy.csv")
