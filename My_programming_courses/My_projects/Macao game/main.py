import pygame
from game import Game

#  setting the game
pygame.init()


# setting the screen
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))

CARD_WIDTH = cell_size * 2
CARD_HEIGHT = cell_size * 3

SCREEN_WIDTH = cell_size * cell_number
SCREEN_HEIGHT = cell_size * cell_number

WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
NUM_PLAYERS = 4

# clock refreshment of game and framerate
clock = pygame.time.Clock()
framerate = 60

# the main object that steering the game
main_game = Game()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# running the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.game_over()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if main_game.current_player == 0:  # Gracz kontrolowany przez użytkownika
                x, y = pygame.mouse.get_pos()
                if SCREEN_HEIGHT - CARD_HEIGHT <= y <= SCREEN_HEIGHT and len(main_game.players[0].hand) > 0:
                    index = x // CARD_WIDTH
                    if index < len(main_game.players[0].hand):
                        main_game.players[0].play_card(index, main_game)
                        main_game.next_player()
            # else:  # Sztuczna inteligencja dla pozostałych graczy
            #     main_game.ai_play(main_game.players[main_game.current_player])

    # draw all our elements
    pygame.display.update()
    clock.tick(framerate)
