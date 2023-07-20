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
from access.db import get_db, DataObject, DataObjectPurpose, Purpose
from access.pap.pap import create_data_object_purposes
from access.pep import get_pep, PolicyEnforcementPoint
from utils import calculate_image_hash
from . import router, credentials

logger = logging.getLogger(__name__)

client = storage.Client(credentials=credentials,
                        project=os.getenv("GCP_PROJECT_NAME"))


def validate_purpose_ids(db: Session, ids: List[str]):
    for id in ids:
        purpose = db.query(Purpose).filter(Purpose.id == id).first()
        if not purpose:
            return False
    return True


def upload_to_bucket(blob_name, blob_data, content_type):
    bucket_name = os.getenv('GOOGLE_CLOUD_BUCKET')
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.upload_from_string(
        blob_data,
        content_type=content_type
    )

    return blob.public_url


@router.post("/blob")
async def upload_object(
    purpose_ids: str = Form(...),
    files: List[UploadFile] = File(...),
    db: Session = Depends(get_db),
):
    ids = json.loads(purpose_ids)
    if not validate_purpose_ids(db, ids):
        raise HTTPException(status_code=400, detail="Invalid purpose ids.")

    if len(files) < 1:
        raise HTTPException(status_code=422, detail="No file to upload.")

    results = []
    for file in files:
        try:
            file_contents = await file.read()
            img = Image.open(io.BytesIO(file_contents))
            img_format = img.format

            destination_blob_name = calculate_image_hash(img)

            upload_to_bucket(destination_blob_name, file_contents,
                             content_type=f'image/{img_format}')

            # Create a reference to a DataObject in the DB
            do = DataObject(name=destination_blob_name)
            db.add(do)

            # Link the DataObject to its purposes
            data_object_purposes = create_data_object_purposes(db, do, ids)
            db.add_all(data_object_purposes)

            db.commit()
            results.append({"filename": file.filename, "result": "success"})
        except:
            pass
        # except Exception as e:
        #    logger.error(f"Failed to process file {file.filename}: {str(e)}")
        #    results.append({"filename": file.filename, "result": "error", "detail": str(e)})
    return results


@router.get("/blob")
def download_objects(request: Request, pep: PolicyEnforcementPoint = Depends(get_pep), db: Session = Depends(get_db)):
    """Return a blob from a bucket in Google Cloud Storage."""
    purpose_id = request.query_params.get("purpose") or None
    blobs = db.query(DataObjectPurpose).options(
        joinedload(DataObjectPurpose.data_object),
        joinedload(DataObjectPurpose.purpose).joinedload(Purpose.transformation)
    ).filter(
        DataObjectPurpose.purpose_id == purpose_id).all()

    transformed_images = []

    for blob in blobs:
        bucket = client.get_bucket(os.getenv("GOOGLE_CLOUD_BUCKET"))
        blob_object = bucket.blob(blob.data_object.name)
        image_data = blob_object.download_as_bytes()
        image = Image.open(io.BytesIO(image_data))

        transformation = blob.purpose.transformation

        if transformation.blackwhite:
            image = transformations.black_white(image)
        if transformation.removebg:
            image = transformations.remove_background(image)
        if transformation.blur:
            image = transformations.blur(image)
        if transformation.downsize:
            image = transformations.downsize(image)
        if transformation.erosion:
            image = transformations.erosion(image)

        byte_arr = io.BytesIO()
        image.save(byte_arr, format='JPEG')
        byte_arr.seek(0)
        transformed_images.append(base64.b64encode(byte_arr.read()).decode('utf-8'))

    return transformed_images
