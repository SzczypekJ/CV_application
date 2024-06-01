from deck import Deck


class Player:
    def __init__(self, player_id, deck):
        self.hand = []
        self.player_id = player_id
        self.deck = deck
    
    # adding the card to the hand of player
    def add_one_card(self):
        self.hand.append(self.deck.draw_card())
        
    
    def add_multiple_cards(self, count):
        for _ in range(count):
            self.hand.append(self.deck.draw_card())

    # adding five cards at the start of the game
    def draw_hand(self):
        for _ in range(5):
            self.hand.append(self.deck.draw_card())

    # playing the card which has an index and telling the game that now this card is our current card
    def play_card(self, index, game):
        card = self.hand.pop(index)
        game.current_card = card
        
    def copy(self):
        new_player = Player(self.player_id, self.deck)
        new_player.hand = self.hand[:]
        return new_player