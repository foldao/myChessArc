class UIColorsEnum:
    BLACK = (226, 175, 78)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BACKGROUND = (95, 112, 120)
    HIGHLIGHT = (254, 252, 127)


class ObjectSizes:
    BORDER = 20
    PANNEL_HEIGHT = 200
    TILE_WIDTH = 80
    TILE_HEIGHT = 80
    TILE_SIZE = (TILE_WIDTH, TILE_HEIGHT)
    BOARD_SIZE = (8*TILE_WIDTH, 8*TILE_HEIGHT)
    WINDOW_SIZE = (BOARD_SIZE[0]+2*BORDER, BOARD_SIZE[1]+BORDER+PANNEL_HEIGHT)


color_switch = {1: UIColorsEnum.WHITE, -1: UIColorsEnum.BLACK}


class Assets:
    BlackBishop = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackBishop.png'
    BlackHorseR = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackHorseR.png'
    BlackKing = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackKing.png'
    BlackKnightL = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackKnightL.png'
    BlackPawn = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackPawn.png'
    BlackQueen = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackQueen.png'
    BlackRook = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/BlackRook.png'
    WhiteBishop = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhiteBishop.png'
    WhiteKing = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhiteKing.png'
    WhiteKnightL = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhiteKnightL.png'
    WhiteKnightR = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhiteKnightR.png'
    WhitePawn = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhitePawn.png'
    WhiteQueen = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhiteQueen.png'
    WhiteRook = r'/home/fpx/_projects/myChessArc/src/Interfaces/Console/assets/Pieces/WhiteRook.png'
