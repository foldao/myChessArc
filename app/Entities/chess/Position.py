from dataclasses import dataclass

@dataclass
class Position:
    x:int
    y:int
    def __post_init__(self):
        if not Position.is_valid(self.x,self.y):
                raise IndexError
    @staticmethod
    def is_valid(x:int,y:int)->bool:
        return all([x<=7,y<=7])