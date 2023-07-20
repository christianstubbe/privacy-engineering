import logging

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
