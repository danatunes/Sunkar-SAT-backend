from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from app.schemas import User


class NotificationBase(BaseModel):
    user_id: Optional[int]
    message: Optional[str]
    url: Optional[str]


class NotificationCreate(NotificationBase):
    user_id: int
    message: str
    url: str


class NotificationUpdate(NotificationBase):
    is_viewed: Optional[bool]
    message: Optional[str]
    url: Optional[str]


class NotificationInDBBase(NotificationBase):
    id: Optional[int] = None
    is_viewed: bool
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


class Notification(NotificationInDBBase):
    pass


class NotificationInDB(NotificationInDBBase):
    pass
