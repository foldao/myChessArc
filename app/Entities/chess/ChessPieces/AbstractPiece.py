from abc import ABC, abstractmethod
from typing import List
from app.Entities.chess.PieceColorEnum import PieceColorEnum
from app.Entities.chess.Position import Position


class AbstractPiece(ABC):
    color: PieceColorEnum
    position: Position
    
    @abstractmethod
    def get_possible_moves(self, board)->List[Position]:
        raise NotImplementedError

