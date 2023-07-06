"""
Module to populate the database on first use,
cleans up everything before inserting new objects
"""
import yaml
import logging
from jsonschema import validate, ValidationError
from adapters.db import collection
from pap import Purpose
from utils import constants

logger = logging.getLogger(__name__)


schema = {
    "appName": "string",
    "logoUrl": "string",
    "purposes": [
        {
            "purpose": "string",
            "parent_id": "string",
            "exceptions": ["string"],
            "transformations": ["string"]
        }
    ],
}


def validate_schema(stream):
    try:
        data = yaml.safe_load(stream)
        validate(instance=data, schema=schema)
        print("YAML file has the correct structure.")
    except yaml.YAMLError as exc:
        logger.error(exc)
    except ValidationError as ve:
        logger.error(f"YAML file has an incorrect structure: {ve}")
    return data


def populate_db():
    with open(constants.CONFIG_FILENAME, "r") as stream:
        data = validate_schema(stream)
        old = collection.count_documents()
        logger.info(f"Eleminating {old} objects present in the collection.")
        collection.delete_many()  # Removes every item

        if collection.count_documents > 0:
            logger.error("Documents could not be removed from the collection.")

        for purpose_yaml in data["purposes"]:
            purpose = Purpose(**purpose_yaml)
            collection.insert_one(purpose)

        new = collection.count_documents()
        logger.info(f"Added {new} new objects from the config file.")
