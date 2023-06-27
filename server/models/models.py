from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from database import Base


class Index(Base):
    __tablename__ = "Index"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256))
