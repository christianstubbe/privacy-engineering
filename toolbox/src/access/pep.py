import logging
from fastapi import Depends
from sqlalchemy.orm import joinedload, Session
from access.db import get_db, DataObjectPurpose, DataObject, Purpose


def get_pep(db: Session = Depends(get_db)):
    return PolicyEnforcementPoint(db)


logger = logging.getLogger(__name__)


class PolicyEnforcementPoint:
    def __init__(self, session: Session):
        self.session = session

    def get_permissions_for_purpose(self, data_object_id: int, purpose: str):
        # Get the purpose tree for the given data object
        purpose_tree = self.get_purpose_tree(data_object_id)

        if not purpose_tree:
            raise ValueError("Invalid data object ID")

        # Initialize list to hold all the transformations
        transformations = []

        # Traverse the purpose tree
        self.traverse_tree(purpose_tree, purpose, transformations)

        # Return all the transformations for the purpose
        return transformations

    def get_purpose_tree(self, data_object_id: int):
        # Load the data object with its purposes and related purpose data
        data_object = self.session.query(DataObject).options(
            joinedload(DataObject.purposes).joinedload(DataObjectPurpose.purpose)
        ).get(data_object_id)

        # Return the purposes as the tree
        return data_object.purposes if data_object else None
