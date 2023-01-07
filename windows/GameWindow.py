import pygame
from pygame.event import Event

import generate_board
from events.ChangeWindowEvent import ChangeWindowEvent

from objects.TileObject import TileObject
from windows.Window import Window


class GameWindow(Window):
    __clicks = 0

    def __init__(self, width, height):
        super().__init__(width, height)
        self.to_be_updated = []
        self.screen_rects = []
        square_size = 30
        # top left of grid
        grid_x = (width // 2) - (30 * square_size // 2)
        grid_y = (height // 2) - (16 * square_size // 2)
        # generating initial board
        for i in range(16):
            for j in range(30):
                y = grid_y + i * square_size + i
                x = grid_x + j * square_size + j
                square_surface = pygame.Surface((square_size, square_size))
                square_surface.fill((180, 180, 180))
                square_rect = square_surface.get_rect()
                square_rect.x = x
                square_rect.y = y
                tile = TileObject(pos_x=x, pos_y=y, index=(i, j), surface=square_surface, rect=square_rect)
                self.screen_rects.append(tile)
                self.to_be_updated.append(tile)

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return ChangeWindowEvent('GameWindow', 'game_switch')
        if event.type == pygame.MOUSEBUTTONDOWN:
            ret_val = None
            for index, (tile) in enumerate(self.screen_rects):
                if tile.rect.collidepoint(event.pos):
                    # handle first click is mine edge case
                    if self.__clicks == 0:
                        generate_board.mine_map_16_30[tile.y][tile.x] = 0
                        if tile.x < 27:
                            generate_board.mine_map_16_30[tile.y][tile.x + 3] = 1
                        else:
                            generate_board.mine_map_16_30[tile.y][tile.x - 3] = 1
                    if (generate_board.mine_map_16_30[tile.y][tile.x] == 1) and not \
                            (event.button == 3) and not \
                            ((pygame.key.get_mods() & pygame.KMOD_SHIFT)): # noqa
                        ret_val = ChangeWindowEvent('LoseWindow', 'lose')
                    tile.handle_clicked(
                        mouse_pos=event.pos,
                        right_click=(event.button == 3),
                        shift=(pygame.key.get_mods() & pygame.KMOD_SHIFT)
                    )
                    tile.surface.fill(tile.bkg_color_to_display())

                    font = pygame.font.Font('fonts/pixel.ttf', 40)
                    text_surface = font.render(tile.text_to_display(), True, tile.text_color_to_display())
                    tile.surface.blit(text_surface, (9, 1))

                    new_rect = tile.surface.get_rect()
                    new_rect.x = tile.rect.x
                    new_rect.y = tile.rect.y
                    tile.rect = new_rect
                    self.to_be_updated.append(tile)
                    self.screen_rects[index] = tile
                    self.__clicks += 1
            return ret_val

    def update(self, mouse_pos):
        pass

    def display(self):
        ret_val = [(obj.surface, obj.rect) for obj in self.to_be_updated]
        self.to_be_updated.clear()
        return ret_val
