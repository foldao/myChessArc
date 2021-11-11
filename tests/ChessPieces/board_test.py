
from src.Entities.chess.BoardFactory import BoardFactory
from src.Entities.chess.ChessPieces.EmptyPosition import EmptyPosition
from src.Entities.chess.ChessPieces.King import King
from src.Entities.chess.ChessPieces.Rook import Rook
from src.Entities.chess.ChessPieces.Pawn import Pawn
from src.Entities.chess.ChessPieces.Queen import Queen
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position
import pytest


def test_board_check():
    board = BoardFactory.create_empty_board()
    board.state[Position(0, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(7, 0)] = Rook(PieceColorEnum.BLACK)
    assert bool(board.color_threating_opposing_king(
        PieceColorEnum.BLACK)) == True


def test_board_non_check():
    board = BoardFactory.create_default_board()
    assert bool(board.color_threating_opposing_king(
        PieceColorEnum.BLACK)) == False


def test_move():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
    board.move(Position(4, 0), Position(4, 1))
    assert isinstance(board.get_piece_by_position(Position(4, 1)), King)


def test_wong_turn_move():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.BLACK)
    with pytest.raises(Exception):
        board.move(Position(4, 0), Position(4, 1))
    assert isinstance(board.get_piece_by_position(
        Position(4, 1)), EmptyPosition)


def test_non_available_move():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(4, 1)] = Pawn(PieceColorEnum.WHITE)
    with pytest.raises(Exception):
        board.move(Position(4, 0), Position(4, 1))
    assert isinstance(board.get_piece_by_position(Position(4, 1)), Pawn)


def test_move_that_would_put_yourself_in_check():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(3, 2)] = Pawn(PieceColorEnum.BLACK)
    with pytest.raises(Exception):
        board.move(Position(4, 0), Position(4, 1))
    assert isinstance(board.get_piece_by_position(
        Position(4, 1)), EmptyPosition)
    assert isinstance(board.get_piece_by_position(Position(4, 0)), King)


def test_check():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(3, 2)] = Pawn(PieceColorEnum.BLACK)
    board.turn = 2
    board.move(Position(3, 2), Position(3, 1))
    assert board.check == PieceColorEnum.BLACK


def test_not_check_mate():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(3, 2)] = Pawn(PieceColorEnum.BLACK)
    board.turn = 2
    board.move(Position(3, 2), Position(3, 1))
    assert not board.is_checkmate()[0]


def test_check_mate():
    board = BoardFactory.create_empty_board()
    board.state[Position(0, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(1, 2)] = Queen(PieceColorEnum.BLACK)
    board.state[Position(5, 1)] = Rook(PieceColorEnum.BLACK)
    board.turn = 2
    board.move(Position(1, 2), Position(1, 1))
    assert board.is_checkmate()[0]
    assert board.check == PieceColorEnum.BLACK
    # assert isinstance(board.get_piece_by_position(Position(4,0)), King)
