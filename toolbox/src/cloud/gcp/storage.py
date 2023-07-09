import os
from google.cloud import storage
import transformations
from . import gcp_router, credentials
import logging
from fastapi import UploadFile
from utils import calculate_image_hash, get_bytes
from typing import Annotated, Union
from PIL import Image
from io import BytesIO
import io

logger = logging.getLogger(__name__)
client = storage.Client(credentials=credentials,
                        project=os.getenv("GCP_PROJECT_NAME"))

bucket_name = "company_directory"


@gcp_router.post("/blob")
async def create_gcs_object(file: UploadFile):
    """
    Uploads a file to a Google Cloud Storage bucket.
    """
    if not file:
        return {"message": "No upload file sent"}
    file_contents = await file.read()
    img = Image.open(BytesIO(file_contents))
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG")
    buffer.seek(0)
    destination_blob_name = calculate_image_hash(img)
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(buffer, content_type='image/jpeg')
    logger.info(f"File {file.filename} uploaded to {destination_blob_name}.")
    return {"result": "success"}


@gcp_router.get("/blob/{bucket_name}/{source_blob_name}")
def read_gcs_object(bucket_name: str, source_blob_name: str) -> str:
    """Return a blob from a bucket in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    img = blob()  # TODO
    transformed_img = transformations.transform(img)
    return transformed_img


# TODO: will it be needed?
@gcp_router.put("/blob/{bucket_name}/{blob_name}/{new_name}")
def update_gcs_object(bucket_name: str, blob_name: str, new_name: str):
    """Renames a blob in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    new_blob = bucket.rename_blob(blob, new_name)

    logger.info(f"Blob {blob.name} has been renamed to {new_blob.name}")


@gcp_router.delete("/bucket/{bucket_name}/{blob_name}")
def delete_gcs_object(bucket_name: str, blob_name: str) -> str:
    """Deletes a blob from Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    logger.info(f"Blob {blob_name} in {bucket_name} was deleted.")


@gcp_router.post("/bucket/{bucket_name}")
def create_gcs_bucket(bucket_name: str):
    """Creates a bucket in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)

    logger.info(f"Bucket {bucket.name} created")


# TODO: make it call
@gcp_router.get("/gcs/bucket/{bucket_name}")
def read_gcs_bucket(bucket_name: str):
    """Returns all the blobs in a bucket Google Cloud Storage."""

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    return blobs


@gcp_router.delete("/bucket/{bucket_name}")
def delete_gcs_bucket(bucket_name: str) -> None:
    """Deletes a bucket in Google Cloud Stoage. The bucket must be empty."""

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()
    logger.info(f"Bucket {bucket.name} deleted")
