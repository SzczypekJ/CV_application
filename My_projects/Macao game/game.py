import sys
import pygame
from player import Player
from bot import Bot
from deck import Deck
from cards import Card
from simplified_game import SimplifiedGame

# Setting the game
pygame.init()

# Setting the screen
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
NUM_PLAYERS = 2

# Clock refreshment of game and framerate
clock = pygame.time.Clock()
framerate = 60

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

# The class which will be steering the whole game


class Game:
    def __init__(self):
        self.deck = Deck()
        self.current_card = self.deck.draw_card()
        self.players = [Player(0, self.deck)] + [Bot(i, self.deck)
                                                 for i in range(1, NUM_PLAYERS)]
        for player in self.players:
            player.draw_hand()

        self.current_player = 0

        # Direction of play (1 = clockwise, -1 = anticlockwise)
        self.direction = 1
        self.attack_stack = 0

    def next_player(self):
        self.current_player = (self.current_player +
                               self.direction) % NUM_PLAYERS

    def draw_all_cards_and_table(self):
        # Fill all the screen with white color - our table
        screen.fill(WHITE)

        # Draw the current card on the middle
        self.current_card.draw(
            SCREEN_WIDTH // 2 - CARD_WIDTH // 2, SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2)

        # Draw the back of the card in the middle to take if your cards don't match
        deck_x = SCREEN_WIDTH // 2 - CARD_WIDTH * 2
        deck_y = SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2
        Card.draw_back(deck_x, deck_y)

        # Draw the cards in your hand
        for i, card in enumerate(self.players[0].hand):
            card.draw(i * CARD_WIDTH, SCREEN_HEIGHT - CARD_HEIGHT)

    def check_playable_cards(self, card):
        return (card.suit == self.current_card.suit or
                card.value == self.current_card.value or
                (self.attack_stack > 0 and card.value in [2, 3]))

    def apply_special_rules(self, card):
        if card.value == 2:
            self.attack_stack += 2
        elif card.value == 3:
            self.attack_stack += 3
        elif card.value == 11:
            self.jupek_initiated(card)
        elif card.value == 13 and card.suit in [0, 3]:
            self.attack_stack += 5

    def jupek_initiated(self, card):
        required_value = card.value
        for player in self.players:
            if player != self.players[self.current_player]:
                playable = False
                for c in player.hand:
                    if c.value == required_value:
                        playable = True
                        break
                if not playable:
                    player.add_one_card()

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.current_player == 0:
                x, y = pygame.mouse.get_pos()
                deck_x = SCREEN_WIDTH // 2 - CARD_WIDTH * 2
                deck_y = SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2

                if deck_x <= x <= deck_x + CARD_WIDTH and deck_y <= y <= deck_y + CARD_HEIGHT:
                    if self.attack_stack > 0:
                        self.players[0].add_multiple_cards(self.attack_stack)
                        self.attack_stack = 0
                    else:
                        self.players[0].add_one_card()
                    self.next_player()
                elif SCREEN_HEIGHT - CARD_HEIGHT <= y <= SCREEN_HEIGHT and len(self.players[0].hand) > 0:
                    index = x // CARD_WIDTH
                    if index < len(self.players[0].hand):
                        card = self.players[0].hand[index]
                        if self.check_playable_cards(card):
                            self.players[0].play_card(index, self)
                            self.apply_special_rules(card)
                            if self.attack_stack == 0 or card.value not in [2, 3, 13]:
                                self.next_player()
                        else:
                            print("You can't use this card: ", card)
            elif self.current_player != 0:
                # Bot move
                bot = self.players[self.current_player]
                index = bot.choose_card(
                    self.current_card, self.attack_stack, self)
                if index is not None:
                    card = bot.hand[index]
                    bot.play_card(index, self)
                    self.apply_special_rules(card)
                    if self.attack_stack == 0 or card.value not in [2, 3, 13]:
                        self.next_player()
                else:
                    if self.attack_stack > 0:
                        bot.add_multiple_cards(self.attack_stack)
                        self.attack_stack = 0
                    else:
                        bot.add_one_card()
                    self.next_player()

    def game_over(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.draw_all_cards_and_table()

    def run(self):
        while True:
            self.event_handler()
            self.draw_all_cards_and_table()
            pygame.display.flip()


# Start the game
game = Game()
game.run()
