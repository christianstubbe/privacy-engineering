from pymongo import MongoClient
import constants

# Create a client to the MongoDB instance
client = MongoClient(constants.COLLECTION_NAME)

# Connect to your database
db = client[constants.DB_NAME]

# Create your collections
collection1 = db[constants.COLLECTION_NAME]

# collection1.insert_many(document1, document2)
