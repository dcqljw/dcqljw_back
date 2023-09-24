from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserInfo(UserBase):
    uuid: str
    email: EmailStr
    create_date: datetime | None
    avatar: str | None


class UserResponse(BaseModel):
    code: str
    userInfo: UserInfo | None
    msg: str | None
    token: str | None


class LoginUser(UserBase):
    password: str


class RegisterUser(UserBase):
    email: EmailStr
    password: str
