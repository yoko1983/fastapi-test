from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from .schemas import TokenData
from sqlalchemy.orm import Session
from .database import get_db
from .functions.user import get

# openssl rand -hex 32 で生成
SECRET_KEY = "2e44eac947fe1f06b26d2553d6d5a437aa3cffa1dcce59ab893955b042c7cc68"
ALGORITHM = "HS256"
# 有効期限(分)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta]=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt

def verify_token(token:str, credentials_exception, db:Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        id: int = payload.get("id")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)

    except JWTError:
        raise credentials_exception

    user = get(id, db)
    return user
