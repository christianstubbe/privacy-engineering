import casbin
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint

class AccessControlMiddleware(BaseHTTPMiddleware):
# Dependency to enforce access control
    async def enforce_access_control(self, request: Request, call_next: RequestResponseEndpoint):
        # TODO depending on the path, enforce a different 
        # Initialize Casbin enforcer with model and policy files
        enforcer = casbin.Enforcer("models/rbac_model.conf", "rules/rbac_policy.csv")
        # Get the subject, object, and action from request headers (or any other source)
        sub = request.headers.get("subject")
        obj = request.headers.get("object")
        act = request.headers.get("action")

        # Check if access is allowed using Casbin enforcer
        if not enforcer.enforce(sub, obj, act):
            # Raise 403 Forbidden if access is denied
            raise HTTPException(status_code=403, detail="Access denied")

        response = await call_next(request)
        return response
