import pygame
from pygame.event import Event

from events.ChangeWindowEvent import ChangeWindowEvent
from windows.GameWindow import GameWindow
from windows.Window import Window


class MainMenuWindow(Window):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.screen_rectangles = []
        self.to_be_updated = []
        # creating the initial main menu display
        self.font = pygame.font.Font(None, 36)
        text_surfaces = self.font.render('Play', True, (0, 0, 0))
        text_rect = text_surfaces.get_rect()
        x = width // 2 - text_rect.width // 2
        y = height // 2 - text_rect.height // 2
        text_rect.x = x
        text_rect.y = y
        self.screen_rectangles.append((text_surfaces, text_rect))
        self.to_be_updated.append((text_surfaces, text_rect))

    def handle_event(self, event: Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, (surface, rect) in enumerate(self.screen_rectangles):
                if rect.collidepoint(event.pos):
                    return ChangeWindowEvent(GameWindow)

    def update(self, mouse_pos):
        for index, (surface, rect) in enumerate(self.screen_rectangles):
            pass

    def display(self):
        ret_val = self.to_be_updated.copy()
        self.to_be_updated.clear()
        return ret_val
