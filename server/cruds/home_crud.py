from sqlalchemy.orm import Session

from models import models
from schemas import schemas


def create_index(db: Session, index: schemas.IndexCreate):
    db_index = models.Index(title=index.title)
    db.add(db_index)
    db.commit()
    db.refresh(db_index)
    return db_index


def get_index(db: Session):
    return db.query(models.Index).order_by(-models.Index.id).first()
