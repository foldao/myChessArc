from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    x: int
    y: int

    def __post_init__(self):
        if not Position.is_valid(self.x, self.y):
            raise IndexError("Position out of the board")

    @staticmethod
    def is_valid(x: int, y: int) -> bool:
        return all([x <= 7, y <= 7, x >= 0, y >= 0])

    @staticmethod
    def tuple_sum(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(map(sum, zip(a, b)))

    @staticmethod
    def try_to_create(x: int, y: int) -> Position | None:
        if Position.is_valid(x, y):
            return Position(x, y)

    def to_string(self):
        return chr(97+self.x)+str(self.y+1)

    def __hash__(self) -> int:
        return hash(self.as_tuple())

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Position):
            return False
        return o.as_tuple() == self.as_tuple()

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)
