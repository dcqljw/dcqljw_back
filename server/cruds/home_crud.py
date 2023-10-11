from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session, defer
from models import models
from schemas import schemas


def create_index(db: Session, index: schemas.IndexCreate):
    db_index = models.Index(title=index.title)
    db.add(db_index)
    db.commit()
    db.refresh(db_index)
    return db_index


def get_index(db: Session):
    return db.query(models.Index).order_by(-models.Index.id).limit(4).all()


def get_hot_top_v1(db: Session, spider_type: str):
    spider_data_key = db.query(models.SpiderTime.spider_data_key).where(
        models.SpiderTime.spider_type == spider_type).order_by(
        desc(models.SpiderTime.time)).limit(1)
    if spider_data_key.first() is not None:
        result = db.query(models.SpiderData) \
            .filter(models.SpiderData.spider_type == spider_type,
                    models.SpiderData.spider_id == spider_data_key[0][0]).all()
        return result
    return None


def get_hot_top(db: Session, spider_type_list: List):
    result_dict = {}
    for spider_type in spider_type_list:
        spider_data_key = db.query(models.SpiderTime.spider_data_key).where(
            models.SpiderTime.spider_type == spider_type).order_by(
            desc(models.SpiderTime.time)).limit(1)
        if spider_data_key.first() is not None:
            result = db.query(models.SpiderData) \
                .filter(models.SpiderData.spider_type == spider_type,
                        models.SpiderData.spider_id == spider_data_key[0][0]).all()
            result_dict[spider_type] = result
        else:
            result_dict[spider_type] = None
    return result_dict
