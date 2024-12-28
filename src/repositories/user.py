from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()


    @staticmethod
    def exists_by_username(db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first() is not None


    @staticmethod
    def exists_by_email(db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first() is not None


    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.id == id).first() is not None


    @staticmethod
    def create_or_update(db: Session, user: dict) -> User:
        user = User(**user)

        if user.id:
            db.merge(user)
        else:
            db.add(user)

        db.commit()

        return user


    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def find_by_username(db: Session, username: str) -> User:
        return db.query(User).filter(User.username == username).first()


    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        user = db.query(User).filter(User.id == id).first()

        if user is not None:
            db.delete(user)
            db.commit()