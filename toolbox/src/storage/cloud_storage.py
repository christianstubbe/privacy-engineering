from fastapi import APIRouter, Request, HTTPException, Depends
import json, os

cloud_router = APIRouter()

# TODO: Get blob data with REST calls
@cloud_router.get("/rdb")
async def get_relational_db():
    """
    Query data from relational database
    """
    env_value = os.environ.get('MY_ENV_VARIABLE', 'default_value')
    return json.dumps("it's alive!")

# TODO: Post blob data with REST calls

# TODO: Get blob data with REST calls

# TODO: Post blob data with REST calls
