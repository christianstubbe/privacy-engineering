from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('./creds.json')

from fastapi import APIRouter

gcp_router = APIRouter()
import cloud.gcp.bq
