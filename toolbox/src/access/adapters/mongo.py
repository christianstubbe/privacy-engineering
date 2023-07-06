"""
This class provides an interface for Casbin to use the custom,
provided model for our data structure.
"""
import casbin_pymongo_adapter
import constants


# TODO: are policies saved diffirently depending on
class PyMongoAdapter(casbin_pymongo_adapter.Adapter):
    def __init__(self, db_url: str, db: str):
        self.db = db

    def load_policy(self, model):
        # Implement logic here to load policy rules from your PyMongo database into the provided model.
        pass

    def save_policy(self, model):
        # Implement logic here to save policy rules from the provided model into your PyMongo database.
        # TODO: add call from PAP module
        pass


adapter = PyMongoAdapter(constants.MONGODB_URL, constants.COLLECTION_NAME)
