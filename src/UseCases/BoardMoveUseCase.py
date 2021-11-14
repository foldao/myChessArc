from src.Interfaces.Repositories.Abstracts.BoardStateRepoABC import BoardStateRepoABC
from dataclasses import dataclass
from src.Entities.PieceColorEnum import PieceColorEnum

from src.Entities.Position import Position


@dataclass(slots=True)
class BoardMoveUseCase:
    board_repo: BoardStateRepoABC

    def move(self, from_tuple: tuple[int, int], to_tuple: tuple[int, int]) -> tuple[dict[tuple[int, int], tuple[str, int]], PieceColorEnum, bool]:
        from_pos = Position(*from_tuple)
        to_pos = Position(*to_tuple)
        board = self.board_repo.get_board()
        board.move(from_pos, to_pos)
        self.board_repo.update_board(board)
        return board.get_representation(), board.check, board.checkmate
