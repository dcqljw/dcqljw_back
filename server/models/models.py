from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship

from database import Base


class Index(Base):
    __tablename__ = "Index"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256))


class SpiderTime(Base):
    __tablename__ = 'spider_time'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time = Column(DateTime)
    spider_type = Column(String(256))
    spider_data_key = Column(String(256), ForeignKey('spider_data.spider_id'))
    spider_data = relationship("SpiderData", back_populates="spider_time")


class SpiderData(Base):
    __tablename__ = 'spider_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    spider_id = Column(String(256))
    spider_type = Column(String(256), nullable=False)
    note = Column(String(256))
    crawl_time = Column(DateTime)
    source_data = Column(Text)
    spider_time = relationship("SpiderTime", back_populates="spider_data")
