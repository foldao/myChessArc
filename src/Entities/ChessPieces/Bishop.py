from src.Entities.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.ChessPieces.utils import get_possible_moves_of_line_attack

from src.Entities.Position import Position
from src.Entities.PieceColorEnum import PieceColorEnum
import src.Entities.Board as bd


class Bishop(AbstractPiece):
    def __init__(self, color: PieceColorEnum) -> None:
        super().__init__(color, "Bishop")

    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: list[Position] = []
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
        movements += get_possible_moves_of_line_attack(
            board, position, self, directions)
        return movements
