"""
Module to populate the database on first use,
cleans up everything before inserting new objects
"""
import yaml
import logging
from jsonschema import validate, ValidationError

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
