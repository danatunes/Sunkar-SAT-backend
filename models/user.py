from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255))
    password_hash = Column(Text)
    first_name = Column(String(255))
    last_name = Column(String(255))
    phone = Column(String(255))
    company = Column(String(255))
    is_active = Column(Boolean)
    is_verified = Column(Boolean)
    locale = Column(String(255))
    role = Column(String(255))
    photo_url = Column(Text)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    orders = relationship("Order", back_populates="user")
    notifications = relationship("Notification", back_populates="user")
