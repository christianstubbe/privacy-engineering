from pydantic import BaseModel
from typing import Optional


class PurposeModel(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = None
    transformations: str
    
    
class DataObjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    format: Optional[str] = None


class DataObjectCreate(DataObjectBase):
    pass


class DataObjectPurposeBase(BaseModel):
    purpose_id: int
    selected: bool


class DataObjectPurposeCreate(DataObjectPurposeBase):
    data_object_id: int

