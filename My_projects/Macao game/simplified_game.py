class SimplifiedGame:
    def __init__(self, current_card, players, current_player, attack_stack, deck):
        self.current_card = current_card
        self.players = [player.copy() for player in players]
        self.current_player = current_player
        self.attack_stack = attack_stack
        self.deck = deck.copy()

    def next_player(self):
        self.current_player = (self.current_player + 1) % len(self.players)

    def copy(self):
        return SimplifiedGame(self.current_card, self.players, self.current_player, self.attack_stack, self.deck)

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

    def add_to_discard_pile(self, card):
        self.deck.discard_pile.append(card)
