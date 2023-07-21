import os

from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
url = os.getenv("DB_URL")
db_name = os.getenv("DB_NAME")
connection_str = f"postgresql://{username}:{password}@{url}/{db_name}"
engine = create_engine(connection_str, echo=True)
database = Database(connection_str)

meta = MetaData()

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
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
    name = Column(String, unique=True)
    purposes = relationship("DataObjectPurpose", back_populates="data_object")


class Transformation(Base):
    __tablename__ = "transformation"

    id = Column(Integer, primary_key=True, index=True)
    purpose_id = Column(Integer, ForeignKey('purpose.id'))
    purpose = relationship("Purpose", back_populates="transformation")
    blackwhite = Column(Boolean)
    removebg = Column(Boolean)
    blur = Column(Boolean)
    downsize = Column(Boolean)
    erosion = Column(Boolean)
    redact_email = Column(Boolean)


class Purpose(Base):
    __tablename__ = "purpose"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    parent_id = Column(Integer, ForeignKey('purpose.id'))
    parent = relationship("Purpose", remote_side=[id])
    data_objects = relationship("DataObjectPurpose", back_populates="purpose")
    transformation = relationship("Transformation", back_populates="purpose", uselist=False)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise
    finally:
        db.close()
