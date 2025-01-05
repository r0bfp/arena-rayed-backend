from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status

from ..errors.match import MatchNotFound

from ..errors.player import InvalidPlayerStatus, PlayerNotFound
from src.configs.database import get_db
from ..usecases.player import PlayerUseCase
from ..utils.auth import Auth


router = APIRouter(prefix='/players')
