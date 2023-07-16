import io
import logging
import os
from io import BytesIO
from http import HTTPStatus

from PIL import Image
from fastapi import UploadFile, File, Request, Depends, HTTPException
from fastapi.responses import StreamingResponse
from google.cloud import storage
from google.cloud.exceptions import GoogleCloudError

import transformations
from access.pep import get_pep, PolicyEnforcementPoint
from http import HTTPStatus as status
from utils import calculate_image_hash
from . import router, credentials

logger = logging.getLogger(__name__)

client = storage.Client(credentials=credentials,
                        project=os.getenv("GCP_PROJECT_NAME"))

bucket_name = "company_directory"  # TODO: convert to a config variable


@router.post("/blob")
async def upload_object(request: Request, file: UploadFile = File(...)):
    """
    Uploads a file to a Cloud Storage bucket.
    """
    if not file:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="No upload file sent")
    # 1. Receive object
    file_contents = await file.read()
    img = Image.open(BytesIO(file_contents))
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    # 2. Create a reference
    destination_blob_name = calculate_image_hash(img)
    purp = request.query_params.get("purpose")
    if purp is None or purp == "":
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="No purpose provided.")
    # 3. 
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    try:
        blob.upload_from_file(buffer, content_type='image/jpeg')
    except GoogleCloudError as e:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="No upload file sent")
    if blob.exists():
        return {"result": "success"}


@router.get("/blob/{data_object_id}")
def download_object(data_object_id: str, request: Request, pep: PolicyEnforcementPoint = Depends(get_pep)):
    """Return a blob from a bucket in Google Cloud Storage."""
    purpose = request.query_params.get("purpose") or None
    # TODO: purpose must match, this is done in the PEP
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(data_object_id)
    image_data = blob.download_as_bytes()
    image = Image.open(io.BytesIO(image_data))
    # TODO: retrieve transformation from database
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


# @ehourdebaigt: I guess, this would have to be a check, we should assume that the bucket already exists
def create_bucket(bucket_name: str):
    """Creates a bucket in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)

    logger.info(f"Bucket {bucket.name} created")


# TODO: would be interesting to limit access to this endpoint
@router.get("/bucket")
def list_bucket():
    """
    Returns all the blobs in a bucket Google Cloud Storage.
    """
    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)
    return {"blobs": [blob.name for blob in blobs]}
