from fruit import Fruit
from snake import Snake
import pygame
import sys

pygame.init()

cell_number = 20
cell_size = 40
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))


game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

apple = pygame.image.load("Graphics/apple.png").convert_alpha()


class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.position == self.snake.body[0]:
            # repositioning the fruit
            self.fruit.randomize()
            # adding new block to teh snake
            self.snake.add_block()
            # sound of crunch
            self.snake.play_crunch_sound()

        # checking if the fruit is on teh snake body
        for block in self.snake.body[1:]:
            if block == self.fruit.position:
                self.fruit.randomize()

    def check_fail(self):
        # check if snake is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        # check if snake hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rectangle = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rectangle)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rectangle = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rectangle)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 75, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rectangle = score_surface.get_rect(center=(score_x, score_y))
        apple_rectangle = apple.get_rect(
            midright=(score_rectangle.left, score_rectangle.centery))

        screen.blit(score_surface, score_rectangle)
        screen.blit(apple, apple_rectangle)
