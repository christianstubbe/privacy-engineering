import logging
from fastapi import APIRouter, HTTPException
from typing import List
import uuid
import os
from pydantic import BaseModel
from . import enforcer as e

logger = logging.getLogger(__name__)

pap_router = APIRouter()


class RequestBody(BaseModel):
    purpose_name: str
    exception: str
    description: str | None = None


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


class Purpose:
        name: str
        parent_id: uuid
        transformations: list[str]
        exceptions: list[uuid]


@pap_router.get("/purpose/add/{purpose_name}", status_code=200)
def add_purpose(purpose_name: str):
    logger.info(f"Added new purpose: {purpose_name}")
    e.add_policy("data", "alice", "test", purpose_name)
    return {"result": "success"}


@pap_router.get("/purpose/list")
async def list_purposes():
    pass


@pap_router.get("/purpose/{id}")
async def get_purpose(id: str):
    pass


@pap_router.post("/exceptions/add")
def add_exception(item: RequestBody):
    items_dict = item.dict()  # Request body
    purpose_name = items_dict["purpose"]
    logger.info(f"Added new exception for purpose: {purpose_name}")


@pap_router.get("/policies/list")
def list_policies():
    directory = './access/models'
    return os.listdir(directory)
