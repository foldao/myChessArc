from src.Entities.chess.BoardFactory import BoardFactory
from src.Entities.chess.ChessPieces.Bishop import Bishop
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position


def test_valid_far_position():
    board = BoardFactory.create_empty_board()
    white_bishop = Bishop(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(2, 4, white_bishop)
    moves = white_bishop.get_possible_moves(board, Position(2, 4))
    assert Position(5, 7) in moves

def test_valid_position():
    board = BoardFactory.create_empty_board()
    white_bishop = Bishop(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_bishop)
    moves = white_bishop.get_possible_moves(board, Position(3, 3))
    assert Position(4, 4) in moves


def test_invalid_position():
    board = BoardFactory.create_empty_board()
    white_bishop = Bishop(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_bishop)
    moves = white_bishop.get_possible_moves(board, Position(3, 3))

    assert Position(3, 4) not in moves


def test_valid_piece_takedown():
    board = BoardFactory.create_empty_board()
    white_bishop = Bishop(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_bishop)
    board.set_piece_by_indexes(4, 4, Bishop(PieceColorEnum.BLACK))
    moves = white_bishop.get_possible_moves(board, Position(3, 3))
    assert Position(4, 4) in moves


def test_invalid_piece_takedown():
    board = BoardFactory.create_empty_board()
    white_bishop = Bishop(PieceColorEnum.WHITE )
    board.set_piece_by_indexes(3, 3, white_bishop)
    board.set_piece_by_indexes(2, 2, Bishop(PieceColorEnum.WHITE ))
    moves = white_bishop.get_possible_moves(board, Position(3, 3))
    assert Position(2, 2) not in moves
