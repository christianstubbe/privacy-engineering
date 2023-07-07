import logging
from fastapi import APIRouter, HTTPException
from typing import List
import uuid
import os
from pydantic import BaseModel
from access.pep import enforcer as e

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


@pap_router.post("/purpose/add/{purpose_name}", status_code=200)
async def add_purpose(purpose_name: str):
    # if collection.find_one({"purpose": purpose_name}):
    #    raise HTTPException(status_code=400, detail="A purpose with that name already exists.")
    # purpose = Purpose(purpose_name)
    # purpose_dict = vars(purpose)
    # collection.insert_one(purpose_dict)
    await e.add_policy("data", "alice", "test", "test")
    logger.info(f"Added new purpose: {purpose_name}")
    return {"result": "success"}


@pap_router.get("/purpose/list")
async def list_purposes():
    # query = .select()
    # return await database.fetch_all(query)
    pass


@pap_router.get("/purpose/{id}")
async def get_purpose(id: str):
    # query = users.select().where(users.c.id == user_id)
    # result = await database.fetch_one(query)
    # if not result:
    #     raise HTTPException(status_code=404, detail="User not found")
    # return result
    pass


@pap_router.post("/exceptions/add")
def add_exception(item: RequestBody):
    items_dict = item.dict()  # Request body
    purpose_name = items_dict["purpose"]
    exception = items_dict["exception"]
    # purpose = Purpose(**collection.find_one({purpose_name}))
    # purpose.add_exception(exception)
    logger.info(f"Added new exception for purpose: {purpose_name}")
    # return collection.find_one({"exceptions": exception})


@pap_router.get("/policies/list")
def list_policies():
    directory = './access/models'
    return os.listdir(directory)
