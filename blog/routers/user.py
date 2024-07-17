from fastapi import APIRouter, Depends, status
from .. import schemas, database
from ..repository import user as userRepository
from sqlalchemy.orm import Session
get_db = database.get_db

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id, db: Session = Depends(get_db)):
    return userRepository.show(id, db)