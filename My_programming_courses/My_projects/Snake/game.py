import pygame
import sys
from main import Main

# mixer of sound to get sound directly after eating the apple
pygame.mixer.pre_init(44100, -16, 2, 512)
#  setting the game
pygame.init()

# setting the screen
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))

# clock refreshment of game and framerate
clock = pygame.time.Clock()
framerate = 60

# the main object that steering the game
main_game = Main()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# running the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.game_over()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = pygame.Vector2(0, -1)
            elif event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = pygame.Vector2(0, 1)
            elif event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = pygame.Vector2(1, 0)
            elif event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = pygame.Vector2(-1, 0)

    screen.fill((175, 215, 70))

    main_game.draw_elements()

    # draw all our elements
    pygame.display.update()
    clock.tick(framerate)
