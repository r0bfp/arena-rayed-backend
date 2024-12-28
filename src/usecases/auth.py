from datetime import timedelta
from sqlalchemy.orm import Session

from ..errors.auth import UserNotFound, WrongPassword
from ..utils.auth import Auth
from ..repositories.user import UserRepository
from ..schemas.token import Token


class AuthUseCase:
   @staticmethod
   def signin(db: Session, user_data: dict) -> Token:
        user = UserRepository.find_by_username(db, user_data.username)

        if not user:
            raise UserNotFound

        pass_is_correct = Auth.verify_password(user_data.password, user.password)

        if not pass_is_correct:
            raise WrongPassword

        token = Auth.create_token(data={'user_id': user.id}, expires_delta=timedelta(days=1))

        return token