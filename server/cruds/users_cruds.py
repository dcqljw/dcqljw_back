from sqlalchemy.orm import Session

from models import UserModels
from schemas import UserSchema
from utils import TokenUtils


def register(db: Session, user: UserSchema.RegisterUser):
    query_user = db.query(UserModels.User).filter(UserModels.User.username == user.username).first()
    if query_user:
        return False, "用户已存在"
    else:
        uuid = TokenUtils.create_uuid(user.username)
        password = TokenUtils.get_password_hash(user.password)
        models_user = UserModels.User(username=user.username, password=password, uuid=uuid, email=user.email)
        db.add(models_user)
        db.commit()
        db.refresh(models_user)
        return True, models_user


def get_user(db: Session, user: UserSchema.LoginUser):
    user = db.query(UserModels.User).filter(UserModels.User.username == user.username).first()
    if user:
        return user
    return None


def create_token(db: Session, user_uuid: str, token: str):
    query_token = db.query(UserModels.Token).filter(UserModels.Token.user_id == user_uuid).first()
    if query_token:
        query_token.token = token
        db.commit()
        return query_token
    else:
        models_token = UserModels.Token(user_id=user_uuid, token=token)
        db.add(models_token)
        db.commit()
        db.refresh(models_token)
        return models_token


def verify_user_token(db: Session, user_uuid: str, token: str):
    db_query = db.query(UserModels.User).join(UserModels.Token, UserModels.User.uuid == user_uuid).filter(
        UserModels.Token.token == token).first()
    if db_query is None:
        return False
    else:
        return True
