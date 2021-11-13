from src.Entities.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.ChessPieces.EmptyPosition import EmptyPosition
from src.Entities.Position import Position
from src.Entities.PieceColorEnum import PieceColorEnum
import src.Entities.Board as bd


class Horse(AbstractPiece):
    def __init__(self, color: PieceColorEnum) -> None:
        super().__init__(color, "Horse")

    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: list[Position] = []
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
