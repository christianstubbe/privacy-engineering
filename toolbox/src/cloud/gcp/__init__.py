import os

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(os.getenv("GCP_CRED_FILE"))

from fastapi import APIRouter

gcp_router = APIRouter()
import cloud.gcp.bq
import cloud.gcp.storage
