""" This package for querying and uploading data to different cloud data storage solutions. """
from pymongo import MongoClient
import constants

client = MongoClient(constants.MONGODB_URL,
                     uuidRepresentation="standard")
db = client[constants.DB_NAME]
collection = db[constants.COLLECTION_NAME]