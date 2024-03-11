import pygame
import random

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))

CARD_WIDTH = cell_size * 2
CARD_HEIGHT = cell_size * 3

# importing the appearance of cards
cards = []
for i in range(1, 14):
    for j in range(4):
        card = pygame.image.load(f'cards/{i}_{j}.png')
        card = pygame.transform.scale(card, (CARD_WIDTH, CARD_HEIGHT))
        cards.append(card)

# adding the back of the cards to the cards
back_of_the_card = pygame.image.load(f'cards/back_of_the_card.png')
back_of_the_card = pygame.transform.scale(
    back_of_the_card, (CARD_WIDTH, CARD_HEIGHT))
cards.append(back_of_the_card)


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

        self.image = cards[value * 4 + suit]

    def draw(self, x, y):
        screen.blit(self.image, (x, y))

    def __repr__(self):
        return f"{self.value} of {self.suit}"
