from typing import Any
import pygame
from src.Entities.ChessPieces.Pawn import Pawn
from src.Entities.ChessPieces.Rook import Rook
from src.Entities.ChessPieces.Horse import Horse
from src.Entities.ChessPieces.King import King
from src.Entities.ChessPieces.Queen import Queen
from src.Entities.ChessPieces.Bishop import Bishop
from src.Interfaces.Console.GameObjects import Assets, UIColorsEnum, ObjectSizes, color_switch
from src.Interfaces.Console.GameMechanics import calculate_board_position_by_click
from src.Interfaces.Repositories.Abstracts.BoardStateRepoABC import BoardStateRepoABC
from src.UseCases.BoardMoveUseCase import BoardMoveUseCase


class PygameInstance:

    window: pygame.surface.Surface
    highlighted_positions: list[tuple[int, int]] = []
    highlighted_piece_position: tuple[int, int] | None = None
    pieces: dict[tuple[str, int], pygame.surface.Surface] = {}
    match_repo: BoardStateRepoABC
    match_controller: BoardMoveUseCase
    myfont: pygame.font.Font
    rendered_objects: list[Any]

    def __init__(self, match_repo: BoardStateRepoABC) -> None:
        self.match_repo = match_repo
        self.match_controller = BoardMoveUseCase(self.match_repo)
        pygame.init()
        pygame.font.init()  # you have to call this at the start,
        # if you want to use this module.
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.window = pygame.display.set_mode(ObjectSizes.WINDOW_SIZE)
        self.load_pieces()
        self.draw_board(message="Whites start!")


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                match event.type:
                    case pygame.MOUSEBUTTONUP:
                        self.handle_mouse_click()
                    case pygame.KEYDOWN:
                        pass
                if event.type == pygame.QUIT:
                    running = False
                    break

        pygame.quit()

    def highlight_list_of_positions(self, positions: list[tuple[int, int]]):
        set_of_positions: set[tuple[int, int]] = set(positions)
        self.draw_board(set_of_positions)

    def handle_mouse_click(self):
        mouse_pos = pygame.mouse.get_pos()
        try:
            board_pos = calculate_board_position_by_click(
                *mouse_pos)
        except Exception:
            return
        if not self.highlighted_positions:
            available_positions = self.match_controller.get_possible_moves(
                board_pos)
            self.highlight_list_of_positions([board_pos, *available_positions])
            self.highlighted_positions = available_positions
            self.highlighted_piece_position = board_pos
            return
        if board_pos in self.highlighted_positions and self.highlighted_piece_position:
            try:
                self.match_controller.move(
                    self.highlighted_piece_position, board_pos)
            except Exception as e:
                self.draw_board(message=str(e),message_color=UIColorsEnum.RED)
                
                return
                
        self.draw_board()
        self.highlighted_positions = []
        self.highlighted_piece_position = None

    def load_pieces(self) -> None:
        asts: dict[tuple[str, int], pygame.surface.Surface] = {}
        asts[(Pawn.name, -1)] = pygame.image.load(Assets.WhitePawn)
        asts[(Rook.name, -1)] = pygame.image.load(Assets.WhiteRook)
        asts[(Queen.name, -1)] = pygame.image.load(Assets.WhiteQueen)
        asts[(King.name, -1)] = pygame.image.load(Assets.WhiteKing)
        asts[(Bishop.name, -1)] = pygame.image.load(Assets.WhiteBishop)
        asts[(Horse.name, -1)] = pygame.image.load(Assets.WhiteKnightR)
        asts[(Horse.name, 1)] = pygame.image.load(Assets.BlackKnightL)
        asts[(Pawn.name, 1)] = pygame.image.load(Assets.BlackPawn)
        asts[(Rook.name, 1)] = pygame.image.load(Assets.BlackRook)
        asts[(Queen.name, 1)] = pygame.image.load(Assets.BlackQueen)
        asts[(King.name, 1)] = pygame.image.load(Assets.BlackKing)
        asts[(Bishop.name, 1)] = pygame.image.load(Assets.BlackBishop)
        self.pieces = asts

    def draw_board(self, highlighted: set[tuple[int, int]] = set(), message:str="", message_color:tuple[int,int,int]=UIColorsEnum.WHITE):
        pygame.draw.rect(self.window, UIColorsEnum.BACKGROUND,
                         (0, 0, *ObjectSizes.WINDOW_SIZE))
        color = -1
        state, check, checkmate = self.match_controller.get_state()
        if check:
            if checkmate:
                self.display_message(f"{check.name}S WON!! ")
                return
            else:
                self.display_message(f"{check.name} is making a check!")
        y = ObjectSizes.PANNEL_HEIGHT
        for j in range(8):
            color *= -1
            x = ObjectSizes.BORDER
            for i in range(8):
                rect_color = UIColorsEnum.HIGHLIGHT if (
                    i, j) in highlighted else color_switch[color]

                # tiles[(i, j)] =
                pygame.draw.rect(self.window, rect_color,
                                 (x, y, *ObjectSizes.TILE_SIZE))
                if (i, j) in state:
                    self.window.blit(self.pieces[state[(i, j)]], (x, y))
                    # pygame.display.update()
                color *= -1
                x += ObjectSizes.TILE_WIDTH
            y += ObjectSizes.TILE_HEIGHT
        if message:
            self.display_message(message, message_color)
        pygame.display.update()

    def display_message(self,msg:str,color:tuple[int,int,int]= UIColorsEnum.WHITE):
        text=self.myfont.render(msg,True,color, UIColorsEnum.BACKGROUND)
        text_rectangle=text.get_rect()
        text_rectangle.center=(ObjectSizes.WINDOW_SIZE[0]//2, (ObjectSizes.WINDOW_SIZE[1]-ObjectSizes.BOARD_SIZE[1])//2)
        self.window.blit(text,text_rectangle)
        # return text,text_rectangle
    def start_match(self):
        pass
