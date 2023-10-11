from datetime import datetime

from pydantic import BaseModel


class GroupBase(BaseModel):
    group_name: str
    group_tag: str

    class Config:
        orm_mode = True


class GroupInfo(GroupBase):
    gid: str
    create_date = datetime
    avatar: str
    user_uuid: str
    desc: str


class CreateGroup(GroupBase):
    pass


class GroupFind(GroupBase):
    group_tag: str | None


class GroupData(BaseModel):
    code: str
    data: GroupInfo | None
    msg: str | None


class TodoBase(BaseModel):
    todo_title: str
    details: str | None
    status: bool
    todo_type: str

    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    group_id: str


class TodoInfo(TodoBase):
    todo_id: str
    user_id: str
    group_id: str
    create_date = datetime


class TodoOut(BaseModel):
    code: str
    result: TodoInfo | None
    msg: str | None


class UserJoinGroup(BaseModel):
    user_id: str
    group_id: str
