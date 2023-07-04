import casbin_pymongo_adapter


# TODO: are policies saved diffirently depending on
class PyMongoAdapter(casbin_pymongo_adapter.Adapter):
    def __init__(self, db_url: str, db: str):
        super()
        self.db = db

    def load_policy(self, model):
        super(model)
        # Implement logic here to load policy rules from your PyMongo database into the provided model.
        pass

    def save_policy(self, model):
        super(model)
        # Implement logic here to save policy rules from the provided model into your PyMongo database.
        # TODO: add call from PAP module
        pass


adapter = PyMongoAdapter("mongodb://localhost:27017/", "pbac_db")
