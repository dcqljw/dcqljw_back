from datetime import datetime
from typing import List

from pydantic import BaseModel


class Index(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class IndexCreate(BaseModel):
    title: str


class SpiderTimeSchema(BaseModel):
    id: int
    time: datetime
    spider_type: str
    spider_data_key: str

    class Config:
        orm_mode = True


class SpiderDataSchema(BaseModel):
    # id: int
    spider_id: str
    spider_type: str
    note: str
    crawl_time: datetime
    source_data: str

    class Config:
        orm_mode = True


class OutSpiderData(BaseModel):
    code: str
    data: List[SpiderDataSchema]
    msg: str
    speech: str = "hello world"
