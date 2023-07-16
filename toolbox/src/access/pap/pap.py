import logging
from typing import Dict

from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from access import enforcer as e
from access.db import get_db, Purpose, DataObjectPurpose, DataObject

logger = logging.getLogger(__name__)

router = APIRouter()


class ListHandler(logging.Handler):
    def __init__(self, log_list):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        # Record is a LogRecord object, whose attribute 'msg' contains the log message
        self.log_list.append(record.msg)


@router.get("/blob/{object_id}/purposes")
def read_purpose_tree_for_object(object_id: int, db: Session = Depends(get_db)):
    db_object = db.query(DataObject).filter(DataObject.id == object_id).first()
    if db_object is None:
        raise HTTPException(status_code=404, detail="Data object not found")

    purpose_tree = []
    for purpose_link in db_object.purposes:
        purpose_tree.append(generate_purpose_tree(purpose_link.purpose, db))

    return {"object_id": object_id, "purpose_tree": purpose_tree}


def generate_purpose_tree(purpose: Purpose, db: Session) -> Dict:
    purpose_dict = {
        "id": purpose.id,
        "name": purpose.name,
        "metadata": purpose.metadata,
        "active": purpose.active,
        "children": []
    }
    children = db.query(Purpose).filter(Purpose.parent_id == purpose.id).all()
    for child in children:
        purpose_dict["children"].append(generate_purpose_tree(child, db))
    return purpose_dict


# Only relevant when casbin is used as PEP
@router.get("/policy")
def get_policy():
    log_list = []
    handler = ListHandler(log_list)
    logger.addHandler(handler)
    e.model.print_policy()
    logger.removeHandler(handler)
    return log_list

