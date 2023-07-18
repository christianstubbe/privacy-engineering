""" This package for querying and uploading data to different cloud data storage solutions. """
import os

from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, Session

from contextlib import contextmanager

# TODO: from .tables import *

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
connection_str = f"postgresql://{username}:{password}@{url}/{db_name}"
engine = create_engine(connection_str, echo=True)
database = Database(connection_str)


@contextmanager
def get_db():
    """Provide a transactional scope around a series of operations."""
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


meta = MetaData()

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class DataObjectPurpose(Base):
    __tablename__ = "data_object_purpose"

    id = Column(Integer, primary_key=True, index=True)
    data_object_id = Column(Integer, ForeignKey('data_object.id'))
    purpose_id = Column(Integer, ForeignKey('purpose.id'))
    active = Column(Boolean)

    purpose = relationship("Purpose", back_populates="data_objects")
    data_object = relationship("DataObject", back_populates="purposes")


class DataObject(Base):
    __tablename__ = "data_object"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)  # TODO: filename
    purposes = relationship("DataObjectPurpose", back_populates="data_object")


class Purpose(Base):
    __tablename__ = "purpose"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    parent_id = Column(Integer, ForeignKey('purpose.id'))
    parent = relationship("Purpose", remote_side=[id])
    transformations = Column(JSON)
    data_objects = relationship("DataObjectPurpose", back_populates="purpose")
    
    
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
