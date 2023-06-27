from pydantic import BaseModel


class Index(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class IndexCreate(BaseModel):
    title: str
