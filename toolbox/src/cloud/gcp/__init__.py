import os
import json
from google.oauth2 import service_account

service_account_json = json.loads(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
credentials = service_account.Credentials.from_service_account_info(service_account_json)

from fastapi import APIRouter

router = APIRouter()
import cloud.gcp.storage
