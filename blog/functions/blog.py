from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, status
from ..schemas import Blog
from .. import models

def create(blog: Blog, db: Session, current_user):
    # JSON形式のデータからIDを取得
    user_id = [d for d in current_user]
    user_id = user_id[0].id
    new_blog = models.Blog(title=blog.title, body=blog.body, user_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {'create' : new_blog }

def get_all(db: Session, current_user):
    # JSON形式のデータからIDを取得
    user_id = [d for d in current_user]
    user_id = user_id[0].id
    blogs = db.query(models.Blog).filter(models.Blog.user_id == user_id).all()
    #blogs = db.query(models.Blog).all()
    return blogs

def get(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Blog with the id {id} is not available')
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail' : f'Blog with the id {id} is not available'}
        
    return blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Blog with the id {id} is not available')

    blog.delete(synchronize_session=False)
    db.commit()
    #HTTPレスポンス204の場合、bodyにはセットできない（HTTPの仕様）
    return Response(status_code=status.HTTP_204_NO_CONTENT)

def update(id: int, req_blog: Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Blog with the id {id} is not available')

    blog.update(req_blog.dict())
    #blog.update(req_blog)
    db.commit()
    db.refresh(blog.first())
    return {'update' : blog.first() }
