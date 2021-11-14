from abc import ABC, abstractmethod
from src.Entities.Board import Board


class BoardStateRepoABC(ABC):
    id: int

    @abstractmethod
    def get_board(self) -> Board:
        raise NotImplementedError

    @abstractmethod
    def update_board(self, board: Board) -> None:
        raise NotImplementedError

    @abstractmethod
    def create_board(self) -> tuple[Board, int]:
        raise NotImplementedError
