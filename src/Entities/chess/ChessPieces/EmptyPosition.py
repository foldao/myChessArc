
from typing import List
from src.Entities.chess.Board import Board
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position


class EmptyPosition(AbstractPiece):
    def __init__(self):
        self.color = PieceColorEnum.NONE
        self.name = "Empty"
        pass

    def get_possible_moves(self, board: Board, position: Position) -> List[Position]:
        return []
