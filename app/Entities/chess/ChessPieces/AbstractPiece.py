from abc import ABC, abstractmethod
from typing import List
from app.Entities.chess.PieceColorEnum import PieceColorEnum
from app.Entities.chess.Position import Position
import app.Entities.chess.Board as bd


class AbstractPiece(ABC):
    color: PieceColorEnum
    name: str
    has_moved=False
    def __init__(self, name: str, color: PieceColorEnum) -> None:
        self.color = color
        self.name = name

    @abstractmethod
    def get_possible_moves(self, board: bd.Board, position: Position) -> List[Position]:
        raise NotImplementedError
    
    def update_state(self, turn:int, position:Position):
        self.has_moved=True
        