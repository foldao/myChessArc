from dataclasses import dataclass
from typing import Tuple


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
    
    def to_string(self):
        return chr(97+self.x )+str(self.y+1)
    
    def __hash__(self) -> int:
        return self.as_tuple().__hash__()

    def __eq__(self, o: object) -> bool:
        return self.as_tuple().__eq__(o)

    def as_tuple(self) -> Tuple[int, int]:
        return (self.x, self.y)
