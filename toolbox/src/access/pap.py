import logging
from fastapi import APIRouter
import hashlib
from . import enforcer as e
from access.db import database, session_scope, Purpose

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

pap_router = APIRouter()


class ListHandler(logging.Handler):
    def __init__(self, log_list):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        # Record is a LogRecord object, whose attribute 'msg' contains the log message
        self.log_list.append(record.msg)


@pap_router.post("/purpose/{purpose_name}", status_code=200)
async def add_purpose(purpose_name: str):
    with session_scope() as session:
        query = session.insert(Purpose).values(name=purpose_name)
        last_record_id = await database.execute(query)
        logger.info(f"Added new purpose: {purpose_name}")


@pap_router.get("/purpose")
def list_purposes():
    with session_scope() as session:
        purposes = session.query(Purpose).all()
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


def tag_content(content, purpose: str):
    my_list_as_bytes = str(content).encode()
    my_hash = hashlib.sha256(my_list_as_bytes)
    sub = ""
    obj = my_hash
    act = ""
    purp = purpose
    e.add_policy(sub, obj, act, purpose)
