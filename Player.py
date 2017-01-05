from enum import Enum


class Result(Enum):
    """
    Enumeration for Showdown result.
    """
    loss, win, tie = range(3)


class Card(object):
    """
    Card class representing each card and suit

    Card Values:
    2 = 2
    3 = 3
    ...
    10 = 10
    J = 11
    Q = 12
    K = 13
    A = 14

    Suit Values:
    1 = Diamonds
    2 = Clubs
    3 = Hearts
    4 = Spades
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class BoardScore(Enum):
    """
    Enumeration for board combination scores.
    """
    high_card = 0
    pair = 1
    two_pair = 2
    three_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_kind = 7
    straight_flush = 8


class Player(object):
    """
    Player class that holds cards and showdown result.

    """

    def __init__(self, cards):
        self.cards = cards
        self.result = Result.loss
        self.best = [BoardScore.high_card, None, None, 8]
