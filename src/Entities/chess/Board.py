from dataclasses import dataclass
from typing import Dict, Optional


from src.Entities.chess.Position import Position
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece


@dataclass
class Board:
    state: Dict[Position, Optional[AbstractPiece]]
    king_positions: Dict[str, Position]

    def set_piece_by_indexes(self, x: int, y: int, piece: Optional[AbstractPiece]):
        self.state[Position(x, y)] = piece

    def get_piece_by_indexes(self, x: int, y: int):
        return self.state[Position(x, y)]

    def set_piece_by_position(self, position: Position, piece: Optional[AbstractPiece]):
        self.state[position] = piece

    def get_piece_by_position(self, position: Position):
        return self.state[position]
