from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class PriceBase(BaseModel):
    satellite: Optional[str]
    acquisition_mode: Optional[str]
    source: Optional[str]
    processing_level: Optional[str]
    currency: Optional[str]
    price: Optional[str]


class PriceCreate(PriceBase):
    satellite: str
    acquisition_mode: str
    source: str
    processing_level: str
    currency: str
    price: str


class PriceUpdate(PriceBase):
    satellite: Optional[str]
    acquisition_mode: Optional[str]
    source: Optional[str]
    processing_level: Optional[str]
    currency: Optional[str]
    price: Optional[str]


class PriceInDBBase(PriceBase):
    id: Optional[int] = None

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Price(PriceInDBBase):
    pass


class PriceInDB(PriceInDBBase):
    pass
