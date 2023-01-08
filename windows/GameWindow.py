import time

import pygame
from pygame.event import Event

import generate_board
from events.ChangeWindowEvent import ChangeWindowEvent

from objects.TileObject import TileObject
from objects.TimerObject import TimerObject
from windows.Window import Window


class GameWindow(Window):
    __clicks = 0

    def __init__(self, width, height):
        super().__init__(width, height)
        self.to_be_updated = []
        self.screen_rects = []
        self.start_time = time.time()
        square_size = 30
        # timer
        timer_surface = pygame.Surface((100, 50))
        timer_surface.fill((180, 180, 180))
        timer_rect = timer_surface.get_rect()
        timer_rect.y = 20
        timer_rect.x = (width // 2) - 30
        self.screen_rects.append(TimerObject(index=(-1, -1), rect=timer_rect, surface=timer_surface))

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
                        # start timer:
                        timer = self.screen_rects[0]
                        timer.start_timer()
                        self.screen_rects[0] = timer

                        generate_board.mine_map_16_30[tile.y][tile.x] = 0
                        if tile.x < 27:
                            generate_board.mine_map_16_30[tile.y][tile.x + 3] = 1
                        else:
                            generate_board.mine_map_16_30[tile.y][tile.x - 3] = 1
                    if (generate_board.mine_map_16_30[tile.y][tile.x] == 1) and not \
                            (event.button == 3) and not \
                            ((pygame.key.get_mods() & pygame.KMOD_SHIFT)):  # noqa
                        ret_val = ChangeWindowEvent('LoseWindow', 'lose')
                    reveal = tile.handle_clicked(
                        mouse_pos=event.pos,
                        right_click=(event.button == 3),
                        shift=(pygame.key.get_mods() & pygame.KMOD_SHIFT)
                    )
                    if reveal:
                        neighbors = [index for index, obj in enumerate(self.screen_rects) if
                                     ((obj.y, obj.x) in reveal)]
                        ret_val = self.reveal_neighbors(neighbors)

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

    def reveal_neighbors(self, neighbors):
        loose = False
        for index in neighbors:

            tile = self.screen_rects[index]
            generate_board.display_map_16_30[tile.y][tile.x] = 1
            if tile.count_mines() == 0:
                # add 0's neighbors to reveal now
                reveal_1 = tile.get_non_revealed_neighbors()
                rev_1 = [index for index, obj in enumerate(self.screen_rects) if ((obj.y, obj.x) in reveal_1)]
                neighbors.extend(rev_1)
                # continue if next is 0
                reveal_2 = tile.get_0_neighbors()
                rev_2 = [index for index, obj in enumerate(self.screen_rects) if
                             ((obj.y, obj.x) in reveal_2)]
                if rev_2:
                    self.reveal_neighbors(rev_2)
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
            if generate_board.mine_map_16_30[tile.y][tile.x] == 1:
                loose = True

        if loose:
            return ChangeWindowEvent('LoseWindow', 'lose')

    def update(self, mouse_pos):
        timer = self.screen_rects[0]
        font = pygame.font.Font('fonts/pixel.ttf', 40)
        text_surface = font.render(timer.get_elapsed(), True, (0, 0, 0))
        timer.surface.fill((200, 200, 200))
        timer.surface.blit(text_surface, (0, 0))
        self.screen_rects[0] = timer
        self.to_be_updated.append(timer)

        # check_victory!
        num_of_flags = 0
        revealed_tiles = 0
        for row in generate_board.display_map_16_30:
            for element in row:
                if element == 2:
                    num_of_flags += 1
                elif element == 1:
                    revealed_tiles += 1
        if (num_of_flags == 99) and (revealed_tiles == 381):
            return ChangeWindowEvent('WinWindow', 'win')

    def display(self):
        ret_val = [(obj.surface, obj.rect) for obj in self.to_be_updated]
        self.to_be_updated.clear()
        return ret_val
