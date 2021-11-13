from src.Entities.BoardFactory import BoardFactory
from src.Entities.ChessPieces.Queen import Queen
from src.Entities.PieceColorEnum import PieceColorEnum
from src.Entities.Position import Position


def test_valid_position():
    board = BoardFactory.create_empty_board()
    white_Queen = Queen(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_Queen)
    moves = white_Queen.get_possible_moves(board, Position(3, 3))
    assert Position(3, 4) in moves
    assert Position(6, 3) in moves
    assert Position(4, 4) in moves
    assert Position(4, 5) not in moves
    assert len(moves) == 27


def test_valid_rock():
    pass
