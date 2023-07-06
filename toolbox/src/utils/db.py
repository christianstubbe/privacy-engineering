from pymongo import MongoClient
from utils import constants

client = MongoClient(constants.MONGODB_URL,
                     uuidRepresentation="standard")
db = client[constants.DB_NAME]
collection = db[constants.COLLECTION_NAME]
