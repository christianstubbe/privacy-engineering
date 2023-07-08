import logging
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Depends

load_dotenv()

# Middleware
from access.pep import control_access

# Router
from access.pap import pap_router
from cloud.gcp import gcp_router

# Configure app-wide logging
# N.B.: logs are automatically handle by the built-in interface of the cloud provider
logging.basicConfig(
    level=logging.ERROR, format="%(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Our main process
app = FastAPI(debug=True)

app.include_router(pap_router, prefix="/api/v1/pap")
app.include_router(gcp_router, prefix="/api/v1/gcp", dependencies=[Depends(control_access())])


@app.get("/")
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# This function is for the cloud provider
def entry_point(request: Request):
    logger.info(f"Serverless function was triggered! {request}")
    return {"Hello from the entry_point function! 🚀 "}
