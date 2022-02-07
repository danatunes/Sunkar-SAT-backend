from sqlalchemy import Column, Integer, Boolean, String, Text, DateTime, func,ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer , primary_key=True,index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    is_viewed = Column(Boolean,default=False)
    message = Column(String(500))
    url = Column(Text)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User",back_populates="notifications")