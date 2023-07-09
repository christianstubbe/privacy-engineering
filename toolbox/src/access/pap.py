import logging
from fastapi import APIRouter, HTTPException
from . import enforcer as e
from access.db import session_scope, Purposes
from pydantic import BaseModel
from typing import Optional

logger = logging.getLogger(__name__)

pap_router = APIRouter()


class PurposeIn(BaseModel):
    name: str
    # exceptions: Optional[list[str]] = [""]
    # transformations: Optional[list[str]] = [""]


class ListHandler(logging.Handler):
    def __init__(self, log_list):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        # Record is a LogRecord object, whose attribute 'msg' contains the log message
        self.log_list.append(record.msg)


@pap_router.post("/purpose/{purpose_name}", status_code=200)
async def add_purpose(purpose: PurposeIn):
    purpose_dict = purpose.dict()
    with session_scope() as session:
        purpose = Purposes(**purpose_dict)
        try:
            query = session.add(purpose)
        except Exception as exc:
            raise HTTPException(detail=f"A purpose with that name already exists. {exc.pgerror}", status_code=405)
        # last_record_id = await database.execute(query)
        logger.info(f"Added new purpose: {purpose_dict['name']}")
        return {**purpose_dict, "id": 0}


@pap_router.get("/purposes")
def list_purposes():
    with session_scope() as session:
        purposes = session.query(Purposes).all()
        return purposes


@pap_router.get("/policy")
def get_policy():
    log_list = []
    handler = ListHandler(log_list)
    logger.addHandler(handler)
    e.model.print_policy()
    logger.removeHandler(handler)
    return log_list


@pap_router.put("/exception")
def add_exception(item):
    items_dict = item.dict()  # Request body
    purpose_name = items_dict["purpose"]
    logger.info(f"Added new exception for purpose: {purpose_name}")

