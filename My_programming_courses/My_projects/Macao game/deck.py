import random
from cards import Card


class Deck:
    # shuffle the cards objects
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    # method allows you to draw a card from the top of the deck
    def draw_card(self):
        return self.cards.pop()

    # def show_back_of_the_card(self):
    #     screen.blit(self.image, (x, y))
