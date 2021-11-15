from abc import ABC, abstractmethod
from src.Entities.Board import Board


class BoardStateRepoABC(ABC):
    id: int

    @abstractmethod
    def get_board(self) -> Board:
        """Returns Board, creates new if necessary

        Returns:
            Board: Board Instance
        """
        raise NotImplementedError

    @abstractmethod
    def update_board(self, board: Board) -> None:
        """Updates stored board Instance

        Args:
            board (Board): new Board version
        """
        raise NotImplementedError
