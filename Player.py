class Card(object):
    """
    Card class representing each card and suit
    Values:
    2 = 2
    3 = 3
    ...
    10 = 10
    J = 11
    Q = 12
    K = 13
    A = 14
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class Player(object):
    """
    Player class that holds cards and showdown result.

    """
    def __init__(self, cards):
        self.cards = cards
        self.result = Result.loss
        self.best = BoardScore.high_card