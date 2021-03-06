from dataclasses import dataclass

import copy
from src.Entities.PieceColorEnum import PieceColorEnum

from src.Entities.Position import Position
from src.Entities.ChessPieces.AbstractPiece import AbstractPiece
from src.Entities.ChessPieces.King import King
from src.Entities.ChessPieces.EmptyPosition import EmptyPosition


@dataclass
class Board:
    state: dict[Position, AbstractPiece]
    turn: int = 1
    check: PieceColorEnum = PieceColorEnum.NONE
    checkmate: bool = False
    check_attacker_position: Position | None = None

    def copy_of_self(self) -> 'Board':
        return copy.deepcopy(self)

    def move(self, a: Position, b: Position):
        if self.checkmate:
            raise Exception(f'Game is Over: {self.check.value}S won!')
        piece_on_a = self.get_piece_by_position(a)
        if not self.validate_move_is_from_the_correct_player(piece_on_a):
            raise Exception("The turn belongs to the opponent!")
        if b not in piece_on_a.get_possible_moves(self, a):
            raise Exception("Invalid Move: This piece cannot make this move!")
        simulation_state = self.copy_of_self()
        simulation_state.set_piece_by_position(b, piece_on_a)
        simulation_state.set_piece_by_position(a, EmptyPosition())
        simulation_state.validate_move_and_check_condition()
        self.state = simulation_state.state

        self.update_state_of_check()
        if self.check:
            if self.is_check_a_checkmate():
                self.checkmate = True

    def get_representation(self) -> dict[tuple[int, int], tuple[str, int]]:
        response: dict[tuple[int, int], tuple[str, int]] = {}
        for position in self.state:
            piece = self.state[position]
            if not isinstance(piece, EmptyPosition):
                response[position.as_tuple()] = (
                    piece.name, piece.get_color().value)
        return response

    def is_check_a_checkmate(self) -> bool:
        color_in_check = self.check.get_opposing_color()
        moves = self.get_all_possible_moves_from_color(color_in_check)
        for piece_position in moves:
            for move in moves[piece_position]:
                simulation_state = self.copy_of_self()
                moved_piece = simulation_state.get_piece_by_position(
                    piece_position)
                simulation_state.set_piece_by_position(move, moved_piece)
                simulation_state.set_piece_by_position(
                    piece_position, EmptyPosition())
                if not simulation_state.color_threating_opposing_king(simulation_state.check):
                    return False
        return True

    def is_checkmate(self) -> tuple[bool, PieceColorEnum]:
        return self.checkmate, self.check

    def update_state_of_check(self):
        color_of_turn = PieceColorEnum.WHITE if self.turn % 2 == 1 else PieceColorEnum.BLACK
        if piece_position := self.color_threating_opposing_king(color_of_turn):
            self.check = color_of_turn
            self.check_attacker_position = piece_position
        self.turn += 1

    def color_threating_opposing_king(self, color: PieceColorEnum) -> Position | None:
        moves = self.get_all_possible_moves_from_color(
            color)
        for piece_position in moves:
            if len(list(filter(lambda x: isinstance(self.state[x], King), moves[piece_position]))) > 0:
                return piece_position
        return None

    def validate_move_and_check_condition(self):
        color_of_turn = PieceColorEnum.WHITE if self.turn % 2 == 1 else PieceColorEnum.BLACK
        if piece_position := self.color_threating_opposing_king(color_of_turn.get_opposing_color()):
            piece = self.get_piece_by_position(piece_position)
            raise Exception(
                f"Invalid Move: Player's own king would be in check by {piece.name} in {piece_position.to_string()}")

    def get_all_possible_moves_from_color(self, color: PieceColorEnum) -> dict[Position, list[Position]]:
        pieces = filter(
            lambda x: self.state[x].get_color() == color, self.state)
        return {position: self.state[position].get_possible_moves(self, position) for position in pieces}

    def get_all_possible_moves_from_piece_in_position(self, position: Position, validate: bool = False) -> list[Position]:
        piece = self.get_piece_by_position(position)
        if validate:
            if not self.validate_move_is_from_the_correct_player(piece):
                return []
        return piece.get_possible_moves(self, position)

    def validate_move_is_from_the_correct_player(self, piece: AbstractPiece | None) -> bool:
        if piece == None:
            return False
        match self.turn % 2:
            case 1:
                if piece.get_color() != PieceColorEnum.WHITE:
                    return False
            case 0:
                if piece.get_color() != PieceColorEnum.BLACK:
                    return False
        return True

    def set_piece_by_indexes(self, x: int, y: int, piece: AbstractPiece):
        self.state[Position(x, y)] = piece

    def get_piece_by_indexes(self, x: int, y: int):
        return self.state[Position(x, y)]

    def set_piece_by_position(self, position: Position, piece: AbstractPiece, is_a_move: bool = True):
        self.state[position] = piece
        if piece and is_a_move:
            piece.update_state(self, position)

    def get_piece_by_position(self, position: Position):
        return self.state[position]
