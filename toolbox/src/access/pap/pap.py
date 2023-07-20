import logging
from typing import Dict

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# from access import enforcer as e
from access.db import get_db, Purpose, DataObjectPurpose, DataObject

logger = logging.getLogger(__name__)

from . import router
from access.db.schemas import *


class ListHandler(logging.Handler):
    def __init__(self, log_list):
        super().__init__()
        self.log_list = log_list

    def emit(self, record):
        # Record is a LogRecord object, whose attribute 'msg' contains the log message
        self.log_list.append(record.msg)


@router.get("/tree/{object_id}")
def read_purpose_tree_for_object(object_id: int, db: Session = Depends(get_db)):
    result = db.query(DataObject).filter(DataObject.id == object_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Data object not found")

    purpose_tree = []
    for purpose_link in result.purposes:
        purpose_tree.append(generate_purpose_tree(purpose_link.purpose, db))

    return {"object_id": object_id, "purpose_tree": purpose_tree}


def generate_purpose_tree(purpose: PurposeModel, db: Session) -> Dict:
    """
    Formats the purpose tree retrieved from the database
    """
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


@router.get("/purposes/{purpose_id}")
def read_purpose(purpose_id: int, db: Session = Depends(get_db)):
    db_purpose = db.query(Purpose).filter(Purpose.id == purpose_id).first()
    if db_purpose is None:
        raise HTTPException(status_code=404, detail="Purpose not found")
    return db_purpose


@router.get("/purposes")
def read_purposes(db: Session = Depends(get_db)):
    purposes = db.query(Purpose).all()
    return purposes


@router.post("/purposes/{parent_id}/purposes", response_model=PurposeModel)
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

        
@router.get("/populate")
def populate(db: Session = Depends(get_db)):
    # Level 1
    all_purposes = Purpose(
        name="All purposes",
        transformations=[],
        parent_id=None
    )
    db.add(all_purposes)

    # Level 2
    marketing = Purpose(
        name="Marketing",
        transformations=["BLUR", "REMOVEBG"],
        parent_id=1
    )
    db.add(marketing)

    hr = Purpose(
        name="HR",
        transformations=[],
        parent_id=1
    )
    db.add(hr)

    sales = Purpose(
        name="Sales",
        transformations=["BLACKWHITE"],
        parent_id=1
    )
    db.add(sales)

    microsoft_365 = Purpose(
        name="Microsoft 365",
        transformations=["REMOVEBG"],
        parent_id=1
    )
    db.add(microsoft_365)

    # Level 3
    offline = Purpose(
        name="Offline",
        transformations=["BLACKWHITE"],
        parent_id=2
    )
    db.add(offline)

    online = Purpose(
        name="Online",
        transformations=["BLACKWHITE"],
        parent_id=2
    )
    db.add(online)

    print_advertising = Purpose(
        name="Print Advertising",
        transformations=["REMOVEBG"],
        parent_id=3
    )
    db.add(print_advertising)
