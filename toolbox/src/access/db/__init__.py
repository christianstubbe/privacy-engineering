import json
import os
from contextlib import contextmanager

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
    description = Column(String)
    parent_id = Column(Integer, ForeignKey('purpose.id'))
    parent = relationship("Purpose", remote_side=[id])
    transformations = Column(JSON)
    data_objects = relationship("DataObjectPurpose", back_populates="purpose")


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


purposes = [
    Purpose(name="Marketing", description="Purpose related to strategizing and executing marketing initiatives.",
            transformations=json.dumps(["BLUR", "REMOVEBG"]), parent_id=None),
    Purpose(name="Offline",
            description="Tailored for traditional marketing channels that do not require internet access.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=1),
    Purpose(name="Print Advertising", description="Specifically aimed at marketing efforts through printed materials.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=2),
    Purpose(name="Outdoor Advertising",
            description="Perfect for organizing and managing billboard and other forms of outdoor promotions.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=2),
    Purpose(name="Event Marketing", description="Geared towards promoting and managing events for marketing purposes.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=2),
    Purpose(name="TV and Radio Advertising",
            description="Suited for advertising campaigns through television and radio channels.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=2),
    Purpose(name="Online", description="Purpose revolving around internet-based marketing tactics.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=1),
    Purpose(name="Social Media",
            description="Specifically for navigating the rapidly changing landscape of social media.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=7),
    Purpose(name="LinkedIn",
            description="Custom-built for exploiting LinkedIn's professional network for marketing opportunities.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=8),
    Purpose(name="Instagram",
            description="Designed for utilizing Instagram's visual-heavy platform for marketing strategies.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=8),
    Purpose(name="Facebook", description="Tailored for leveraging Facebook's vast user base for targeted marketing.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=8),
    Purpose(name="Website", description="Intended for improving and maintaining website for better online presence.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=7),
    Purpose(name="HR", description="Designed for all facets of managing human resources.",
            transformations=json.dumps([]), parent_id=None),
    Purpose(name="Recruitment",
            description="Geared towards the streamlined and effective process of recruiting talent.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=13),
    Purpose(name="Payroll Processing", description="Suited for the regular task of managing and executing payroll.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=13),
    Purpose(name="Training and Development",
            description="Tailored for the continuous process of enhancing employees' skills.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=13),
    Purpose(name="Performance Evaluation",
            description="Designed for the structured process of assessing employee performance.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=13),
    Purpose(name="Sales", description="Intended for all sales-related operations and strategies.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=None),
    Purpose(name="Customer Relationship Management Access",
            description="Custom-built for maintaining healthy customer relations and database access.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=18),
    Purpose(name="Sales Order Processing",
            description="Geared for efficiently processing orders to improve sales operations.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=18),
    Purpose(name="Sales Campaign Management", description="Tailored for running effective sales campaigns.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=18),
    Purpose(name="Sales Forecasting", description="Geared towards predicting and strategizing future sales.",
            transformations=json.dumps(["BLACKWHITE"]), parent_id=18),
    Purpose(name="Microsoft 365", description="Aimed at efficient utilization of Microsoft 365 for various tasks.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=None),
    Purpose(name="User Management", description="Designed for effective management of user roles and access rights.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=23),
    Purpose(name="Exchange Online Administration",
            description="Intended for administering and managing Exchange Online services.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=23),
    Purpose(name="SharePoint Online Administration",
            description="Geared towards effectively running SharePoint Online services.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=23),
    Purpose(name="Microsoft Teams Administration",
            description="Custom-built for managing and organizing Microsoft Teams services.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=23),
    Purpose(name="License Management",
            description="Created for the efficient handling of software licenses within the organization.",
            transformations=json.dumps(["REMOVEBG"]), parent_id=23),
]

