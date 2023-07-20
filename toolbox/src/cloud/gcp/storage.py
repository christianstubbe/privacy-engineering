import base64
import io
import json
import logging
import os
from http import HTTPStatus
from io import BytesIO
from typing import List

from PIL import Image
from fastapi import UploadFile, File, Request, Depends, HTTPException, Form
from google.cloud import storage
from google.cloud.exceptions import GoogleCloudError
from sqlalchemy.orm import Session, joinedload

import transformations
from access.db import get_db, DataObject, DataObjectPurpose
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
    purpose_ids = json.loads(ids)  # TODO: checks if purposes exist.
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


@router.get("/blob")
def download_objects(request: Request, pep: PolicyEnforcementPoint = Depends(get_pep), db: Session = Depends(get_db)):
    """Return a blob from a bucket in Google Cloud Storage."""
    purpose_id = request.query_params.get("purpose") or None
    blobs = db.query(DataObjectPurpose).options(joinedload(DataObjectPurpose.data_object)).filter(DataObjectPurpose.purpose_id == purpose_id).all()

    transformed_images = []

    for blob in blobs:
        bucket = client.get_bucket(bucket_name)
        blob = bucket.blob(blob.data_object.name)
        image_data = blob.download_as_bytes()
        image = Image.open(io.BytesIO(image_data))
        # TODO: retrieve transformation from DataObject
        transformed_img = transformations.transform(image, transformations.Transformations.BLACKWHITE)
        byte_arr = io.BytesIO()
        # TODO: it's possible to programmatically read the mimetypes
        transformed_img.save(byte_arr, format='JPEG')
        byte_arr.seek(0)

        # Encode the image to base64 and append to the list
        transformed_images.append(base64.b64encode(byte_arr.read()).decode('utf-8'))

    # Returns a list of base64 encoded images
    return transformed_images
