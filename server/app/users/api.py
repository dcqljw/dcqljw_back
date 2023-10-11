from datetime import timedelta, datetime
from typing import Union

from fastapi import Depends, APIRouter, Response
from sqlalchemy.orm import Session

from app import get_db
from schemas import UserSchema
from cruds import users_cruds
from utils import TokenUtils

router = APIRouter(prefix='/user')


@router.post("/login", response_model=UserSchema.UserResponse)
def login(user: UserSchema.LoginUser, db: Session = Depends(get_db)):
    userinfo = users_cruds.get_user(db, user)
    if userinfo is not None:
        is_pas = TokenUtils.verify_password(user.password, userinfo.password)
        if is_pas:
            token = TokenUtils.create_token({
                "username": userinfo.username,
                "uuid": userinfo.uuid,
                "time": str(datetime.now() + timedelta(days=1))
            })
            users_cruds.create_token(db, userinfo.uuid, token)
            return {
                "code": "2000",
                "userInfo": userinfo,
                "msg": "登录成功",
                "token": token
            }
    return {
        "code": "2001",
        "msg": "用户名或密码错误"
    }


@router.post("/register")
def register(user: UserSchema.RegisterUser, db: Session = Depends(get_db)):
    state, userinfo = users_cruds.register(db, user)
    if not state:
        return {
            "code": "2001",
            "msg": userinfo
        }
    else:
        return {
            "code": "2000",
            "msg": "注册成功",
            "info": {
                "uuid": userinfo.uuid,
                "username": userinfo.username,
                "email": userinfo.email,
            }
        }
