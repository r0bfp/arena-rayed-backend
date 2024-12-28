from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException, Response
from typing import List

from src.errors.auth import UserNotFound
from src.errors.user import DuplicatedEmail, DuplicatedUsername
from src.schemas.user import UserOut, UserIn
from src.configs.database import get_db
from src.utils.auth import Auth
from src.usecases.user import UserUseCase


# router = APIRouter(prefix='/users', dependencies=[Depends(Auth.is_authenticated)])
router = APIRouter(prefix='/users')

@router.get('', response_model=List[UserOut])
def list(db: Session = Depends(get_db)):
    users = UserUseCase.list_users(db)

    return [UserOut.model_validate(user) for user in users]


@router.post('', response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create(request: UserIn, db: Session = Depends(get_db)):
    try: 
        return UserUseCase.create_user(db, request)
    except DuplicatedUsername:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username already exists')
    except DuplicatedEmail:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')


@router.get("/{id}", response_model=UserOut)
def find_one(id: int, db: Session = Depends(get_db)):
    try: 
        user = UserUseCase.get_a_user(db, id)

        return UserOut.model_validate(user)
    except UserNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


@router.put('/{id}', response_model=UserOut)
def update(request: UserIn, id: int, db: Session = Depends(get_db)):
    try:
        user = UserUseCase.update_user(db, request, id)

        return UserOut.model_validate(user)
    except UserNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    except DuplicatedUsername:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Username already exists')
    except DuplicatedEmail:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')



@router.delete('/{id}', response_model=UserOut)
def delete(id: int, db: Session = Depends(get_db)):
    try:
        UserUseCase.delete_user(db, id)

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except UserNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")



