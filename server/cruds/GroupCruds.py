from sqlalchemy.orm import Session
from sqlalchemy import and_
from models import GroupModels
from schemas import GroupSchema


def get_group(db: Session, gid: str):
    return db.query(GroupModels.Group).filter(GroupModels.Group.gid == gid).first()


def get_group_name(db: Session, group_name: str):
    return db.query(GroupModels.Group).filter(GroupModels.Group.group_name == group_name).first()


def create_group(db: Session, group: GroupSchema.GroupInfo):
    models_group = GroupModels.Group(**group.dict())
    db.add(models_group)
    db.commit()
    db.refresh(models_group)
    return models_group


def user_join_group(db: Session, join_data: GroupSchema.UserJoinGroup):
    try:
        users = GroupModels.GroupUsers(**join_data.dict())
        db.add(users)
        db.commit()
        db.refresh(users)
        return True
    except Exception as e:
        print(e)
        return False


def user_in_group(db: Session, user_id: str, group_id: str):
    first = db.query(GroupModels.GroupUsers).filter(and_(
        GroupModels.GroupUsers.user_id == user_id, GroupModels.GroupUsers.group_id == group_id
    )).first()
    if first:
        return True
    return False


def create_todo(db: Session, todo: GroupSchema.TodoInfo):
    try:
        todos = GroupModels.Todos(**todo.dict())
        db.add(todos)
        db.commit()
        db.refresh(todos)
        return todos
    except Exception:
        return False


def get_todo(db: Session, todo_type: str, user_id: str, group_id: str):
    todos = db.query(GroupModels.Todos).filter(
        and_(
            GroupModels.Todos.todo_type == todo_type, GroupModels.Todos.user_id == user_id,
            GroupModels.Todos.group_id == group_id
        )).all()
    return todos
