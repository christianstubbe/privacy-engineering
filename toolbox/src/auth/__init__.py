from fastapi import Request, HTTPException
from jose import jwt, JWTError
import requests
import os


project_nb = os.getenv("GCP_PROJECT_NB")
project_name = os.getenv("GCP_PROJECT_NAME")
AUDIENCE = f"/projects/{project_nb}/apps/{project_name}"
GOOGLE_CERTS_URL = "https://www.googleapis.com/oauth2/v1/certs"


async def iap_jwt_middleware(request: Request, call_next):
    token = request.headers.get('x-goog-iap-jwt-assertion')
    if token:
        try:
            certs = requests.get(GOOGLE_CERTS_URL).json()
            payload = jwt.decode(token, certs, algorithms=['RS256'], audience=AUDIENCE)
            request.state.user = payload.get("email")
        except JWTError as e:
            raise HTTPException(status_code=401, detail="Invalid token")
    response = await call_next(request)
    return response

