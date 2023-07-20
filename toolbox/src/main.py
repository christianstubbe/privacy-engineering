from dotenv import load_dotenv

load_dotenv()

import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
# Routers
from access.pap import router as pap_router
from cloud.gcp import router as cloud_router
from auth import JWTMiddleware

# Configure app-wide logging
# N.B.: logs are automatically handle by the built-in interface of the cloud provider
logging.basicConfig(
    level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Our main process
app = FastAPI(debug=True)
app.add_middleware(JWTMiddleware)
app.include_router(pap_router, prefix="/api/v1/pap")
app.include_router(cloud_router, prefix="/api/v1/gcp")

origins = [
    "http://localhost:3000",  # React app
    "http://localhost:8000",  # FastAPI server (if they are on the same machine)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    from access.db import database
    await database.connect()
    logger.info("Connected to the database!")


@app.on_event("shutdown")
async def shutdown():
    from access.db import database
    await database.disconnect()
    logger.info("Disconnected from the database!")


# This function is for the cloud provider
def entry_point(request: Request):
    logger.info(f"Serverless function was triggered! {request}")
    return {"Hello from the entry_point function! 🚀 "}
