from fastapi import APIRouter, status, Depends
from .. import schemas, database
from ..repository import blog as blogRepository
from ..oauth2 import get_current_user
from sqlalchemy.orm import Session
get_db = database.get_db

router = APIRouter(
    prefix = '/blog',
    tags=['Blogs']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[schemas.ShowBlog])
def all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.create(request, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.update(id, request, db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blogRepository.show(id, db)