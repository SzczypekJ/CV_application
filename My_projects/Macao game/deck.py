# deck.py
import random
from cards import Card  # Zakładam, że Card jest importowane z cards.py


class Deck:
    def __init__(self):
        self.cards = self.initialize_deck()
        self.discard_pile = []

    def initialize_deck(self):
        # Tworzenie standardowej talii kart
        deck = []
        for value in range(1, 14):  # Wartości od 1 do 13
            for suit in range(4):  # 4 kolory (0, 1, 2, 3)
                deck.append(Card(value, suit))
        random.shuffle(deck)
        return deck

    def draw_card(self):
        if not self.cards:
            self.reshuffle_discard_pile()
        if self.cards:
            return self.cards.pop()
        else:
            raise IndexError("No cards left to draw")

    def copy(self):
        new_deck = Deck()
        new_deck.cards = self.cards[:]
        new_deck.discard_pile = self.discard_pile[:]
        return new_deck

    def reshuffle_discard_pile(self):
        if self.discard_pile:
            self.cards = self.discard_pile[:]
            self.discard_pile = []
            random.shuffle(self.cards)
