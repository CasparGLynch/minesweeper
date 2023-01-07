import sys

import pygame.display

from events.ChangeWindowEvent import ChangeWindowEvent
from windows.MainMenuWindow import MainMenuWindow


class Main:

    def __init__(self):
        pygame.init()
        self.s_height = 1200
        self.s_width = 675
        self.running = True
        self.display = pygame.display.set_mode((self.s_height, self.s_width))
        self.screen = pygame.display
        self.display.fill((200, 200, 200))
        self.currentWindow = MainMenuWindow(self.s_height, self.s_width)

    def run(self):
        self.screen.flip()
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                event = self.currentWindow.handle_event(event)
                if event.__class__ == ChangeWindowEvent:
                    self.currentWindow = event.new_window(self.s_width, self.s_height)
                    self.display.fill((200, 200, 200))
                    self.screen.update()

            # update
            self.currentWindow.update(pygame.mouse.get_pos())

            # all the rectangles that have to be updated
            to_be_updated = self.currentWindow.display()
            for surface, rect in to_be_updated:
                self.display.fill((200, 200, 200), rect)
                self.display.blit(surface, (rect.x, rect.y))
                self.screen.update(rect)

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Main().run()
