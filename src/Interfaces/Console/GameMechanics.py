from src.Interfaces.Console.GameObjects import ObjectSizes as OS


def calculate_tile_origin_by_click(x: int, y: int):
    if any([x < OS.BORDER, x > OS.BORDER+OS.BOARD_SIZE[0], y < OS.PANNEL_HEIGHT, y > OS.PANNEL_HEIGHT+OS.BOARD_SIZE[1]]):
        raise IndexError("Not In Board")
    x_in_reference_to_board = x-OS.BORDER
    width_from_x_to_tile_origin = x_in_reference_to_board % OS.TILE_WIDTH
    y_in_reference_to_board = y-OS.PANNEL_HEIGHT
    height_from_y_to_tile_origin = y_in_reference_to_board % OS.TILE_HEIGHT
    return (x-width_from_x_to_tile_origin, y-height_from_y_to_tile_origin)


def calculate_board_position_by_tile_origin(x: int, y: int):
    x_in_reference_to_board = x-OS.BORDER
    x_position = int(x_in_reference_to_board/OS.TILE_WIDTH)
    y_in_reference_to_board = y-OS.PANNEL_HEIGHT
    y_position = int(y_in_reference_to_board/OS.TILE_HEIGHT)
    return (x_position, y_position)


def calculate_tile_origin_by_board_position(x: int, y: int):
    x_skipping_tiles = x*OS.TILE_WIDTH
    x_origin = x_skipping_tiles+OS.BORDER
    y_skipping_tiles = y*OS.TILE_HEIGHT
    y_origin = y_skipping_tiles+OS.PANNEL_HEIGHT
    return (x_origin, y_origin)


def calculate_board_position_by_click(x: int, y: int):
    _x, _y = calculate_tile_origin_by_click(x, y)
    return calculate_board_position_by_tile_origin(_x, _y)


# def high_light_tile_by_origin(x: int, y: int):
