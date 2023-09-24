from datetime import datetime

from sqlalchemy import Column, Integer, CHAR, DateTime, VARCHAR, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    uuid = Column(CHAR(36), nullable=False)
    username = Column(CHAR(16), nullable=False)
    password = Column(CHAR(128), nullable=False)
    email = Column(CHAR(100))
    create_date = Column(DateTime, default=datetime.now())
    avatar = Column(VARCHAR(256))

    tokens = relationship("Token")


class Token(Base):
    __tablename__ = "tokens"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(CHAR(36), ForeignKey("users.uuid"), nullable=False)
    token = Column(VARCHAR(255))
    expires_date = Column(DateTime)
    create_date = Column(DateTime, default=datetime.now())
