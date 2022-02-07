from geoalchemy2 import Geometry
from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean, Numeric, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class OrderUnit(Base):
    __tablename__ = "order_units"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    price_id = Column(Integer, ForeignKey("prices.id"))
    acquisition_mode = Column(Text, nullable=False)
    address = Column(String)
    priority = Column(String)
    is_express = Column(Boolean)
    cloud_coverage_start = Column(Integer)
    cloud_coverage_end = Column(Integer)
    geom = Column(Geometry)
    geom_raw = Column(JSON)
    price = Column(Numeric(15, 2))
    currency = Column(String)
    periods = Column(JSON)
    satellite = Column(String)
    wish = Column(String(1000))
    application_theme = Column(String)
    coverage = Column(Integer)
    is_archive = Column(Boolean)
    status = Column(String, nullable=False)
    nadir = Column(Boolean)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    price = relationship("Price", back_populates="order_units")
    order = relationship("Order", back_populates="order_units")
