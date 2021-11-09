from __future__ import annotations
# pyright: reportUnknownParameterType=false, reportMissingParameterType=false
from abc import ABC, abstractmethod
from typing import List
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position


class AbstractPiece(ABC):
    color: PieceColorEnum
    name: str
    has_moved = False

    def __init__(self, color: PieceColorEnum, name: str) -> None:
        self.color = color
        self.name = name

    @abstractmethod
    def get_possible_moves(self, board, position: Position) -> List[Position]:

        raise NotImplementedError

    def get_color(self):
        return self.color

    def update_state(self,  board, position: Position):

        self.has_moved = True
