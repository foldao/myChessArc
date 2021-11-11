from __future__ import annotations

from typing import List, TYPE_CHECKING
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.chess.ChessPieces.EmptyPosition import EmptyPosition
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position
if TYPE_CHECKING:
    import src.Entities.chess.Board as bd


class King(AbstractPiece):
    def __init__(self, color: PieceColorEnum) -> None:
        super().__init__(color, "King")

    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: List[Position] = []
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for dir in directions:
            if evaluated_position := Position.try_to_create(*(
                    Position.tuple_sum(dir, position.as_tuple()))):
                match board.get_piece_by_position(evaluated_position):
                    case EmptyPosition():
                        movements.append(evaluated_position)
                    case AbstractPiece(color=x):
                        if x != self.color:
                            movements.append(evaluated_position)
        if castle_position := self.can_castle(board, position):
            movements += castle_position
        return movements

    def can_castle(self, board: bd.Board, position: Position) -> List[Position]:
        response: List[Position] = []
        position_tuple = position.as_tuple()
        if not board.check and not self.has_moved and position.x == 4:
            for dir in [(-4, 0), (3, 0)]:
                if evaluated_position := Position.try_to_create(*(
                        Position.tuple_sum(dir, position_tuple))):
                    rook_position = board.get_piece_by_position(
                        evaluated_position)
                    if not rook_position.has_moved:
                        path_is_free = True
                        unit_of_direction = (int(dir[0]/abs(dir[0])), dir[1])
                        position_copy = Position.tuple_sum(
                            unit_of_direction, position_tuple)
                        while position_copy[0] not in [0, 7]:
                            if not isinstance(board.get_piece_by_indexes(*position_copy), EmptyPosition):
                                path_is_free = False
                            position_copy = Position.tuple_sum(
                                position_copy, unit_of_direction)
                        if path_is_free:
                            end_position = Position(
                                *(position_tuple[0]+(2*unit_of_direction[0]), position_tuple[1]))
                            simulation_board = board.copy_of_self()
                            self.execute_castle(
                                simulation_board, position, end_position)
                            if not simulation_board.color_threating_opposing_king(self.color):
                                response.append(end_position)
        return response

    def execute_castle(self, board: bd.Board, start_position: Position, end_position: Position):
        y = start_position.y
        rook_x = 0 if start_position.x > end_position.x else 7
        rook_position = Position(rook_x, y)
        rook_piece = board.state[rook_position]
        king_end_x = 2 if rook_x == 0 else 6
        rook_end_x = 3 if rook_x == 0 else 5
        rook_end_position = Position(rook_end_x, y)
        king_end_position = Position(king_end_x, y)
        self.has_moved = True
        rook_piece.has_moved = True
        board.set_piece_by_position(king_end_position, self)
        board.set_piece_by_position(rook_end_position, rook_piece)
        board.set_piece_by_position(rook_position, EmptyPosition())
        board.set_piece_by_position(start_position, rook_piece)

    def update_state(self,  board: bd.Board, position: Position):
        if not self.has_moved and position.x not in [3, 4, 5]:
            self.execute_castle(board, Position(4, position.y), position)

        self.has_moved = True
