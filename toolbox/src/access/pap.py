import logging
from fastapi import APIRouter, HTTPException
from utils.db import collection
from typing import List
import uuid
import os
from pydantic import BaseModel

logger = logging.getLogger(__name__)

pap_router = APIRouter()


class Item(BaseModel):
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
    def __init__(self, name: str, parent_id="",
                 exceptions=[""], transformations=[""]):
        self.purpose = name
        self.parent_id = parent_id
        self.exceptions = exceptions
        self.transformations = transformations

    def add_exception(self, purpose_id: str):
        if is_valid_uuid(purpose_id):
            self.exceptions.append(purpose_id)


# TODO: replace function with ** op
def cast_purpose(obj) -> Purpose:
    return Purpose(
        obj["name"],
        obj["_id"],
        obj["parent_id"],
        obj["exceptions"],
        obj["transformations"]
    )


@pap_router.post("/purpose/add/{purpose_name}", status_code=200)
def add_purpose(purpose_name: str):
    if collection.find_one({"purpose": purpose_name}):
        raise HTTPException(status_code=400, detail="A purpose with that name already exists.")
    purpose = Purpose(purpose_name)
    purpose_dict = vars(purpose)
    collection.insert_one(purpose_dict)
    logger.info(f"Added new purpose: {purpose_name}")
    return {"result": "success"}


@pap_router.get("/purpose/list")
def list_purposes():
    cursor = collection.find({}, {'_id': 0})
    documents = list(cursor)
    if len(documents) == 0:
        raise HTTPException(status_code=404, detail="No purpose exists in the collection.")
    return documents


@pap_router.get("/purpose/{id}")
def get_purpose(id: str):
    document = collection.find_one({"_id": id})
    if document is None:
        raise HTTPException(status_code=404, detail=f"No purpose found with that ID: {id}")
    return document


@pap_router.post("/exceptions/add")
def add_exception(item: Item):
    items_dict = item.dict()  # Request body
    purpose_name = items_dict["purpose"]
    exception = items_dict["exception"]
    purpose = cast_purpose(collection.find_one({purpose_name}))
    purpose.add_exception(exception)
    logger.info(f"Added new exception for purpose: {purpose_name}")
    return collection.find_one({"exceptions": exception})


@pap_router.get("/policies/list", response_model=List[str])
def list_policies():
    directory = './access/models'
    return os.listdir(directory)
