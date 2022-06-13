from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import Login, ShowUser
from ..functions import auth


router = APIRouter(
    tags=['Auth'],
)

#@router.post('/login')
#def login(request: Login, db: Session = Depends(get_db)):
#    return auth.login(request, db)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth.login(request, db)
