import pygame
import sys
import random

# Inicjalizacja Pygame
pygame.init()

# Stałe
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CARD_WIDTH = 73
CARD_HEIGHT = 98
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
NUM_PLAYERS = 4

# Utwórz ekran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Makao')

# Wczytaj obrazki kart
cards = []
for i in range(1, 14):
    for j in range(4):
        card = pygame.image.load(f'cards/{i}_{j}.png')
        card = pygame.transform.scale(card, (CARD_WIDTH, CARD_HEIGHT))
        cards.append(card)

# Klasa reprezentująca kartę
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.image = cards[value + suit * 13]

    def draw(self, x, y):
        screen.blit(self.image, (x, y))

# Klasa reprezentująca talię kart
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(13):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

# Klasa reprezentująca gracza
class Player:
    def __init__(self, player_id):
        self.hand = []
        self.player_id = player_id

    def draw_hand(self, deck):
        self.hand = [deck.draw_card() for _ in range(5)]

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())

    def play_card(self, index, game):
        card = self.hand.pop(index)
        game.current_card = card

# Klasa reprezentująca grę
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(i) for i in range(NUM_PLAYERS)]
        for player in self.players:
            player.draw_hand(self.deck)
        self.current_player = 0
        self.current_card = self.deck.draw_card()
        self.direction = 1  # kierunek gry (1 = zgodny z ruchem wskazówek zegara, -1 = przeciwnie)

    def next_player(self):
        self.current_player = (self.current_player + self.direction) % NUM_PLAYERS

    def draw(self):
        screen.fill(WHITE)
        self.current_card.draw(SCREEN_WIDTH // 2 - CARD_WIDTH // 2, SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2)
        for i, card in enumerate(self.players[0].hand):
            card.draw(i * CARD_WIDTH, SCREEN_HEIGHT - CARD_HEIGHT)

    def check_playable_cards(self, player):
        playable_cards = []
        for card in player.hand:
            if card.suit == self.current_card.suit or card.value == self.current_card.value:
                playable_cards.append(card)
        return playable_cards

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_player == 0:  # Gracz kontrolowany przez użytkownika
                    x, y = pygame.mouse.get_pos()
                    if SCREEN_HEIGHT - CARD_HEIGHT <= y <= SCREEN_HEIGHT and len(self.players[0].hand) > 0:
                        index = x // CARD_WIDTH
                        if index < len(self.players[0].hand):
                            self.players[0].play_card(index, self)
                            self.next_player()
                else:  # Sztuczna inteligencja dla pozostałych graczy
                    self.ai_play(self.players[self.current_player])

    def ai_play(self, player):
        playable_cards = self.check_playable_cards(player)
        if len(playable_cards) > 0:
            card_to_play = random.choice(playable_cards)
            index = player.hand.index(card_to_play)
            player.play_card(index, self)
            self.next_player()
        else:
            player.draw_card(self.deck)

    def apply_special_rules(self, card):
        if card.value == 2 or card.value == 3:
            self.current_player.draw_card(self.deck)
            self.apply_special_rules(self.current_card)
        elif card.value == 4:
            self.direction *= -1
        elif card.value == 11:
            self.request_suit_change()
        elif card.value == 12:
            self.current_player.draw_card(self.deck)
            self.current_player.draw_card(self.deck)
            self.apply_special_rules(self.current_card)

    def request_suit_change(self):
        # Change the suit of the current card
        self.current_card.suit = random.randint(0, 3)

    def run(self):
        while True:
            self.event_handler()
            self.draw()
            pygame.display.flip()

# Uruchom grę
if __name__ == '__main__':
    game = Game()
    game.run()
