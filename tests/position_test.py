from src.Entities.Position import Position
import pytest


def test_position_properly_created():
    pos = Position(3, 5)
    assert pos.x == 3 and pos.y == 5

def test_try_create_valid_postion():
    pos=Position.try_to_create(3, 5)
    assert pos ==Position(3,5)

def test_invalid_postion_to_the_right():
    with pytest.raises(IndexError):
        Position(10, 5)
        

def test_try_create_invalid_postion_to_the_right():
    pos=Position.try_to_create(10, 5)
    assert pos is None


def test_invalid_postion_to_the_left():
    with pytest.raises(IndexError):
        Position(-1, 5)
        

def test_try_create_invalid_postion_to_the_left():
    pos=Position.try_to_create(-1, 5)
    assert pos is None


def test_invalid_postion_upwards():
    with pytest.raises(IndexError):
        Position(5, 10)
        

def test_try_create_invalid_postion_upwards():
    pos=Position.try_to_create(5, 10)
    assert pos is None


def test_invalid_postion_downwards():
    with pytest.raises(IndexError):
        Position(5, -5)
        

def test_try_create_invalid_postion_downwards():
    pos=Position.try_to_create(5, -5)
    assert pos is None

def test_tuple_sum():
    x=(1,2)
    y=4,4
    assert Position.tuple_sum(x,y)==(5,6)