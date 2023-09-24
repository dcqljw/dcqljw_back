from datetime import datetime

from sqlalchemy import Column, Integer, CHAR, DateTime, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    gid = Column(CHAR(36), nullable=False)
    group_name = Column(CHAR(16), nullable=False)
    group_tag = Column(CHAR(128), nullable=False)
    create_date = Column(DateTime, default=datetime.now())
    avatar = Column(VARCHAR(256))
    user_uuid = Column(CHAR(36), ForeignKey("users.uuid"), nullable=False)
