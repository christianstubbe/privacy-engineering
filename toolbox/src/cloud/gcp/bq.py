import os

from google.cloud import bigquery
import logging
from . import gcp_router, credentials

logger = logging.getLogger(__name__)
client = bigquery.Client(credentials=credentials,
                         project=os.getenv("GCP_PROJECT_NAME"))


@gcp_router.get("/bq/{query}")
def query_bq(query: str):
    """Executes a client query in BigQuery and returns the result."""
    query_job = client.query(query)
    return list(query_job)


@gcp_router.post("/bq")
def create_bq_dataset(dataset_id: str, location: str) -> str:
    """
    Create a new dataset in BigQuery based on the query params.
    """
    
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.

    logging.info(f"Created dataset {client.project}.{dataset.dataset_id}")
    return {"result": "success"}


@gcp_router.delete("/bq")
def delete_bq_dataset(dataset_id: str) -> str:
    """Deletes a dataset in BigQuery."""
    client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
    logger.info("Deleted dataset '{dataset_id}'.")
    return {"result": "success"}
