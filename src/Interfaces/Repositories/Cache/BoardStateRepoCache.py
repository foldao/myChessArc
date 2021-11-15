
from src.Entities.Board import Board
from src.Interfaces.Repositories.Abstracts.BoardStateRepoABC import BoardStateRepoABC
from src.UseCases.BoardMoveUseCase import BoardMoveUseCase


class BoardStateRepoCache(BoardStateRepoABC):
    board: Board

    def get_board(self):
        if not hasattr(self, 'board'):
            self.board = BoardMoveUseCase.create_new_board()
        return self.board

    def update_board(self, board: Board) -> None:
        self.board = board
