import random
import copy
from player import Player
from simplified_game import SimplifiedGame


class Bot(Player):
    def __init__(self, player_id, deck):
        super().__init__(player_id, deck)

    def choose_card(self, current_card, attack_stack, game):
        best_move = self.mcts(current_card, attack_stack, game)
        return best_move

    def mcts(self, current_card, attack_stack, game, simulations=1000):
        possible_moves = []
        for i, card in enumerate(self.hand):
            if game.check_playable_cards(card):
                possible_moves.append((i, card))

        if not possible_moves:
            return None

        move_scores = {move: 0 for move in possible_moves}

        for _ in range(simulations):
            for move in possible_moves:
                index, card = move
                game_copy = SimplifiedGame(
                    game.current_card, game.players, game.current_player, game.attack_stack, game.deck)
                self.simulate_move(game_copy, index, card)
                move_scores[move] += self.simulate_game(game_copy)

        best_move = max(move_scores, key=move_scores.get)
        return best_move[0]

    def simulate_move(self, game, index, card):
        game.players[game.current_player].hand.pop(index)
        game.current_card = card
        game.apply_special_rules(card)
        game.add_to_discard_pile(card)

    def simulate_game(self, game):
        while True:
            current_player = game.players[game.current_player]
            if isinstance(current_player, Bot):
                index = current_player.choose_card(
                    game.current_card, game.attack_stack, game)
                if index is not None:
                    card = current_player.hand[index]
                    current_player.play_card(index, game)
                    game.apply_special_rules(card)
                    game.add_to_discard_pile(card)
                else:
                    if game.attack_stack > 0:
                        current_player.add_multiple_cards(game.attack_stack)
                        game.attack_stack = 0
                    else:
                        current_player.add_one_card()
            else:
                break
            game.next_player()
            if len(current_player.hand) == 0:
                return 1 if isinstance(current_player, Bot) else -1
        return 0
