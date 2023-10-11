from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import get_db
from cruds import home_crud

from schemas import schemas
from fastapi import Request
from fastapi.responses import JSONResponse
from utils.spiders import baiduSpider

router = APIRouter(prefix='/home')


@router.get("")
def Index(db: Session = Depends(get_db)):
    index = home_crud.get_index(db)
    return index


@router.post("/create_title")
async def Index(request: Request, index: schemas.IndexCreate, db: Session = Depends(get_db)):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=404, content={"msg": "error"})
    is_create = home_crud.create_index(db, index)
    if is_create:
        return {"msg": "ok"}
    else:
        return {"msg": "error"}


@router.get("/hot_top_v1", response_model=schemas.OutSpiderDataV1)
def get_hot_top(spider_type: str, db: Session = Depends(get_db)):
    hot_top = home_crud.get_hot_top_v1(db, spider_type)
    if hot_top:
        data = {
            "code": "2000",
            "data": hot_top,
            "msg": "success"
        }
        return data
    else:
        data = {
            "code": "2001",
            "data": [],
            "msg": "no data"
        }
        return data


@router.get("/hot_top", response_model=schemas.OutSpiderData)
def get_hot_top(spider_type_list: str, db: Session = Depends(get_db)):
    spider_list = spider_type_list.split("_")
    hot_top = home_crud.get_hot_top(db, spider_list)
    return {
        "code": 2000,
        "data": hot_top,
        "msg": "success"
    }


@router.get("/start_spider")
def start_spider(request: Request, spider_type: str):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=401, content={"msg": "error"})
    else:
        if spider_type == "baidu":
            result = baiduSpider.run()
            if result['status']:
                return {"code": "200"}
            else:
                return {"msg": "error"}
        else:
            return {"code": "null"}
