from typing import Optional

from pydantic import BaseModel, EmailStr

from enum import Enum

from datetime import datetime


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"
    USER = "USER"


# Shared properties

class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[UserRole]
    phone: Optional[str]
    email: Optional[EmailStr]
    photo_url: Optional[str]


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    role: UserRole
    is_active: bool


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str]


class UserInDBBase(UserBase):
    id: Optional[int] = None

    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    password_hash: str
