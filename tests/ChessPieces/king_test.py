from src.Entities.chess.BoardFactory import BoardFactory
from src.Entities.chess.ChessPieces.King import King
from src.Entities.chess.ChessPieces.Rook import Rook
from src.Entities.chess.ChessPieces.Pawn import Pawn
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position
# import pytest

def test_valid_position():
    board = BoardFactory.create_empty_board()
    white_king = King(PieceColorEnum.WHITE)
    board.set_piece_by_indexes(3, 3, white_king)
    board.set_piece_by_position(Position(2,3),Pawn(PieceColorEnum.WHITE))
    board.set_piece_by_position(Position(2,2),Pawn(PieceColorEnum.BLACK))
    moves = white_king.get_possible_moves(board, Position(3, 3))
    assert Position(3, 4) in moves
    assert Position(4, 3) in moves
    assert Position(4, 5) not in moves
    assert len(moves) == 7
    
def test_castle_is_available():
    board = BoardFactory.create_empty_board()
    board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
    board.state[Position(7, 0)] = Rook(PieceColorEnum.WHITE)
    board.state[Position(0, 0)] = Rook(PieceColorEnum.WHITE)
    moves=board.state[Position(4, 0)].get_possible_moves(board,Position(4, 0))
    assert Position(2,0 ) in moves
    assert Position(6,0 ) in moves
    assert Position(7,0 ) not in moves
    
def test_castle_execution():
    board = BoardFactory.create_empty_board()
    king= King(PieceColorEnum.WHITE)
    rook1=Rook(PieceColorEnum.WHITE)
    rook2=Rook(PieceColorEnum.WHITE)
    board.state[Position(4, 0)] = king
    board.state[Position(7, 0)] = rook1
    board.state[Position(0, 0)] = rook2
    board.move(Position(4,0), Position(2,0))
    assert isinstance(board.get_piece_by_position(Position(2,0 )),King)
    assert isinstance(board.get_piece_by_position(Position(3,0 )),Rook)
    assert isinstance(board.get_piece_by_position(Position(7,0 )) ,Rook)
    
 
# def test_castle_is_available():
#     board = BoardFactory.create_empty_board()
#     board.state[Position(4, 0)] = King(PieceColorEnum.WHITE)
#     board.state[Position(7, 0)] = Rook(PieceColorEnum.WHITE)
#     board.state[Position(0, 0)] = Rook(PieceColorEnum.WHITE)
#     board.move()
