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
    name = Column(String, unique=True)
    purposes = relationship("DataObjectPurpose", back_populates="data_object")


class Purpose(Base):
    __tablename__ = "purpose"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    parent_id = Column(Integer, ForeignKey('purpose.id'))
    parent = relationship("Purpose", remote_side=[id])
    transformations = Column(JSON)
    data_objects = relationship("DataObjectPurpose", back_populates="purpose")
    