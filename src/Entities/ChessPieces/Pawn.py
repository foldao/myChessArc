from typing import List
from src.Entities.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.ChessPieces.EmptyPosition import EmptyPosition
from src.Entities.PieceColorEnum import PieceColorEnum
from src.Entities.Position import Position
import src.Entities.Board as bd


class Pawn(AbstractPiece):

    turn_when_can_get_taken_en_passant: int = 0

    def __init__(self, color: PieceColorEnum) -> None:
        super().__init__(color, "Pawn")

    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: List[Position] = []

        if (front_position := Position.try_to_create(*(Position.tuple_sum(position.as_tuple(), (0, self.color.value))))):
            match board.get_piece_by_position(front_position):
                case EmptyPosition():
                    movements.append(front_position)
        for diag_dir in [(1,  self.color.value), (-1, self.color.value)]:
            if diag_position := Position.try_to_create(*(Position.tuple_sum(position.as_tuple(), diag_dir))):
                match board.get_piece_by_position(diag_position):
                    case EmptyPosition():
                        side_position = Position(
                            *(Position.tuple_sum(diag_position.as_tuple(), (0, -1*self.color.value))))
                        match piece := board.get_piece_by_position(side_position):
                            case Pawn(color=others_color):
                                if others_color != self.color and piece.turn_when_can_get_taken_en_passant and side_position.y in [4, 5]:
                                    movements.append(diag_position)
                    case AbstractPiece(color=others_color):
                        if others_color != self.color:
                            movements.append(diag_position)
        return movements

    def update_state(self, board: bd.Board, position: Position):
        if not self.has_moved:
            if position.y in [4, 5]:
                self.turn_when_can_get_taken_en_passant = board.turn+1
        self.has_moved = True
