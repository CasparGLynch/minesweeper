import pygame
from pygame.event import Event

from events.ChangeWindowEvent import ChangeWindowEvent
from windows.Window import Window


class LoseWindow(Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.to_be_updated = []
        self.screen_rects = []

        self.font = pygame.font.Font('fonts/pixel.ttf', 36)
        text_surfaces = self.font.render('You Lose Nerd! \nPress \'r\' to restart', True, (0, 0, 0))
        text_rect = text_surfaces.get_rect()
        x = width // 2 - text_rect.width // 2
        y = height // 2 - text_rect.height // 2
        text_rect.x = x
        text_rect.y = y
        self.screen_rects.append((text_surfaces, text_rect))
        self.to_be_updated.append((text_surfaces, text_rect))

    def handle_event(self, event: Event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                return ChangeWindowEvent('GameWindow', 'game_switch')

    def update(self, mouse_pos):
        pass

    def display(self):
        ret_val = self.to_be_updated.copy()
        self.to_be_updated.clear()
        return ret_val
