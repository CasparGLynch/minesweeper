import random
from unittest import TestCase

from game_screens.play_10_10 import get_neighbors_16_30


class Test_16_30(TestCase):
    def test__get_neighbors__top_left(self):
        index = (0, 0)
        expected_neighbors = [(1, 0), (1, 1), (0, 1)]
        self.assertListEqual(sorted(get_neighbors_16_30(index)), sorted(expected_neighbors))

    def test__get_neighbors__bottom_left(self):
        index = (15, 0)
        expected_neighbors = [(15, 1), (14, 1), (14, 0)]
        self.assertListEqual(sorted(get_neighbors_16_30(index)), sorted(expected_neighbors))

    def test__get_neighbors__top_right(self):
        index = (0, 29)
        expected_neighbors = [(1, 29), (0, 28), (1, 28)]
        self.assertListEqual(sorted(get_neighbors_16_30(index)), sorted(expected_neighbors))

    def test__get_neighbors__bottom_right(self):
        index = (15, 29)
        expected_neighbors = [(14, 29), (15, 28), (14, 28)]
        self.assertListEqual(sorted(get_neighbors_16_30(index)), sorted(expected_neighbors))

    def test__get_neighbors__random(self):
        index = (12, 20)
        expected_neighbors = [(11, 20), (13, 20), (11, 21), (12, 21), (13, 21), (11, 19), (12, 19), (13, 19)]
        self.assertListEqual(sorted(get_neighbors_16_30(index)), sorted(expected_neighbors))

    def test__get__neighbors__bottom(self):
        index = (15, 13)
        expected_neighbors = [(15, 12), (15, 14), (14, 12), (14, 13), (14, 14)]
        self.assertListEqual(sorted(get_neighbors_16_30(index)), sorted(expected_neighbors))
