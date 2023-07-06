from pymongo import MongoClient
from schema import validate_schema
from access.pap import Purpose
import constants
import logging

client = MongoClient(constants.MONGODB_URL)
db = client[constants.DB_NAME]
collection = db[constants.COLLECTION_NAME]


logger = logging.getLogger(__name__)


def populate_db():
    with open(constants.CONFIG_FILENAME, "r") as stream:
        data = validate_schema(stream)
        result = collection.delete_many({})  # Removes every item
        logger.info(f"Eleminated {result.deleted_count} objects present in the collection.")

        for purpose_yaml in data["purposes"]:
            purpose = Purpose(**purpose_yaml)
            collection.insert_one(purpose)

        new = collection.count_documents()
        logger.info(f"Added {new} new objects from the config file.")

# TODO: dump the current database to a file that can be downloaded
