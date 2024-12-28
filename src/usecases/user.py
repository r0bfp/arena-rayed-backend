
from sqlalchemy.orm import Session

from ..utils.auth import Auth
from ..errors.user import DuplicatedEmail, DuplicatedUsername
from ..errors.auth import UserNotFound
from ..schemas.user import UserIn
from ..models.user import User
from ..repositories.user import UserRepository


class UserUseCase:
    @staticmethod
    def delete_user(db: Session, id: int) -> None:
        if not UserRepository.exists_by_id(db, id):
            raise UserNotFound

        UserRepository.delete_by_id(db, id)


    @staticmethod
    def update_user(db: Session, new_user: UserIn, id: int) -> User:
        if not UserRepository.exists_by_id(db, id):
            raise UserNotFound

        if UserRepository.exists_by_username(db, new_user.username):
            raise DuplicatedUsername

        if UserRepository.exists_by_email(db, new_user.email):
            raise DuplicatedEmail

        return UserRepository.create_or_update(db, {**new_user.model_dump(), 'id': id})


    @staticmethod
    def get_a_user(db: Session, id: int) -> User:
        user = UserRepository.find_by_id(db, id)

        if not user:
            raise UserNotFound

        return user


    @staticmethod
    def create_user(db: Session, new_user: UserIn) -> User:
        if UserRepository.exists_by_username(db, new_user.username):
            raise DuplicatedUsername

        if UserRepository.exists_by_email(db, new_user.email):
            raise DuplicatedEmail

        new_user.password = Auth.get_password_hash(new_user.password)

        return UserRepository.create_or_update(db, new_user.model_dump())


    @staticmethod
    def list_users(db: Session) -> list[User]:
        return UserRepository.find_all(db)