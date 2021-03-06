from src.Entities.BoardFactory import BoardFactory
from src.Entities.ChessPieces.Horse import Horse
from src.Entities.PieceColorEnum import PieceColorEnum
from src.Entities.Position import Position


def test_valid_position():
    board = BoardFactory.create_empty_board()
    white_horse = Horse(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(7, 0, white_horse)
    moves = white_horse.get_possible_moves(board, Position(7, 0))
    assert Position(5, 1) in moves
    assert Position(6, 2) in moves
    assert len(moves) == 2


def test_invalid_position():
    board = BoardFactory.create_empty_board()
    white_horse = Horse(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_horse)
    moves = white_horse.get_possible_moves(board, Position(3, 3))

    assert Position(3, 4) not in moves


def test_valid_piece_takedown():
    board = BoardFactory.create_empty_board()
    white_horse = Horse(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_horse)
    board.set_piece_by_indexes(5, 4, Horse(PieceColorEnum.BLACK))
    moves = white_horse.get_possible_moves(board, Position(3, 3))
    assert Position(5, 4) in moves


def test_invalid_piece_takedown():
    board = BoardFactory.create_empty_board()
    white_horse = Horse(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_horse)
    board.set_piece_by_indexes(5, 4, Horse(PieceColorEnum.WHITE))
    moves = white_horse.get_possible_moves(board, Position(3, 3))
    assert Position(5, 4) not in moves
