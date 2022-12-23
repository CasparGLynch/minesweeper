import random

import numpy as np

window_size_main_menu = (800, 600)
window_size_10_10 = (500, 500)
running = True
main_menu_screen_color = (120, 120, 120)
play_screen_color = (100, 100, 100)
main_menu_font_color = (250, 250, 250)
current_screen = 'Main'
square_color = (200, 200, 200)
square_size_10_10 = 50


def generate_random_index(already_taken_indexes: list):
    while True:
        num_x = random.randint(0, 9)
        num_y = random.randint(0, 9)
        for i in already_taken_indexes:
            if i[0] == num_x:
                if i[1] == num_y:
                    return generate_random_index(already_taken_indexes)
        return num_x, num_y


def set_up_board():
    board = np.zeros((10, 10))
    index_not_allowed = []
    while len(index_not_allowed) < 10:
        index_not_allowed.append(generate_random_index(index_not_allowed))


minesweeper_board_10_10 = generate_random_index([])

a = 1
