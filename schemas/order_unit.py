from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from geojson_pydantic import Polygon


class OrderUnitBase(BaseModel):
    order_id: Optional[int]
    price_id: Optional[int]
    acquisition_mode: Optional[str]
    priority: Optional[str]
    is_express: Optional[bool]
    cloud_coverage_start: Optional[int]
    cloud_coverage_end: Optional[int]
    geom_raw: Optional[Polygon]
    price: Optional[str]
    currency: Optional[str]
    periods: Optional[Polygon]
    satellite: Optional[str]
    wish: Optional[str]
    application_theme: Optional[str]
    coverage: Optional[int]
    is_archive: Optional[bool]
    status: Optional[str]
    nadir: Optional[bool]


class OrderUnitCreate(OrderUnitBase):
    satellite: str
    acquisition_mode: str
    priority: str
    is_express: bool
    cloud_coverage_start: int
    cloud_coverage_end: int
    geom_raw: Polygon
    periods: Polygon
    wish: str
    coverage: int
    is_archive: bool
    status: str
    nadir: bool
    application_theme: str
    currency: str
    price: str


class OrderUnitUpdate(OrderUnitBase):
    satellite: Optional[str]
    acquisition_mode: Optional[str]
    priority: Optional[str]
    is_express: Optional[bool]
    cloud_coverage_start: Optional[int]
    cloud_coverage_end: Optional[int]
    geom_raw: Optional[Polygon]
    periods: Optional[Polygon]
    wish: Optional[str]
    coverage: Optional[int]
    is_archive: Optional[bool]
    status: Optional[str]
    nadir: Optional[bool]
    application_theme: Optional[str]
    currency: Optional[str]
    price: Optional[str]


class OrderUnitInDBBase(OrderUnitBase):
    id: Optional[int] = None

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class OrderUnit(OrderUnitInDBBase):
    pass


class OrderUnitInDB(OrderUnitInDBBase):
    pass
