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
            return f'{self.start_time:.1f}'
        else:
            return '0.0'

    def start_timer(self):
        self.start_time = 0.0

    def add_time(self):
        self.start_time += float(1/30)
