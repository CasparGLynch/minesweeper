import time

import pygame

from objects.Object import Object


class TimerObject(Object):
    def __init__(self, index, surface: pygame.Surface, rect: pygame.Rect):
        self.x = index[1]
        self.y = index[0]
        self.surface = surface
        self.rect = rect
        self.start_time = 00.00

    def get_elapsed(self):
        if not self.start_time == 00.00:
            elapsed_time = time.time() - self.start_time
            return f'{elapsed_time:.2f}'
        else:
            return '0.00'

    def start_timer(self):
        self.start_time = time.time()
