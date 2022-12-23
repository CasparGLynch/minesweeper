import pygame

import defs
from game_screens.play_10_10 import play_10_10

pygame.init()

screen = pygame.display.set_mode(defs.window_size_main_menu)


while defs.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            defs.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                defs.running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if defs.current_screen == 'Main Menu':
                if play_rect.collidepoint(mouse_pos):
                    defs.current_screen = 'Play_10_10'
            if defs.current_screen == 'Play_10_10':
                if check_collision_10_10(mouse_pos):
                    handle_collision_10_10(mouse_pos)

    if defs.current_screen == 'Main':

        screen.fill(defs.main_menu_screen_color)
        pygame.display.set_caption('Main Menu')
        font = pygame.font.Font(None, 36)
        text = font.render("Play", True, defs.main_menu_font_color)
        play_rect = text.get_rect()
        play_rect.center = (defs.window_size_main_menu[0] / 2, defs.window_size_main_menu[1] / 2)
        screen.blit(text, play_rect)

    elif defs.current_screen == 'Play_10_10':
        play_10_10(screen, defs)

    pygame.display.flip()
pygame.quit()
