import email
from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from ..schemas import Login
from .. import models, token
from ..hashing import Hash

def login(request: OAuth2PasswordRequestForm, db: Session):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()
    if not user:
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'User with the email {request.email} is not available')
    
    if not Hash.verify(request.password, user.password):
        raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Incorrect password')
    
    access_token = token.create_access_token(data={"sub": user.email, "id":user.id})
        
    return {"access_token": access_token, "token_type":"bearer"}
    