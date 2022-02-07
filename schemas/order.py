from typing import Optional

from pydantic import BaseModel, EmailStr

from enum import Enum

from datetime import datetime

from app.schemas import User


class OrderStage(str, Enum):
    PENDING_ASSESSMENT = "PENDING_ASSESSMENT"
    PENDING_PROPOSAL = "PENDING_PROPOSAL"
    PENDING_APPROVEMENT = "PENDING_APPROVEMENT"
    PENDING_IMAGING = "PENDING_IMAGING"
    PENDING_REVIEW_RESULTS = "PENDING_REVIEW_RESULTS"
    PENDING_PACKING = "PENDING_PACKING"
    DONE = "DONE"
    REJECTED = "REJECTED"


# Shared properties

class OrderBase(BaseModel):
    user_id: Optional[int]
    price: Optional[str]
    currency: Optional[str]
    coverage: Optional[int]
    download_url: Optional[str]


# Properties to receive via API on creation
class OrderCreate(OrderBase):
    user_id: int
    price: str
    currency: str
    coverage: int


# Properties to receive via API on update
class OrderUpdate(OrderBase):
    stage: Optional[OrderStage]


class OrderInDBBase(OrderBase):
    id: Optional[int] = None

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# Additional properties to return via API
class Order(OrderInDBBase):
    pass


# Additional properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
