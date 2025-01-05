from sqlalchemy.orm import Session

from ..models.player import Player



class PlayerRepository:
    @staticmethod
    def find_by_match_id_and_user_id(db: Session, match_id: int, user_id: int) -> Player:
        return db.query(Player).filter(Player.match_id == match_id, Player.user_id == user_id).first()


    @staticmethod
    def find_opponent(db: Session, match_id: int, user_id: int) -> Player:
        return db.query(Player).filter(Player.match_id == match_id, Player.user_id != user_id).first()


    @staticmethod
    def find_by_id(db: Session, player_id: int) -> Player:
        return db.query(Player).filter(Player.id == player_id).first()


    @staticmethod
    def exists_by_id(db: Session, player_id: int) -> bool:
        return db.query(Player).filter(Player.id == player_id).first() is not None


    @staticmethod
    def create_or_update(db: Session, player: dict) -> Player:
        player = Player(**player)

        if player.id:
            db.merge(player)
        else:
            db.add(player)

        db.commit()

        return player