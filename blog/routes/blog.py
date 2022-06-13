from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas import Blog, ShowBlog, User
from ..database import get_db
from ..functions import blog
from .. import oauth2

router = APIRouter(
    prefix='/blog',
    tags=['blogs'],
)

# User = Depends(oauth2.get_current_user)を追加することでエンドポイントに認証設定可能となる
@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user)

# User = Depends(oauth2.get_current_user)を追加することでエンドポイントに認証設定可能となる
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[ShowBlog])
def all_fetch(db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
    return blog.get_all(db, current_user)

# TODO ユーザ認証未対応
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    return blog.get(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    return blog.delete(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: Blog, db: Session = Depends(get_db)):
    return blog.update(id, request, db)
