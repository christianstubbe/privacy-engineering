"""
This class provides an interface for Casbin to use the custom,
provided model for our data structure.
"""
from casbin_databases_adapter import DatabasesAdapter
from databases import Database
from access.db import purposes
import os

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
db_url = f"postgresql://{username}:{password}@{url}"

adapter = DatabasesAdapter(Database(db_url), table=purposes)
