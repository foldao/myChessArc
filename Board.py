from dataclasses import dataclass
from typing import Dict


from app.Entities.chess.Position import Position
from app.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece


@dataclass
class Board:
    state: Dict[Position, AbstractPiece]

    
    def set_position_by_indexes(self,x:int,y:int, piece:AbstractPiece):
        self.state[Position(x,y)]=piece
        
    def get_position_in_indexes(self,x:int,y:int):
        return self.state[Position(x,y)]
    
