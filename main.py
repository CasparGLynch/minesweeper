import sys
import numpy as np
import pygame.display

from windows.GameWindow import GameWindow
from windows.LoseWindow import LoseWindow
from windows.MainMenuWindow import MainMenuWindow
import generate_board


class Main:
    __frame_rate = 30

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Minesweeper')
        self.windows = {
            'LoseWindow': LoseWindow,
            'MainMenuWindow': MainMenuWindow,
            'GameWindow': GameWindow
        }
        self.s_width = 1200
        self.s_height = 675
        self.running = True
        self.display = pygame.display.set_mode((self.s_width, self.s_height))
        icon_surface = pygame.image.load("icon.jpg").convert_alpha()
        pygame.display.set_icon(icon_surface)
        self.screen = pygame.display
        self.clock = pygame.time.Clock()
        self.display.fill((200, 200, 200))
        self.currentWindow = MainMenuWindow(self.s_width, self.s_height)

    def run(self):
        self.screen.flip()
        while self.running:
            self.clock.tick(self.__frame_rate)
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                event = self.currentWindow.handle_event(event)
                if event is not None:
                    if event.type_e == 'game_switch':
                        generate_board.mine_map_16_30 = generate_board.set_up_board()
                        generate_board.display_map_16_30 = np.zeros((16, 30))
                        self.currentWindow = self.windows[event.new_window](self.s_width, self.s_height)
                        self.display.fill((200, 200, 200))
                        self.screen.update()
                    elif event.type_e == 'restart':
                        generate_board.mine_map_16_30 = generate_board.set_up_board()
                        generate_board.display_map_16_30 = np.zeros((16, 30))
                        self.currentWindow = self.windows[event.new_window](self.s_width, self.s_height)
                        self.screen.update()
                    elif event.type_e == 'lose':
                        to_be_updated = self.currentWindow.display()
                        for surface, rect in to_be_updated:
                            self.display.fill((200, 200, 200), rect)
                            self.display.blit(surface, (rect.x, rect.y))
                            self.screen.update(rect)
                        self.currentWindow = self.windows[event.new_window](self.s_width, self.s_height)
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
