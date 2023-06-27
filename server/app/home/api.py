from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import get_db
from cruds import home_crud
from schemas import schemas
from fastapi import Request
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/home')


@router.get("/")
def Index(db: Session = Depends(get_db)):
    index = home_crud.get_index(db)
    return index.title


@router.post("/create_title")
def Index(request: Request, index: schemas.IndexCreate, db: Session = Depends(get_db)):
    dcq = request.headers.get('dcq', None)
    if dcq != "5d9c9e023a33a510e7382393e7286d59":
        return JSONResponse(status_code=404, content={"msg": "error"})
    is_create = home_crud.create_index(db, index)
    if is_create:
        return {"msg": "ok"}
    else:
        return {"msg": "error"}
