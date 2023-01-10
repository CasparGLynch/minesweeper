import random

import numpy as np


def generate_random_index_list():
    already_taken_indexes = []
    while len(already_taken_indexes) < 99:
        num_x = random.randint(0, 29)
        num_y = random.randint(0, 15)
        if (num_x, num_y) not in already_taken_indexes:
            already_taken_indexes.append((num_x, num_y))

    return already_taken_indexes


def set_up_board():
    board = np.zeros((16, 30))
    index_not_allowed = generate_random_index_list()

    for i in index_not_allowed:
        board[i[1]][i[0]] = 1

    return board


mine_map_16_30 = set_up_board()
display_map_16_30 = np.zeros((16, 30))
