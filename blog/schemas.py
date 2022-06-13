from typing import List, Optional
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_tyoe: str

class TokenData(BaseModel):
    email: Optional[str] = None

class Login(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class BlogBase(BaseModel):
    class Config:
        orm_mode = True

class Blog(BlogBase):
    title: str
    body: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True