from dataclasses import dataclass
from typing import Dict


from app.Entities.chess.Position import Position
from app.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece

@dataclass
class Board:
    state:Dict[Position, AbstractPiece]
    black_tower_left_has_moved:bool=False
    black_tower_right_has_moved:bool=False
    black_king_left_has_moved:bool=False
    white_king_left_has_moved:bool=False
    white_tower_right_has_moved:bool=False
    white_tower_left_has_moved:bool=False