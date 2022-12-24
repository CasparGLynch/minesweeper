import pygame


def play_10_10(screen, defs, font):
    pygame.display.set_caption('Minesweeper')
    screen.fill(defs.play_screen_color)
    for row in range(10):
        row_pos = 40 + defs.square_size_10_10 * row + row
        for column in range(10):
            column_pos = 140 + defs.square_size_10_10 * column + column
            mines = check_how_many_mines(index=(row, column), display_map=defs.display_map_10_10, mine_map=defs.mine_map_10_10)
            mine_surface = font.render(f'{mines}', True, (50, 50, 50))
            mine_rect = mine_surface.get_rect()
            mine_rect.center = (column_pos + 25, row_pos + 25)
            pygame.draw.rect(screen, defs.square_color,
                             ((column_pos, row_pos), (defs.square_size_10_10, defs.square_size_10_10)))
            screen.blit(mine_surface, mine_rect)


def check_collision(mouse_pos):
    pass


def handle_collision_10_10(mouse_pos):
    pass


def check_how_many_mines(index, display_map, mine_map):

    # TODO Fix index checks
    if (display_map[index[0]][index[1]] == 0) | (mine_map[index[0]][index[1]] == 1):
        return - 1
    mine_count = 0
    for i in range(index[0]-1, index[0]+1):
        for j in range(index[1]-1, index[1]+1):
            if mine_map[i][j] == 1:
                mine_count += 1
    return mine_count
