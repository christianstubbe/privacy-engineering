from cloud.interface import CloudAPIInterface
import logging
logger = logging.getLogger(__name__)
client = bigquery.Client(credentials=credentials,
                         project=os.getenv("GCP_PROJECT_NAME"))

class GoogleWrapper(CloudAPIInterface):
    
    