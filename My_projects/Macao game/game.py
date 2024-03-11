import sys
import pygame
from player import Player
from bot import Bot
from deck import Deck

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
NUM_PLAYERS = 1

# clock refreshment of game and framerate
clock = pygame.time.Clock()
framerate = 60


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


# the class which will be steering the whole game
class Game:
    def __init__(self):
        self.deck = Deck()
        self.current_card = self.deck.draw_card()
        self.players = [Player(i, self.deck) for i in range(NUM_PLAYERS)]
        for player in self.players:
            player.draw_hand()

        self.current_player = 0

        # direction of play (1 = clockwise, -1 = anticlockwise)
        self.direction = 1

    def next_player(self):
        self.current_player = (self.current_player +
                               self.direction) % NUM_PLAYERS

    def draw_all_cards_and_table(self):
        # fill all the screen with white color - our table
        screen.fill(WHITE)

        # draw the current card on the middle
        self.current_card.draw(
            SCREEN_WIDTH // 2 - CARD_WIDTH // 2, SCREEN_HEIGHT // 2 - CARD_HEIGHT // 2)

        # draw the back of the card in the middle to take if your cards doesn't match
        # self.deck.draw_card()

        # draw the card on your hand
        for i, card in enumerate(self.players[0].hand):
            card.draw(i * CARD_WIDTH, SCREEN_HEIGHT - CARD_HEIGHT)

    # the method which checking if you can play the card on current card
    def check_playable_cards(self, card):
        return card.suit == self.current_card.suit or card.value == self.current_card.value

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.current_player == 0:
                    x, y = pygame.mouse.get_pos()
                    if SCREEN_HEIGHT - CARD_HEIGHT <= y <= SCREEN_HEIGHT and len(self.players[0].hand) > 0:
                        index = x // CARD_WIDTH
                        print(index)
                        if index < len(self.players[0].hand):
                            card = self.players[0].hand[index]
                            print(card)
                            print(self.current_card)
                            # if len(self.players) > 0:
                            if self.check_playable_cards(card):
                                self.players[0].play_card(index, self)
                                self.next_player()
                            else:
                                # TODO: dobieranie z środka kart
                                print("You can't use this card: ", card)
                                self.players[0].add_one_card()
                            # else:
                            #     self.game_over()
                # else:  # Sztuczna inteligencja dla pozostałych graczy
                #     self.ai_play(self.players[self.current_player])

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


# Uruchom grę
game = Game()
game.run()
