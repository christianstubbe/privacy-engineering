from fastapi import APIRouter, Request, HTTPException, Depends
import json, os, requests, logging
# TODO: import utilitary file for data transformation
logger = logging.getLogger(__name__)

cloud_router = APIRouter()

# Bearer token
token = os.environ.get('SERVICE_ACCOUNT_TOKEN')
if token is None:
    logger.error("Token is not set! Cannot make a request")
    # raise HTTPException(status_code=500, detail="Improperly set function!")

headers = {
    'Authorization': f'Bearer {token}'
}

# TODO: Get RDB data with REST calls
@cloud_router.get("/data/rdb")
async def get_relational_db():
    """
    Query data from relational database
    """
    url = 'https://example.com/api/resource'
    response = requests.get(url, headers=headers)
    return json.dumps("it's alive!")

# TODO: Post RDB data with REST calls

# TODO: Get blob data with REST calls

# TODO: Post blob data with REST calls

# TODO: Query/upload with images
