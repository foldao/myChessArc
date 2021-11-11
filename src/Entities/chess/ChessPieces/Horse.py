from typing import List
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.chess.ChessPieces.EmptyPosition import EmptyPosition
from src.Entities.chess.Position import Position
from src.Entities.chess.PieceColorEnum import PieceColorEnum
import src.Entities.chess.Board as bd


class Horse(AbstractPiece):
    def __init__(self, color: PieceColorEnum) -> None:
        super().__init__(color, "Horse")

    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: List[Position] = []
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for dir in directions:
            if evaluated_position := Position.try_to_create(*(
                    Position.tuple_sum(dir, position.as_tuple()))):
                match board.get_piece_by_position(evaluated_position):
                    case EmptyPosition():
                        movements.append(evaluated_position)
                    case AbstractPiece(color=x):
                        if x != self.color:
                            movements.append(evaluated_position)
        return movements
