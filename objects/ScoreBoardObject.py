import pygame

from objects.Object import Object


class ScoreBoardObject(Object):
    def __init__(self, index, surface: pygame.Surface, rect: pygame.Rect):
        self.x = index[1]
        self.y = index[0]
        self.surface = surface
        self.rect = rect
