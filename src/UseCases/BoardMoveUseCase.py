from src.Entities.Board import Board
from src.Interfaces.Repositories.Abstracts.BoardStateRepoABC import BoardStateRepoABC
from dataclasses import dataclass
from src.Entities.PieceColorEnum import PieceColorEnum
from src.Entities.BoardFactory import BoardFactory
from src.Entities.Position import Position


@dataclass(slots=True)
class BoardMoveUseCase:
    board_repo: BoardStateRepoABC

    def move(self, from_tuple: tuple[int, int], to_tuple: tuple[int, int]):
        from_pos = Position(*from_tuple)
        to_pos = Position(*to_tuple)
        board = self.board_repo.get_board()
        board.move(from_pos, to_pos)
        self.board_repo.update_board(board)

    def get_possible_moves(self, pos: tuple[int, int]) -> list[tuple[int, int]]:
        board = self.board_repo.get_board()
        if position := Position.try_to_create(*pos):
            positions = board.get_all_possible_moves_from_piece_in_position(
                position)
            return [available_position.as_tuple() for available_position in positions]
        else:
            return []

    def get_state(self) -> tuple[dict[tuple[int, int], tuple[str, int]], PieceColorEnum, bool]:
        board = self.board_repo.get_board()
        return board.get_representation(), board.check, board.checkmate

    @staticmethod
    def create_new_board() -> Board:
        return BoardFactory.create_default_board()
