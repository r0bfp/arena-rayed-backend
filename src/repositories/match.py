from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from ..models.enums import MatchStatus

from ..models.player import Player

from ..models.match import Match


class MatchRepository:
    @staticmethod
    def find_by_id(db: Session, id: int) -> bool:
        return db.query(Match).filter(Match.id == id).first()


    @staticmethod
    def find_by_id(db: Session, id: int) -> bool:
        return db.query(Match).filter(Match.id == id).first()


    @staticmethod
    def find_all_by_tournament_id(db: Session, tournament_id: int) -> List[Match]:
        return db.query(Match).filter(Match.tournament_id == tournament_id).all()


    @staticmethod
    def find_all_from_last_round_by_tournament_id(db: Session, tournament_id: int) -> List[Match]:
        last_round = (
            db.query(func.max(Match.round_number))
            .filter(Match.tournament_id == tournament_id)
            .scalar()
        )
        
        return db.query(Match).filter(
            Match.tournament_id == tournament_id,
            Match.round_number == last_round
        ).all()
    

    @staticmethod
    def find_winners_by_round(db: Session, tournament_id: int, round_number: int):
        return db.query(Player).join(Match).filter(
            Match.tournament_id == tournament_id,
            Match.round_number == round_number,
            Match.status == MatchStatus.COMPLETED,
            Player.is_winner == True
        ).all()


    @staticmethod
    def create_or_update(db: Session, match: dict) -> Match:
        match = Match(**match)

        if match.id:
            db.merge(match)
        else:
            db.add(match)

        db.commit()

        return match