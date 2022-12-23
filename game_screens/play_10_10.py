import pygame


def play_10_10(screen, defs):
    pygame.display.set_caption('Minesweeper')
    screen.fill(defs.play_screen_color)
    for row in range(10):
        row_pos = 40 + defs.square_size_10_10 * row + row
        for column in range(10):
            column_pos = 140 + defs.square_size_10_10 * column + column
            pygame.draw.rect(screen, defs.square_color,
                             ((column_pos, row_pos), (defs.square_size_10_10, defs.square_size_10_10)))


def check_collision(mouse_pos):
    pass


def handle_collision_10_10(mouse_pos):
    pass
