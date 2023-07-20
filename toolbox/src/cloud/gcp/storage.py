import io
import logging
import os
import json
from http import HTTPStatus
from http import HTTPStatus as status
from io import BytesIO
from typing import List

from PIL import Image
from fastapi import UploadFile, File, Request, Depends, HTTPException, Form
from fastapi.responses import StreamingResponse
from google.cloud import storage
from google.cloud.exceptions import GoogleCloudError
from sqlalchemy.orm import Session

import transformations
from access.db import get_db, DataObject
from access.pap.pap import create_data_object_purposes
from access.pep import get_pep, PolicyEnforcementPoint
from utils import calculate_image_hash
from . import router, credentials

logger = logging.getLogger(__name__)

client = storage.Client(credentials=credentials,
                        project=os.getenv("GCP_PROJECT_NAME"))

bucket_name = "company_directory"  # TODO: convert to a config variable


@router.post("/blob")
async def upload_object(ids: str = Form(...),
                        files: List[UploadFile] = File(...), 
                        db: Session = Depends(get_db)):
    """
    Uploads a file to a Cloud Storage bucket.
    """
    purpose_ids = json.loads(ids) # TODO: checks if purposes exist.
    if len(files) < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="No file to upload.")
    
    # 1. Receive object(s)
    for file in files:
        file_contents = await file.read()
        img = Image.open(BytesIO(file_contents))
        buffer = io.BytesIO()
        img.save(buffer, format="JPEG")
        buffer.seek(0)
        # 2. Create a reference to a DataObject in the DB
        # TODO: this should probably be elsewhere to make sure we don't skip important steps
        destination_blob_name = calculate_image_hash(img) # That helps us avoid duplicate images
        do = DataObject(name=destination_blob_name)
        db.add(do)
        # 3. Link the DataObject to its purposes
        data_object_purposes = create_data_object_purposes(db, do, purpose_ids)
        db.add_all(data_object_purposes)
        # 4. Upload it to bucket
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        exist = False
        try:
            blob.upload_from_file(buffer, content_type='image/jpeg')
            exist = blob.exists()
        except GoogleCloudError as e:
            raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=e)
    return {"result": "success" if exist else "failed"}


@router.get("/blob/{data_object_id}")
def download_object(data_object_id: str, request: Request, pep: PolicyEnforcementPoint = Depends(get_pep)):
    """Return a blob from a bucket in Google Cloud Storage."""
    purpose = request.query_params.get("purpose") or None
    # TODO: purpose must match, this is done in the PEP
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(data_object_id)
    image_data = blob.download_as_bytes()
    image = Image.open(io.BytesIO(image_data))
    # TODO: retrieve transformation from DataObject
    try:
        return {"transformations": pep.get_permissions_for_purpose(data_object_id, purpose)}
    except ValueError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data object not found.")
    transformed_img = transformations.transform(image, transformations.Transformations.BLACKWHITE)
    byte_arr = io.BytesIO()
    # TODO: it's possible to programmatically read the mimetypes
    transformed_img.save(byte_arr, format='JPEG')
    byte_arr.seek(0)
    return StreamingResponse(byte_arr, media_type="image/jpeg")

