import pygame
from src.Interfaces.Console.GameObjects import UIColorsEnum, ObjectSizes, color_switch
from src.Interfaces.Console.GameMechanics import calculate_board_position_by_click


class PygameInstance:
    window: pygame.surface.Surface
    is_highlighted: bool

    def run(self):
        pygame.init()
        self.window = pygame.display.set_mode(ObjectSizes.WINDOW_SIZE)
        self.start_board()
        self.is_highlighted = False
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
        self.start_board(set_of_positions)

    def handle_mouse_click(self):
        self.is_highlighted = True
        mouse_pos = pygame.mouse.get_pos()
        board_pos = calculate_board_position_by_click(
            *mouse_pos)
        self.highlight_list_of_positions([board_pos])

    def start_board(self, highlighted: set[tuple[int, int]] = set()):
        pygame.draw.rect(self.window, UIColorsEnum.BACKGROUND,
                         (0, 0, *ObjectSizes.WINDOW_SIZE))
        color = -1
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
                color *= -1
                x += ObjectSizes.TILE_WIDTH
            y += ObjectSizes.TILE_HEIGHT
        pygame.display.update()
