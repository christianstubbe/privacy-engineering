""" This package for querying and uploading data to different cloud data storage solutions. """
import os
from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
engine = create_engine(f"postgresql://{username}:{password}@{url}/{db_name}")

metadata = MetaData()

Base = declarative_base()


purposes = Table(
    "purposes",
    MetaData(),
    Column("id", Integer, primary_key=True),
    Column("name", String(100), nullable=False),
    # Column("parent_id", Integer, ForeignKey('tree.id')),
    # relationship("parent", 'Tree', remote_side=[id])
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)