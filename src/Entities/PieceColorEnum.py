from enum import IntEnum


class PieceColorEnum(IntEnum):
    WHITE = 1
    NONE = 0
    BLACK = -1

    def get_opposing_color(self):
        return PieceColorEnum(self.value*(-1))
