from typing import Dict, List
from src.Entities.chess.ChessPieces.Bishop import Bishop
from src.Entities.chess.ChessPieces.Horse import Horse
from src.Entities.chess.ChessPieces.King import King
from src.Entities.chess.ChessPieces.Pawn import Pawn
from src.Entities.chess.ChessPieces.Queen import Queen
from src.Entities.chess.ChessPieces.Rook import Rook
from src.Entities.chess.PieceColorEnum import PieceColorEnum
from src.Entities.chess.Position import Position
from src.Entities.chess.Board import Board
from src.Entities.chess.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.chess.ChessPieces.EmptyPosition import EmptyPosition


class BoardFactory:
    schema: Dict[str, List[str]]

    def _validate_board(self, schema: str | Dict[str, List[str]]):
        match schema:
            case str():
                self.schema = self._create_board_dict_from_string(schema)

            case dict():
                self.schema = schema
            case _:
                raise Exception("Board can only be created from dict or str")

    @staticmethod
    def create_empty_board() -> Board:
        state: Dict[Position, AbstractPiece] = {
            Position(i, j): EmptyPosition() for i in range(8) for j in range(8)}
        return Board(state)

    @staticmethod
    def create_default_board() -> Board:
        board = BoardFactory.create_empty_board()
        w = PieceColorEnum.WHITE
        b = PieceColorEnum.BLACK
        board.state[Position(0, 0)] = Rook(w)
        board.state[Position(7, 0)] = Rook(w)
        board.state[Position(0, 7)] = Rook(b)
        board.state[Position(7, 7)] = Rook(b)

        board.state[Position(1, 0)] = Horse(w)
        board.state[Position(6, 0)] = Horse(w)
        board.state[Position(1, 7)] = Horse(b)
        board.state[Position(6, 7)] = Horse(b)

        board.state[Position(2, 0)] = Bishop(w)
        board.state[Position(5, 0)] = Bishop(w)
        board.state[Position(2, 7)] = Bishop(b)
        board.state[Position(5, 7)] = Bishop(b)

        board.state[Position(3, 0)] = Queen(w)
        board.state[Position(3, 7)] = Queen(b)

        board.state[Position(4, 0)] = King(w)
        board.state[Position(4, 7)] = King(b)
        for i in range(8):
            board.state[Position(i, 1)] = Pawn(w)
            board.state[Position(i, 6)] = Pawn(b)

        return board

    def get_board(self, schema: str | Dict[str, List[str]]) -> Board:
        raise NotImplementedError

    def _create_board_dict_from_string(self, board_json: str) -> Dict[str, List[str]]:
        raise NotImplementedError
