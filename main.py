import numpy as np
import pygame

import defs
from game_screens.play_10_10 import play_10_10

pygame.init()

screen = pygame.display.set_mode(defs.window_size_main_menu)

font = pygame.font.Font(None, 36)

clicks = 0

game_clicked_mouse = (0, 0)
shift_clicked_mouse = (0, 0)
while defs.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            defs.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                defs.running = False
            if defs.current_screen == 'Main':
                if event.key == pygame.K_RETURN:
                    defs.current_screen = 'Play_10_10'
            elif defs.current_screen == 'Play_10_10':
                if event.key == pygame.K_r:
                    defs.display_map_10_10 = np.zeros((10, 10))
                    defs.mine_map_10_10 = defs.set_up_board()
                    defs.lost = False
                    clicks = 0

        if not defs.lost:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if defs.current_screen == 'Play_10_10':
                    game_clicked_mouse = mouse_pos
                    clicks += 1
                mods = pygame.key.get_mods()
                if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_RSHIFT:
                    shift_clicked_mouse = mouse_pos
                    game_clicked_mouse = (0, 0)

    if defs.current_screen == 'Main':

        screen.fill(defs.main_menu_screen_color)
        pygame.display.set_caption('Main Menu')
        font = pygame.font.Font(None, 36)
        text = font.render("Press ENTER to Play", True, defs.main_menu_font_color)
        play_rect = text.get_rect()
        play_rect.center = (defs.window_size_main_menu[0] / 2, defs.window_size_main_menu[1] / 2)
        screen.blit(text, play_rect)

    elif defs.current_screen == 'Play_10_10':
        play_10_10(screen, defs, font, game_clicked_mouse, shift_clicked_mouse, clicks)
        game_clicked_mouse = (0, 0)
        shift_clicked_mouse = (0, 0)

        if not np.any(defs.display_map_10_10 == 0):
            defs.running = False
    pygame.display.flip()

pygame.quit()
