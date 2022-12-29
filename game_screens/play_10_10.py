import pygame


def play_10_10(screen, defs, font, game_clicked_mouse, shift_clicked_mouse, clicks):
    pygame.display.set_caption('Minesweeper')
    screen.fill(defs.play_screen_color)
    for row in range(16):
        row_pos = 40 + defs.square_size_10_10 * row + row
        for column in range(30):
            column_pos = 140 + defs.square_size_10_10 * column + column
            if (game_clicked_mouse[0] > column_pos) & (game_clicked_mouse[0] < column_pos + 30) & \
                    (game_clicked_mouse[1] > row_pos) & (game_clicked_mouse[1] < row_pos + 30) & \
                    (defs.display_map_10_10[row][column] == 0):
                if (clicks == 1) & (defs.mine_map_10_10[row][column] == 1):
                    defs.mine_map_10_10[row][column] = 0
                elif defs.mine_map_10_10[row][column] == 1:
                    defs.lost = True
                defs.display_map_10_10[row][column] = 1
            if (shift_clicked_mouse[0] > column_pos) & (shift_clicked_mouse[0] < column_pos + 30) & \
                    (shift_clicked_mouse[1] > row_pos) & (shift_clicked_mouse[1] < row_pos + 30):
                if defs.display_map_10_10[row][column] == 0:
                    defs.display_map_10_10[row][column] = 2
                elif defs.display_map_10_10[row][column] == 2:
                    defs.display_map_10_10[row][column] = 0
                elif defs.display_map_10_10[row][column] == 1:
                    mine_display_tuple = reveal_neighbors(index=(row, column), display_map=defs.display_map_10_10,
                                                          mine_map=defs.mine_map_10_10)
                    defs.mine_map_10_10 = mine_display_tuple[1]
                    defs.display_map_10_10 = mine_display_tuple[0]
            mines = check_how_many_mines(index=(row, column), display_map=defs.display_map_10_10,
                                         mine_map=defs.mine_map_10_10)
            current_color = defs.square_color
            display = mines
            if mines == -3:
                display = 'M'
                current_color = (255, 0, 0)
                defs.lost = True
            if mines == -2:
                display = 'F'
            if mines == -1:
                display = ''
            text_color = color_picker(mines)
            mine_surface = font.render(f'{display}', True, text_color)
            mine_rect = mine_surface.get_rect()
            mine_rect.center = (column_pos + 15, row_pos + 15)
            square_rect = pygame.Rect(column_pos, row_pos, defs.square_size_10_10, defs.square_size_10_10)
            pygame.draw.rect(screen, current_color, square_rect)
            screen.blit(mine_surface, mine_rect)


def color_picker(mines):
    text_color = (0, 0, 0)
    if mines == 0:
        text_color = (255, 255, 255)
    if mines == 1:
        text_color = (0, 51, 204)
    if mines == 2:
        text_color = (0, 204, 0)
    if mines == 3:
        text_color = (255, 0, 0)
    if mines == 4:
        text_color = (0, 0, 153)
    if mines == 5:
        text_color = (153, 0, 0)
    if mines == 6:
        text_color = (0, 153, 153)
    if mines == 7:
        text_color = (128, 0, 255)
    if mines == 8:
        text_color = (204, 204, 204)
    return text_color


def get_neighbors_16_30(index):
    neighbors_x = (index[1] - 1, index[1] + 2)
    neighbors_y = (index[0] - 1, index[0] + 2)
    if neighbors_x[0] < 0:
        neighbors_x = (0, index[1] + 2)
    elif neighbors_x[1] > 30:
        neighbors_x = (index[1] - 1, 30)

    if neighbors_y[0] < 0:
        neighbors_y = (0, index[0] + 2)
    elif neighbors_y[1] > 16:
        neighbors_y = (index[0] - 1, 16)
    neighbors = []
    for x in range(neighbors_x[0], neighbors_x[1]):
        for y in range(neighbors_y[0], neighbors_y[1]):
            neighbors.append((y, x))
    neighbors.remove(index)
    return neighbors


def check_how_many_mines(index, display_map, mine_map):
    if display_map[index[0]][index[1]] == 0:
        return -1
    if display_map[index[0]][index[1]] == 2:
        return -2
    if mine_map[index[0]][index[1]] == 1:
        return -3
    mine_count = 0
    for i in get_neighbors_16_30(index):
        if mine_map[i[0]][i[1]] == 1:
            mine_count += 1
    return mine_count


def check_if_completed(index, display_map, mine_map):
    num_mines = check_how_many_mines(index, display_map, mine_map)
    flag_count = 0
    for i in get_neighbors_16_30(index):
        if display_map[i[0]][i[1]] == 2:
            flag_count += 1
    return flag_count == num_mines


def reveal_neighbors(index, display_map, mine_map):
    if check_if_completed(index, display_map, mine_map):
        neighbors = get_neighbors_16_30(index)

        for neighbor in neighbors:
            mines = check_how_many_mines(neighbor, display_map, mine_map)
            if (mines == 0) | (mines == -1):
                display_map[neighbor[0]][neighbor[1]] = 1

        return display_map, mine_map
    else:
        return display_map, mine_map
