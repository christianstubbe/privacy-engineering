from fastapi import FastAPI, Request, HTTPException, Depends
import casbin

app = FastAPI()

# Initialize Casbin enforcer with model and policy files
enforcer = casbin.Enforcer("rbac_model.conf", "rbac_policy.csv")

# Dependency to enforce access control
async def enforce_access_control(request: Request):
    # Get the subject, object, and action from request headers (or any other source)
    sub = request.headers.get("subject")
    obj = request.headers.get("object")
    act = request.headers.get("action")

    # Check if access is allowed using Casbin enforcer
    if not enforcer.enforce(sub, obj, act):
        # Raise 403 Forbidden if access is denied
        raise HTTPException(status_code=403, detail="Access denied")

# Define a protected route
@app.get("/protected-resource", dependencies=[Depends(enforce_access_control)])
async def protected_resource():
    return {"message": "Access to protected resource granted"}
