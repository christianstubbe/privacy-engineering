from google.cloud import storage


def create_gcs_object(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to a Google Cloud Storage bucket."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    return f"File {source_file_name} uploaded to {destination_blob_name}."


def read_gcs_object(bucket_name: str, source_blob_name: str):
    """Return a blob from a bucket in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    contents = blob.download_as_string()

    return contents


def update_gcs_object(bucket_name: str, blob_name: str, new_name: str):
    """Renames a blob in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    new_blob = bucket.rename_blob(blob, new_name)

    return f"Blob {blob.name} has been renamed to {new_blob.name}"


def delete_gcs_object(bucket_name: str, blob_name: str):
    """Deletes a blob from Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    return f"Blob {blob_name} deleted."


def create_gcs_bucket(bucket_name: str):
    """Creates a bucket in Google Cloud Storage."""

    storage_client = storage.Client()
    bucket = storage_client.create_bucket(bucket_name)

    return f"Bucket {bucket.name} created"


def read_gcs_bucket(bucket_name: str):
    """Returns all the blobs in a bucket Google Cloud Storage."""

    storage_client = storage.Client()
    blobs = storage_client.list_blobs(bucket_name)

    return blobs


def delete_gcs_bucket(bucket_name: str):
    """Deletes a bucket in Google Cloud Stoage. The bucket must be empty."""

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()

    print(f"Bucket {bucket.name} deleted")
