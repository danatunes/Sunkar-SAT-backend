from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    price = Column(Numeric(15, 2))
    currency = Column(String(255))
    coverage = Column(Integer)
    stage = Column(String(255))
    download_url = Column(Text)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="orders")
    order_units = relationship("OrderUnit", back_populates="order")
