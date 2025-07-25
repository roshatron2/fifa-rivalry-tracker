# Models package - Export all models for easy importing
from .player import Player, PlayerDetailedStats
from .match import MatchCreate, Match, MatchUpdate, HeadToHeadStats
from .tournament import TournamentCreate, Tournament, TournamentPlayerStats
from .auth import UserCreate, User, UserLogin, Token, TokenData, UserInDB
from pydantic import BaseModel
from typing import Generic, TypeVar, List

# Generic type for paginated responses
T = TypeVar('T')

class PaginatedResponse(BaseModel, Generic[T]):
    """Generic pagination response model"""
    items: List[T]
    total: int
    page: int
    page_size: int
    total_pages: int
    has_next: bool
    has_previous: bool

__all__ = [
    # Player models
    "Player", 
    "PlayerDetailedStats",
    
    # Match models
    "MatchCreate",
    "Match",
    "MatchUpdate",
    "HeadToHeadStats",
    
    # Tournament models
    "TournamentCreate",
    "Tournament",
    "TournamentPlayerStats",
    
    # Auth models
    "UserCreate",
    "User",
    "UserLogin",
    "Token",
    "TokenData",
    "UserInDB",
    
    # Pagination models
    "PaginatedResponse",
]
