from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..schemas import ShowUser, User
from ..database import get_db
from ..functions import user
from .. import oauth2

router = APIRouter(
    prefix='/user',
    tags=['users'],
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: User, db: Session = Depends(get_db)):
    return user.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=ShowUser)
def show(id: int, db: Session = Depends(get_db)):
    return user.get(id, db)
