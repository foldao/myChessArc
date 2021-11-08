from typing import Dict, List, Tuple, Union
from src.Entities.chess.Position import Position
from src.Entities.chess.Board import Board
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece


class BoardFactory:
    schema: Dict[str, List[str]]

    def _validate_board(self, schema: str | Dict[str, List[str]]) -> Dict[str, List[str]]:
        match schema:
            case str():
                self.schema = self._create_board_dict_from_string(schema)

            case dict():
                self.schema = schema
            case _:
                raise Exception("Board can only be created from dict or str")

    @staticmethod
    def create_empty_board() -> Board:
        state = {Position(i, j): None for i in range(8) for j in range(8)}
        return Board(state)

    def get_board(self, schema: str | Dict[str, List[str]]) -> Board:
        pass

    def _create_board_dict_from_string(self, board_json: str) -> Dict[str, List[str]]:
        pass
