import time

import pygame

from objects.Object import Object


class TimerObject(Object):
    def __init__(self, index, surface: pygame.Surface, rect: pygame.Rect):
        self.x = index[1]
        self.y = index[0]
        self.surface = surface
        self.rect = rect
        self.start_time = time.time()

    def get_elapsed(self):
        elapsed_time = time.time() - self.start_time
        return f'{elapsed_time:.2f}'
