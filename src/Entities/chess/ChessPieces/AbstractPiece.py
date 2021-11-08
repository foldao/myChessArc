from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List, Tuple
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position
if TYPE_CHECKING:
    from Entities.chess.Board import Board


class AbstractPiece(ABC):
    color: PieceColorEnum
    name: str
    has_moved = False

    def __init__(self, color: PieceColorEnum, name: str) -> None:
        self.color = color
        self.name = name

    @abstractmethod
    def get_possible_moves(self, board: Board, position: Position) -> List[Position]:
        raise NotImplementedError

    def get_color(self):
        return self.color

    def update_state(self, turn: int, position: Position):
        self.has_moved = True


def get_possible_moves_of_line_attack(board: Board, position: Position, piece: AbstractPiece, directions: List[Tuple[int, int]]):
    movements: List[Position] = []
    pos_tuple = position.as_tuple()
    for dir in directions:
        next_on_dir = Position.tuple_sum(pos_tuple, dir)
        should_continue = True
        while(should_continue):
            should_continue = False
            if Position.is_valid(*next_on_dir):
                pos = Position(*next_on_dir)
                match board.get_piece_by_position(pos):
                    case  None:
                        movements.append(pos)
                        next_on_dir = Position.tuple_sum(next_on_dir, dir)
                        should_continue = True
                    case AbstractPiece(color=x):
                        if x != piece.get_color():
                            movements.append(pos)
                        should_continue = False

    return movements
