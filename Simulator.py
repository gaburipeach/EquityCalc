from Showdown import Showdown
from Player import Player, Card
import random
from itertools import combinations
import time


class Simulator(object):

    def generate_random_cards(self, num_cards, deck):
        random_cards = []
        random_cards_tuple = []
        # random.shuffle(deck)
        # for card in deck[0:num_cards]:
        #     random_cards.append(Card(card[0], card[1]))
        # return random_cards
        for i in range(num_cards):
            draw = random.choice(deck)
            random_cards_tuple.append(draw)
            deck.remove(draw)
        for card in random_cards_tuple:
            random_cards.append(Card(card[0], card[1]))
        return random_cards

    # Generates a random 5-card board for the given players
    # Add Dead-Card optional variable that allows users to input 0-5 cards
    def generate_random_showdown(self, players):
        dead_cards = [card for player in players for card in player.cards]
        winner_tally = [0] * len(players)
        simulations = 100000
        deck = []
        # Generates entire deck
        for val in range(2, 15):
            for suit in range(1, 5):
                deck.append((val, suit))
        # Removes dead cards
        if dead_cards:
            for c in dead_cards:
                deck.remove((c.value, c.suit))
        for i in range(simulations):
            board = self.generate_random_cards(5, deck)
            for card in board:
                deck.append((card.value, card.suit))
            s = Showdown(players, board)
            s.find_winners()
            for winner in s.winners:
                winner_tally[players.index(winner)] += 1
        split = (sum(winner_tally) - simulations)/len(winner_tally)
        winner_tally = [(winner_tally[i] - split)/simulations for i in range(len(
            winner_tally))]
        return winner_tally
