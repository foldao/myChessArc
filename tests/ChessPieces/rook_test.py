from src.Entities.chess.BoardFactory import BoardFactory
from src.Entities.chess.ChessPieces.Rook import Rook
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position


def test_valid_position():
    board = BoardFactory.create_empty_board()
    white_Rook = Rook(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_Rook)
    moves = white_Rook.get_possible_moves(board, Position(3, 3))
    assert Position(3, 4) in moves
    assert Position(6, 3) in moves
    assert Position(4, 4) not in moves
    assert len(moves) == 14


def test_valid_rock():
    pass
