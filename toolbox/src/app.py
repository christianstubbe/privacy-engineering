from fastapi import FastAPI, APIRouter, Request, HTTPException, Depends
import logging
# Middleware
from access import AccessControlMiddleware
# Router
from storage import cloud_router

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(levelname)s: %(message)s')

# Our main process
app = FastAPI()

# Configure 
app.add_middleware(AccessControlMiddleware)

# Include the router in the FastAPI app
app.include_router(cloud_router, prefix="/cloud")

logging.info("Serverless function was triggered!")
