""" This package for querying and uploading data to different cloud data storage solutions. """
import os
from sqlalchemy import create_engine, MetaData, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker, Session
from sqlalchemy_utils import UUIDType
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from databases import Database
import uuid

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
connection_str = f"postgresql://{username}:{password}@{url}/{db_name}"
engine = create_engine(connection_str, echo=True)
database = Database(connection_str)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session(engine)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


meta = MetaData()

Base = declarative_base()


class Purpose(Base):
    __tablename__ = "purpose"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    # Column("parent_id", Integer, ForeignKey('tree.id')),
    # relationship("parent", 'Tree', remote_side=[id])


class PurposeException(Base):
    __tablename__ = "purpose_exception"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    purpose_id = Column(Integer, ForeignKey('purpose.id'))
    exception_list = Column(String(100))


class Transformation(Base):
    __tablename__ = "transformation"
    id = Column(Integer, primary_key=True)
    name = Column(Integer, ForeignKey('purpose.id'), unique=True)
    transformation_list = Column("transformation_list", String(100))


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def populate():
    """
    Populate the database with basic information (purposes, exceptions, transformations, ...) provided by the config file
    """

    pass
