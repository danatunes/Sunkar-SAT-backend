from sqlalchemy import Column, Integer, String, Text, DateTime, func, Numeric
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Price(Base):
    __tablename__ = "prices"
    id = Column(Integer, primary_key=True, index=True)
    satellite = Column(String)
    acquisition_mode = Column(Text)
    source = Column(String, nullable=False)
    processing_level = Column(String, nullable=False)
    currency = Column(String(255))
    price = Column(Numeric(15, 2))
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    order_units = relationship("OrderUnit", back_populates="price")
