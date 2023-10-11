from datetime import datetime

from sqlalchemy import Column, Integer, CHAR, DateTime, VARCHAR, ForeignKey, TEXT, BOOLEAN, DATETIME

from database import Base


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, autoincrement=True)
    gid = Column(CHAR(36), nullable=False)
    group_name = Column(CHAR(16), nullable=False)
    group_tag = Column(CHAR(128), nullable=False)
    create_date = Column(DATETIME, default=datetime.now())
    avatar = Column(VARCHAR(256))
    user_uuid = Column(CHAR(36), ForeignKey("users.uuid"), nullable=False)
    desc = Column(VARCHAR(256))


class GroupUsers(Base):
    __tablename__ = "group_users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(CHAR(36), ForeignKey("users.uuid"), nullable=False)
    group_id = Column(CHAR(36), ForeignKey("groups.gid"), nullable=False)
    join_date = Column(DATETIME, default=datetime.now())


class Todos(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    todo_id = Column(CHAR(32), nullable=False)
    todo_title = Column(CHAR(50), nullable=False)
    create_date = Column(DATETIME, default=datetime.now())
    details = Column(TEXT)
    status = Column(BOOLEAN, default=False)
    todo_type = Column(CHAR(10))
    user_id = Column(CHAR(36), ForeignKey("users.uuid"), nullable=False)
    group_id = Column(CHAR(36), ForeignKey("groups.gid"), nullable=False)
