from src.Entities.chess.BoardFactory import BoardFactory
from src.Entities.chess.ChessPieces.King import King
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position


def test_valid_position():
    board = BoardFactory.create_empty_board()
    white_king = King(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_king)

    moves = white_king.get_possible_moves(board, Position(3, 3))
    assert Position(3, 4) in moves
    assert Position(4, 3) in moves
    assert Position(4, 4) not in moves
    assert len(moves) == 4
