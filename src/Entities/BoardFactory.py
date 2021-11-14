from src.Entities.ChessPieces.Bishop import Bishop
from src.Entities.ChessPieces.Horse import Horse
from src.Entities.ChessPieces.King import King
from src.Entities.ChessPieces.Pawn import Pawn
from src.Entities.ChessPieces.Queen import Queen
from src.Entities.ChessPieces.Rook import Rook
from src.Entities.PieceColorEnum import PieceColorEnum
from src.Entities.Position import Position
from src.Entities.Board import Board
from src.Entities.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.ChessPieces.EmptyPosition import EmptyPosition


class BoardFactory:
    schema: dict[str, list[str]]

    def _validate_board(self, schema: str | dict[str, list[str]]):
        pass
        # match schema:
        #     case str():
        #         self.schema = self._create_board_dict_from_string(schema)

        #     case dict():
        #         self.schema = schema
        #     case _:
        #         raise Exception("Board can only be created from dict or str")

    @staticmethod
    def create_empty_board() -> Board:
        state: dict[Position, AbstractPiece] = {
            Position(i, j): EmptyPosition() for i in range(8) for j in range(8)}
        return Board(state)

    @staticmethod
    def create_default_board() -> Board:
        board = BoardFactory.create_empty_board()
        black = PieceColorEnum.BLACK
        white = PieceColorEnum.WHITE
        board.state[Position(0, 0)] = Rook(black)
        board.state[Position(7, 0)] = Rook(black)
        board.state[Position(0, 7)] = Rook(white)
        board.state[Position(7, 7)] = Rook(white)

        board.state[Position(1, 0)] = Horse(black)
        board.state[Position(6, 0)] = Horse(black)
        board.state[Position(1, 7)] = Horse(white)
        board.state[Position(6, 7)] = Horse(white)

        board.state[Position(2, 0)] = Bishop(black)
        board.state[Position(5, 0)] = Bishop(black)
        board.state[Position(2, 7)] = Bishop(white)
        board.state[Position(5, 7)] = Bishop(white)

        board.state[Position(3, 0)] = Queen(black)
        board.state[Position(3, 7)] = Queen(white)

        board.state[Position(4, 0)] = King(black)
        board.state[Position(4, 7)] = King(white)
        for i in range(8):
            board.state[Position(i, 1)] = Pawn(black)
            board.state[Position(i, 6)] = Pawn(white)

        return board

    def board_to_json(self) -> None:
        raise NotImplementedError

    def _create_board_dict_from_string(self, board_json: str) -> dict[str, list[str]]:
        raise NotImplementedError
