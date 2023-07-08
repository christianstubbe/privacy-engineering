"""
This class provides an interface for Casbin to use the custom,
provided model for our data structure.
"""
from casbin_sqlalchemy_adapter import Adapter
from sqlalchemy import create_engine
import os

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
connection_string = f"postgresql://{username}:{password}@{url}/{db_name}"
engine = create_engine(connection_string, echo=True)

adapter = Adapter(engine)
