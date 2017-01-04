"""
Showdown

Class representing the hierarchy of 5-card combinations at showdown for Texas Hold'em Poker

Takes in an n amount of player's cards and the board state and determines the winner

"""
from enum import Enum
import itertools
from Player import Player, Card


class Result(Enum):
    """
    Enumeration for Showdown result.
    """
    loss, win, tie = range(3)


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


class Showdown(object):
    """
    Rank class that calculates final showdown rank.

    """
    def __init__(self, players, board):
        self.players = players
        self.board = board
        # Rank is organized as (Best combo, Best Primary, Best Secondary, Kicker)
        self.rank = (BoardScore.high_card, None, None, 8)
        self.winners = None

    @classmethod
    def is_pair(cls, combo):
        """
        Finds if five-card combo contains a pair.

        """
        # IMPORTANT WHAT IS COMBO????
        for card in combo:
            if combo.count(card) == 2:
                return True
        return False

    @classmethod
    def is_two_pair(cls, combo):
        """
        Finds if five-card combo contains two pairs.
        """
        for card in combo:
            if combo.count(card) == 2:
                combo.remove(card)
                combo.remove(card)
                new_combo = combo[:]
                for new_card in new_combo:
                    if new_combo.count(new_card) == 2:
                        return True
                return False
        return False

    @classmethod
    def is_three_kind(cls, combo):
        """
        Finds if five-card combo contains three of a kind.
        """
        for card in combo:
            if combo.count(card) == 3:
                return True
        return False

    @classmethod
    def is_sequential(cls, sorted_board):
        """
        Checks if the sorted board passed in is sequential. Used in is_straight().

        """
        it = (card_val for card_val in sorted_board)
        first = next(it)
        return all(a == b for a, b in enumerate(it, first+1))

    @classmethod
    def is_straight(cls, combo):
        """
        Checks if 5-card combo contains a straight.

        """
        # Sorts the list of cards
        sorted_values = []
        for card in combo:
            sorted_values += card.value
        sorted_values.sort()
        # Checks if list is sequential
        is_seq_straight = cls.is_sequential(sorted_values)
        # Checks edge case of A2345
        if sorted_values == [1, 2, 3, 4, 14]:
            is_seq_straight = True
        return is_seq_straight

    @classmethod
    def is_flush(cls, combo):
        """
        Checks if 5-card combo contains a flush

        Combo contains a tuple of (board, players).
        Combo[0] contains the board, which contains a list of cards (card, card, card...).

        """
        if (combo[0][0].suit == combo[0][1].suit and combo[0][0].suit == combo[0][2].suit and
                    combo[0][0].suit == combo[0][3].suit and combo[0[0]] == combo[0][4]):
            return True
        return False

    @classmethod
    def is_full_house(cls, combo):
        """
        Finds if five-card combo contains a full house.

                return True
        return False

        """
        for card in combo:
            if combo.count(card) == 3:
                combo.remove(card)
                combo.remove(card)
                combo.remove(card)
                if combo[0] == combo[1]:
                    return True
            return False
        return False

    @classmethod
    def is_four_kind(cls, combo):
        """
        Finds if five-card combo contains four of a kind.

        """
        for card in combo:
            if combo.count(card) == 4:
                return True
        return False

    def find_possible_combos(self):
        """
        Finds all possible 5-card combination for each player at showdown

        """
        for player in self.players:
            # Adds the player's cards to the possible board combos
            self.board.append(player.cards[0])
            self.board.append(player.cards[1])
            # Finds all possible combos for the player
            for possible_board in itertools.combinations(self.board, 5):
                yield (possible_board, player)
            # Removes the player's cards to prepare for the next player
            self.board.remove(player.cards[0])
            self.board.remove(player.cards[1])

    def find_best(self):
        """
        Finds the best five-card combination.

        """
        all_combos = self.find_possible_combos()
        for combo in all_combos:
            if self.is_straight(combo[0]) and self.is_flush(combo[0]):
                combo[1].best = BoardScore.straight_flush
            # 3 Different types of hands
            # Flushes, Straights, and Pairs
            # Check Flush
