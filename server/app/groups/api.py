import datetime
from typing import Dict

from fastapi import APIRouter, Depends, Request, HTTPException, UploadFile, Form
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from schemas import GroupSchema
from app import get_db
from cruds.users_cruds import verify_user_token
from cruds import GroupCruds
from utils import TokenUtils, MinioUtils, OtherUtils


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
        raise HTTPException(status_code=400, detail="error")


router = APIRouter(prefix="/group")


@router.get("/get_group", response_model=GroupSchema.GroupData)
def get_group(gid: str, db: Session = Depends(get_db)):
    group = GroupCruds.get_group(db, gid)
    if group is None:
        return {
            "code": "2001",
            "data": None,
            "msg": "查询失败"
        }
    return {
        "code": "2000",
        "data": group
    }


@router.post("/create_group")
def create_group(file: UploadFile,
                 group_name: str = Form(),
                 group_tag: str = Form(),
                 desc: str = Form(),
                 db: Session = Depends(get_db)):
    try:
        group = GroupCruds.get_group_name(db, group_name)
        if group:
            return {
                "code": "2001",
                "msg": "已存在"
            }
        file.filename = f"{OtherUtils.get_md5(group_name)}.{file.filename.split('.')[-1]}"
        url = MinioUtils.upload_file('static', file)
        gid = OtherUtils.get_md5(group_name)
        create_group_data = GroupSchema.GroupInfo(
            group_name=group_name,
            group_tag=group_tag,
            gid=gid,
            avatar=url,
            user_uuid="c3836ad4729b35a7bad649bd98ed7466",
            desc=desc
        )
        data = GroupCruds.create_group(db, create_group_data)
        if data:
            GroupCruds.user_in_group(db, user_id="c3836ad4729b35a7bad649bd98ed7466", group_id=gid)
            return {
                "code": "2000",
                "data": create_group_data
            }
        else:
            return {"code": "2001", "msg": "error"}
    except Exception as e:
        print(e)
        return {"code": "2001", "msg": "error"}


@router.post("/join_group")
def join_group(joinData: GroupSchema.UserJoinGroup, db: Session = Depends(get_db)):
    in_group = GroupCruds.user_in_group(db, joinData.user_id, joinData.group_id)
    if in_group:
        return {"msg": "不可重复加入"}
    group = GroupCruds.user_join_group(db, joinData)
    if group:
        return {"msg": "加入成功"}
    else:
        return {"msg": "加入失败"}


@router.get("/download")
async def download():
    response = StreamingResponse(MinioUtils.main(), media_type="application/octet-stream", headers={
        "Content-Disposition": "filename=test.txt"
    })
    return response


@router.post("/create_todo", response_model=GroupSchema.TodoOut)
def create_todo(todo: GroupSchema.TodoCreate, db: Session = Depends(get_db), token: Dict = Depends(get_header_value)):
    user_id = token['uuid']
    in_group = GroupCruds.user_in_group(db, user_id=user_id, group_id=todo.group_id)
    if not in_group:
        return {"code": "2001", "msg": "未加入该组，不可创建任务"}
    data = GroupSchema.TodoInfo(**todo.dict(),
                                todo_id=OtherUtils.get_md5(
                                    f"create_todo{todo.todo_title}{str(datetime.datetime.now())}"),
                                user_id=token['uuid'])
    create = GroupCruds.create_todo(db, data)
    if create:
        return {
            "code": "2000",
            "result": create,
        }
    else:
        return {"code": "2001", "msg": '创建失败'}


@router.get("/get_todos")
def get_todos(group_id: str, todo_type: str, db: Session = Depends(get_db), token: Dict = Depends(get_header_value)):
    user_id = token['uuid']
    todos = GroupCruds.get_todo(db, todo_type=todo_type, user_id=user_id, group_id=group_id)
    print(todos)
    return todos
