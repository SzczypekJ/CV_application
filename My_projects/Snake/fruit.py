import pygame
from pygame.math import Vector2
import random

cell_size = 40
cell_number = 20

screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))


# importing image of apple
apple = pygame.image.load("Graphics/apple.png").convert_alpha()


class Fruit:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rectangle = pygame.Rect(
            (self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size))
        screen.blit(apple, fruit_rectangle)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
