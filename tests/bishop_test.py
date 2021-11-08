from app.Entities.chess.BoardFactory import BoardFactory
from app.Entities.chess.ChessPieces.Bishop import Bishop
from app.Entities.chess.PieceColorEnum import PieceColorEnum
from app.Entities.chess.Position import Position


def valid_position_test():
    board=BoardFactory.create_empty_board()
    board.set_position_by_indexes(3,3,Bishop(PieceColorEnum.WHITE,'Bishop'))
    moves = board.get_position_in_indexes(3,3).get_possible_moves(board,Position(3,3))
    assert Position(4,4) in moves
    assert Position(3,4 ) not in moves