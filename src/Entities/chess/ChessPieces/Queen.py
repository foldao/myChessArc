from typing import List
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.chess.ChessPieces.utils import get_possible_moves_of_line_attack

from src.Entities.chess.Position import Position
import src.Entities.chess.Board as bd


class Queen(AbstractPiece):
    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: List[Position] = []
        directions = [(1, 1), (-1, 1), (1, -1), (-1, -1),
                      (1, 0), (-1, 0), (0, -1), (0, 1)]
        movements += get_possible_moves_of_line_attack(
            board, position, self, directions)
        return movements
