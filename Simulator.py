from Showdown import Showdown
from Player import Player, Card
import random


class Simulator(object):

    def generate_random_cards(self, num_cards, dead_cards=None):
        deck = []
        random_cards = []
        # Generates entire deck
        for val in range(2, 15):
            for suit in range(1, 5):
                card = Card(val, suit)
                deck.append(card)
        # Removes dead cards
        if dead_cards:
            for c in dead_cards:
                deck.remove(c)
        for i in range(num_cards):
            draw = random.choice(deck)
            random_cards.append(draw)
            deck.remove(draw)
        return random_cards

    # Generates a random 5-card board for the given players
    def generate_random_showdown(self, players):
        dead_cards = [card for player in players for card in player.cards]
        return dead_cards
