from __future__ import annotations
# pyright: reportUnknownParameterType=false, reportMissingParameterType=false
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from src.Entities.PieceColorEnum import PieceColorEnum
from src.Entities.Position import Position
if TYPE_CHECKING:
    from src.Entities.Board import Board


class AbstractPiece(ABC):
    color: PieceColorEnum
    name: str
    has_moved = False

    def __init__(self, color: PieceColorEnum) -> None:
        self.color = color

    @abstractmethod
    def get_possible_moves(self, board: Board, position: Position) -> list[Position]:

        raise NotImplementedError

    def get_color(self):
        return self.color

    def update_state(self,  board: Board, position: Position):

        self.has_moved = True
