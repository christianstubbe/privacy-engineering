from google.cloud import bigquery
import logging
from . import gcp_router

logger = logging.getLogger(__name__)


@gcp_router.get("/bq/query")
def query_bq(query: str):
    """Executes a client query in BigQuery and returns the result."""

    client = bigquery.Client()
    query_job = client.query(query)

    return query_job


@gcp_router.post("/bq/create")
def create_bq_dataset(dataset_id: str, location: str) -> str:
    """
    Create a new dataset in BigQuery based on the query params.
    """

    client = bigquery.Client()
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.

    logging.info(f"Created dataset {client.project}.{dataset.dataset_id}")


@gcp_router.delete("/bq/delete")
def delete_bq_dataset(dataset_id: str) -> str:
    """Deletes a dataset in BigQuery."""

    client = bigquery.Client()
    client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)

    logger.info("Deleted dataset '{dataset_id}'.")
