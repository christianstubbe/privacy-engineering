import yaml
import logging
from jsonschema import validate, ValidationError

logger = logging.getLogger(__name__)


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
}

with open("config.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        validate(instance=data, schema=schema)
        print("YAML file has the correct structure.")
    except yaml.YAMLError as exc:
        print(exc)
    except ValidationError as ve:
        print(f"YAML file has an incorrect structure: {ve}")
