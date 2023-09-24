import datetime
from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from app import get_db
from cruds.users_cruds import verify_user_token
from utils import TokenUtils

router = APIRouter(prefix="/group")


def get_header_value(reqeust: Request, db: Session = Depends(get_db)):
    token = reqeust.headers.get("authorization", default=None)
    result_data = TokenUtils.verify_token(token)
    now_date = datetime.datetime.now()
    if result_data is None or token is None:
        raise HTTPException(status_code=400, detail="Not Authorization")
    elif result_data["time"] < str(now_date):
        raise HTTPException(status_code=400, detail="time out")
    if verify_user_token(db, user_uuid=result_data["uuid"], token=token):
        return result_data
    else:
        return False


@router.post("/create_group")
def create_group(token: str = Depends(get_header_value)):
    return token
