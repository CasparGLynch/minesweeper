import random

import numpy as np


def generate_random_index(already_taken_indexes: list):
    while True:
        num_x = random.randint(0, 29)
        num_y = random.randint(0, 15)
        for i in already_taken_indexes:
            if i[1] == num_x:
                if i[0] == num_y:
                    return generate_random_index(already_taken_indexes)
        return num_x, num_y


def set_up_board():
    board = np.zeros((16, 30))
    index_not_allowed = []
    while len(index_not_allowed) < 99:
        index_not_allowed.append(generate_random_index(index_not_allowed))

    for i in index_not_allowed:
        board[i[1]][i[0]] = 1

    return board


mine_map_10_10 = set_up_board()
display_map_10_10 = np.zeros((16, 30))
