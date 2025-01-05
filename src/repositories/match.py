from sqlalchemy.orm import Session

from ..models.match import Match


class MatchRepository:
    @staticmethod
    def find_by_id(db: Session, id: int) -> bool:
        return db.query(Match).filter(Match.id == id).first()


    @staticmethod
    def find_by_id(db: Session, id: int) -> bool:
        return db.query(Match).filter(Match.id == id).first()


    @staticmethod
    def find_all_by_tournament_id(db: Session, tournament_id: int) -> Match:
        return db.query(Match).filter(Match.tournament_id == tournament_id).all()


    @staticmethod
    def create_or_update(db: Session, match: dict) -> Match:
        match = Match(**match)

        if match.id:
            db.merge(match)
        else:
            db.add(match)

        db.commit()

        return match