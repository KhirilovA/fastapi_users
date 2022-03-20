from datetime import date
from datetime import datetime


from pydantic import (
    BaseModel, 
    EmailStr
)


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PasswordUpdate(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str



