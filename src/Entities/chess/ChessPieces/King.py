from typing import List
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.chess.Position import Position
import src.Entities.chess.Board as bd


class King(AbstractPiece):
    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: List[Position] = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for dir in directions:
            if evaluated_position := Position.try_to_create(*(
                    Position.tuple_sum(dir, position.as_tuple()))):
                match board.get_piece_by_position(evaluated_position):
                    case AbstractPiece(color=x):
                        if x != self.color:
                            movements.append(evaluated_position)
                    case None:
                        movements.append(evaluated_position)
        # TODO rock logic
        return movements
