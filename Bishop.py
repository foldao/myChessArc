from typing import List
from Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from Entities.chess.PieceColorEnum import PieceColorEnum
from Entities.chess.Position import Position
import app.Entities.chess.Board as bd



class Bishop(AbstractPiece):
    def get_possible_moves(self, board: bd.Board, position: Position):
        movements: List[Position] = []
        pos_tuple=position.as_tuple()
        directions=[(1,1),(-1,1),(1,-1),(-1,-1)]
        for dir in directions:
            next_on_dir=pos_tuple+dir
            should_continue=True
            while(should_continue):
                should_continue=False
                if Position.is_valid(*next_on_dir):
                    pos=Position(*next_on_dir)
                    if isinstance(board[pos]):
                        movements.append(pos)
                        should_continue=False
                    if board[pos] is None:
                        movements.append(pos)
                        next_on_dir+=dir
                        should_continue=True
        return movements
