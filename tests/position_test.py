from app.Entities.chess.Position import Position
import pytest
def test_position_properly_created():
    pos=Position(3,5)
    assert pos.x==3 and pos.y==5

def test_invalid_postion():
    with  pytest.raises(IndexError):
        pos=Position(10,5)