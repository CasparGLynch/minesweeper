import pygame

import generate_board
from objects.Object import Object


class TileObject(Object):

    def __init__(self, pos_x, pos_y, index, surface: pygame.Surface, rect: pygame.Rect):
        self.x = index[1]
        self.y = index[0]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.surface = surface
        self.rect = rect
        self.neighbors = self.get_neighbors(index[1], index[0])

    @staticmethod
    def get_neighbors(x, y):
        neighbors = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if (i >= 0) and (i < 30) and (j >= 0) and (j < 16):
                    neighbors.append((j, i))
        return neighbors

    def is_revealed(self) -> bool:
        return generate_board.display_map_16_30[self.y][self.x] == 1

    def is_mine(self) -> bool:
        return generate_board.mine_map_16_30[self.y][self.x] == 1

    def is_flag(self) -> bool:
        return generate_board.display_map_16_30[self.y][self.x] == 2

    def count_mines(self) -> int:
        num_of_mines = 0
        for neighbor in self.neighbors:
            if generate_board.mine_map_16_30[neighbor[0]][neighbor[1]] == 1:
                num_of_mines += 1
        return num_of_mines

    def handle_clicked(self, mouse_pos, right_click, shift):
        if self.rect.collidepoint(mouse_pos):
            if generate_board.display_map_16_30[self.y][self.x] == 0:
                if right_click or shift:
                    generate_board.display_map_16_30[self.y][self.x] = 2
                else:
                    generate_board.display_map_16_30[self.y][self.x] = 1
            elif generate_board.display_map_16_30[self.y][self.x] == 2:
                if right_click or shift:
                    generate_board.display_map_16_30[self.y][self.x] = 0

    def text_to_display(self):
        if self.is_flag():
            return 'F'
        elif self.is_revealed():
            if self.is_mine():
                return 'M'
            else:
                return f'{self.count_mines()}'
        else:
            return ''

    def bkg_color_to_display(self):
        if self.is_revealed():
            if self.is_mine():
                return 250, 0, 0
            else:
                return 200, 200, 200
        else:
            return 180, 180, 180

    def text_color_to_display(self):
        if self.is_revealed():
            if self.is_mine():
                return 0, 0, 0
            else:
                mine_count = self.count_mines()
                if mine_count == 0:
                    return 245, 242, 242
                elif mine_count == 1:
                    return 3, 36, 255
                elif mine_count == 2:
                    return 24, 135, 28
                elif mine_count == 3:
                    return 219, 24, 2
                elif mine_count == 4:
                    return 17, 14, 99
                elif mine_count == 5:
                    return 74, 17, 10
                elif mine_count == 6:
                    return 21, 116, 138
                elif mine_count == 7:
                    return 0, 0, 0
                else:
                    return 115, 115, 115
        else:
            return 0, 0, 0
