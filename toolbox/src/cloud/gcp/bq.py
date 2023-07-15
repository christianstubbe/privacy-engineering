import os

from google.cloud import bigquery
from google.cloud.exceptions import GoogleCloudError

import logging
from . import router, credentials

logger = logging.getLogger(__name__)
client = bigquery.Client(credentials=credentials,
                         project=os.getenv("GCP_PROJECT_NAME"))


@router.get("/bq/{query}")
def query_bq(query: str):
    """Executes a client query in BigQuery and returns the result."""
    query_job = client.query(query)
    return list(query_job)


@router.post("/bq")
def create_bq_dataset(dataset_id: str, location: str) -> str:
    """
    Create a new dataset in BigQuery based on the query params.
    """
    
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.

    logging.info(f"Created dataset {client.project}.{dataset.dataset_id}")
    return {"result": "success"}


@router.delete("/bq")
def delete_bq_dataset(dataset_id: str) -> str:
    """Deletes a dataset in BigQuery."""
    client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
    logger.info("Deleted dataset '{dataset_id}'.")
    return {"result": "success"}
