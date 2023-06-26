from google.cloud import bigquery

def queryBQ(query):
    """Executes a client query in BigQuery and returns the result."""

    client = bigquery.Client()
    query_job = client.query(query)

    return query_job


def createBQDataset(dataset_id, location):
    """Create a new dataset in BigQuery."""
    
    client = bigquery.Client()
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = location
    dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
    
    return "Created dataset {}.{}".format(client.project, dataset.dataset_id)


def deleteBQDataset(dataset_id):
    """Deletes a dataset in BigQuery."""

    client = bigquery.Client()
    client.delete_dataset(
        dataset_id, delete_contents=True, not_found_ok=True
    )  

    return "Deleted dataset '{}'.".format(dataset_id)