
from src.Entities.Board import Board
from src.Interfaces.Repositories.Abstracts.BoardStateRepoABC import BoardStateRepoABC


class BoardStateRepoCache(BoardStateRepoABC):
    def get_board(self) -> Board:
        raise NotImplementedError

    def update_board(self, board: Board) -> None:
        raise NotImplementedError

    def create_board(self) -> tuple[Board, int]:
        raise NotImplementedError
