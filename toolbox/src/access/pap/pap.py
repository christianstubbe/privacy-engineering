import logging
from typing import Dict

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# from access import enforcer as e
from access.db import get_db, Purpose, DataObjectPurpose, DataObject

logger = logging.getLogger(__name__)

from . import router
from access.db.schemas import *


@router.get("/purposes")
def read_purposes(db: Session = Depends(get_db)):
    purposes = db.query(Purpose).all()
    return purposes


# TODO
@router.post("/purposes")
def add_purpose_to_tree(parent_id: int, purpose: PurposeModel, db: Session = Depends(get_db)):
    db_parent = db.query(Purpose).filter(Purpose.id == parent_id).first()
    if db_parent is None:
        raise HTTPException(status_code=404, detail="Parent purpose not found")
    db.add(Purpose(name=purpose.name, parent_id=parent_id, metadata=purpose.metadata))
    return {"name": purpose.name, "parent_id": parent_id, "metadata": purpose.metadata}


def create_data_object_purposes(db: Session, data_object, purpose_ids):
    data_object_purposes = []

    for purpose_id in purpose_ids:

        purpose = db.query(Purpose).filter(Purpose.id == purpose_id).first()

        data_object_purpose = DataObjectPurpose(
            data_object=data_object,
            purpose=purpose,
            active=True
        )
        data_object_purposes.append(data_object_purpose)

    return data_object_purposes
