import logging
from fastapi import APIRouter
from adapters.db import collection
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


class PolicyAdministrationPoint:
    def __init__(self):
        pass


class Purpose:
    def __init__(self, name: str, parent_id: uuid, _id=uuid.uuid4(),
                 exceptions=[""], transformations=[""]) -> None:
        self.purpose = name
        self._id = _id
        self.parent_id = parent_id
        self.exceptions = exceptions
        self.transformations = transformations

    def add_exception(self, purpose_id: str):
        if is_valid_uuid(purpose_id):
            self.exceptions.append(purpose_id)


def cast_purpose(obj) -> Purpose:
    return Purpose(
        obj["name"],
        obj["_id"],
        obj["parent_id"],
        obj["exceptions"],
        obj["transformations"]
    )


@pap_router.post("/purpose/add/{purpose_name}")
def add_purpose(purpose_name: str):
    purpose = Purpose(purpose_name)
    collection.insert_one(purpose)
    logger.info(f"Added new purpose: {purpose_name}")


@pap_router.get("/purpose/list/")
def list_purposes():
    purpose = Purpose(purpose_name)
    collection.insert_one(purpose)
    logger.info(f"Added new purpose: {purpose_name}")


@pap_router.post("/exceptions/add/")
def add_exception(item: Item):
    items_dict = item.dict()
    purpose_name = items_dict["purpose_name"]
    exception = items_dict["exception"]
    purpose = cast_purpose(collection.find_one({purpose_name}))
    purpose.add_exception(exception)
    logger.info(f"Added new exception for purpose: {purpose_name}")


@pap_router.get("/policies/list", response_model=List[str])
def list_policies():
    directory = './access/models'
    return os.listdir(directory)
