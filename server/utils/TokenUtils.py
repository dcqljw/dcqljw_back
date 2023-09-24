from jose import jwt, JWTError
from passlib.context import CryptContext
import Config
import uuid

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def verify_password(plain_password, hashed_password):
    try:
        if pwd_context.verify(plain_password, hashed_password):
            return True
    except:
        return False


def get_password_hash(password):
    return pwd_context.hash(password)


def create_uuid(username: str):
    return str(uuid.uuid3(uuid.NAMESPACE_DNS, username)).replace("-", "")


def create_token(data: dict):
    encode = jwt.encode(data, Config.SECRET_KEY, algorithm=Config.ALGORITHM)
    return encode


def verify_token(token: str):
    try:
        decode = jwt.decode(token, Config.SECRET_KEY)
        return decode
    except JWTError:
        return None


if __name__ == '__main__':
    print(create_uuid("dcq"))
    print(get_password_hash("dcq.159357"))
    print(verify_password("dcq.159357", "$21$EixZaYVK1fsbw1ZfbXePaWxn96p36WQoeG6Lruj3vjPGga31lW"))
    data = {
        "username": "dcq",
    }
    print(create_token(data))
    print(verify_token(create_token(data)))
    print(verify_token("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRjcSIsInRpbWUiOiIyMDIzLTA5LTIxIDE5OjUzOjEyLjc0OTcyNCJ9.AJn9YufKCEK12qaM20smZF54i3y-0orY89rQDb0VtVo"))
