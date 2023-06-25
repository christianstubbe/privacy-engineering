from fastapi import FastAPI
import logging

# Middleware
from access.pep import AccessControlMiddleware

# Router
from api.storage import cloud_router
from access.pap import pap_router

# Configure app-wide logging
# N.B.: logs are automatically handle by the built-in interface of the cloud provider
logging.basicConfig(
    level=logging.ERROR, format="%(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Our main process
app = FastAPI()

app.add_middleware(AccessControlMiddleware)

app.include_router(cloud_router, prefix="/api/v1")
app.include_router(pap_router, prefix="/api/v1")


@app.get("/")
def hello_world():
    return {"message": "hello, world!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


logger.info("Serverless function was triggered!")
