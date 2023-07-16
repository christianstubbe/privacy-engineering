import os

from fastapi import FastAPI, Request, HTTPException, Response
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from jose import jwt, JWTError
import requests

project_nb = os.getenv("GCP_PROJECT_NB")
project_name = os.getenv("GCP_PROJECT_NAME")
AUDIENCE = f"/projects/{project_nb}/apps/{project_name}"
GOOGLE_CERTS_URL = "https://www.googleapis.com/oauth2/v1/certs"


class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
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
