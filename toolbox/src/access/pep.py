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

    def traverse_tree(self, tree, purpose, transformations):
        for node in tree:
            if node.purpose.name == purpose and node.active:
                transformations.append(node.purpose.transformations)

            # Recurse into the parent purpose if it exists
            if node.purpose.parent:
                self.traverse_tree([node.purpose.parent], purpose, transformations)

    async def create_data(self):
        all_purposes = Purpose(
            purpose_id=1,
            name="All purposes",
            selected=False,
            transformations=[],
            parent_id=None
        )
        self.session.add(all_purposes)

        # Level 2
        marketing = Purpose(
            purpose_id=2,
            name="Marketing",
            selected=False,
            transformations=["BLUR", "REMOVEBG"],
            parent_id=1
        )
        self.session.add(marketing)

        hr = Purpose(
            purpose_id=11,
            name="HR",
            selected=False,
            transformations=[],
            parent_id=1
        )
        self.session.add(hr)

        sales = Purpose(
            purpose_id=16,
            name="Sales",
            selected=False,
            transformations=["BLACKWHITE"],
            parent_id=1
        )
        self.session.add(sales)

        microsoft_365 = Purpose(
            purpose_id=21,
            name="Microsoft 365",
            selected=False,
            transformations=["REMOVEBG"],
            parent_id=1
        )
        self.session.add(microsoft_365)

        # Level 3
        offline = Purpose(
            purpose_id=3,
            name="Offline",
            selected=False,
            transformations=["BLACKWHITE"],
            parent_id=2
        )
        self.session.add(offline)

        online = Purpose(
            purpose_id=8,
            name="Online",
            selected=False,
            transformations=["BLACKWHITE"],
            parent_id=2
        )
        self.session.add(online)

        print_advertising = Purpose(
            purpose_id=4,
            name="Print Advertising",
            selected=False,
            transformations=["REMOVEBG"],
            parent_id=3
        )
        self.session.add(print_advertising)
