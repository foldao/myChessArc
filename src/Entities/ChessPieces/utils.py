from src.Entities.Board import Board
from src.Entities.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.ChessPieces.EmptyPosition import EmptyPosition
from src.Entities.Position import Position


def get_possible_moves_of_line_attack(board: Board, position: Position, piece: AbstractPiece, directions: list[tuple[int, int]]):
    movements: list[Position] = []
    pos_tuple = position.as_tuple()
    for dir in directions:
        next_on_dir = Position.tuple_sum(pos_tuple, dir)
        should_continue = True
        while(should_continue):
            should_continue = False
            if Position.is_valid(*next_on_dir):
                pos = Position(*next_on_dir)
                match board.get_piece_by_position(pos):
                    case  EmptyPosition():
                        movements.append(pos)
                        next_on_dir = Position.tuple_sum(next_on_dir, dir)
                        should_continue = True
                    case AbstractPiece(color=x):
                        if x != piece.get_color():
                            movements.append(pos)
                        should_continue = False

    return movements
