from datetime import datetime

from pydantic import BaseModel


class GroupBase(BaseModel):
    group_name: str
    group_tag: str


class GroupInfo(GroupBase):
    gid: str
    create_date = datetime
    avatar: str
    user_uuid: str


class CreateGroup(GroupBase):
    pass


class GroupFind(GroupBase):
    group_tag: str | None
