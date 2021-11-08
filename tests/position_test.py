from src.Entities.chess.Position import Position
import pytest
def test_position_properly_created():
    pos=Position(3,5)
    assert pos.x==3 and pos.y==5

def test_invalid_postion_to_the_right():
    with  pytest.raises(IndexError):
        pos=Position(10,5)
def test_invalid_postion_to_the_left():
    with  pytest.raises(IndexError):
        pos=Position(-1,5)
def test_invalid_postion_upwards():
    with  pytest.raises(IndexError):
        pos=Position(5,10)
def test_invalid_postion_downwards():
    with  pytest.raises(IndexError):
        pos=Position(5,-5)
        
 