"""
Showdown

Class representing the hierarchy of 5-card combinations at showdown for Texas Hold'em Poker

Takes in an n amount of player's cards and the board state and determines the winner

"""
from enum import Enum
import itertools
from Player import Player, Card, BoardScore


class Showdown(object):
    """
    Rank class that calculates final showdown rank.

    """

    def __init__(self, players, board):
        # Players is a list of players
        self.players = players
        # Board is a list of cards
        self.board = board
        # Rank is organized as [Best combo, Best Primary, Best Secondary, Kicker]
        self.rank = [BoardScore.high_card, 0, 0, 0, 0, 0]
        self.winners = None

    @classmethod
    def retrieve_values(cls, combo):
        combo_values = []
        for card in combo:
            combo_values.append(card.value)
        return combo_values

    # %%Checked%%
    def is_pair(self, combo):
        """
        Finds if five-card combo contains a pair.
        Returns true if there is at least a pair in the combo.

        """
        combo_values = self.retrieve_values(combo)
        combo_values.sort() #WHOOO
        for card in combo_values:
            if combo_values.count(card) == 2:
                combo_values.remove(card)
                combo_values.remove(card)
                return True, [card, card, combo_values[4], combo_values[3], combo_values[2]]
        return False, []

    # %%Checked%%
    def is_two_pair(self, combo):
        """
        Finds if five-card combo contains two pairs.
        """
        combo_values = self.retrieve_values(combo)
        combo_values.sort() #WHOO
        combo_values.reverse()
        pair1 = None
        pair2 = None
        for card in combo_values:
            if combo_values.count(card) >= 2:
                # Removing while iterating is ok here because there are only 5
                # cards and by removing we skip 1 iteration, so max there will
                # only be 3 cards left and it doesn't matter if we skip 1
                combo_values.remove(card)
                combo_values.remove(card)
                if not pair1:
                    pair1 = card
                else:
                    pair2 = card
                if pair2:
                    if pair1 < pair2:
                        pair1, pair2 = pair2, pair1
                    return True, [pair1, pair1, pair2, pair2, combo_values[0]]
        return False, []

    # %%Checked%%
    def is_three_kind(self, combo):
        """
        Finds if five-card combo contains three of a kind.
        """
        combo_values = self.retrieve_values(combo)
        combo_values.sort() #WHOO
        for card in combo_values:
            if combo_values.count(card) >= 3:
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                return True, [card, card, card, combo_values[3], combo_values[2]]
        return False, []

    @classmethod
    def is_sequential(cls, sorted_board):
        """
        Checks if the sorted board passed in is sequential. Used in is_straight().

        """
        it = (card_val for card_val in sorted_board)
        first = next(it)
        return all(a == b for a, b in enumerate(it, first + 1))

    # %%Checked%%
    def is_straight(self, combo, straight_flush=None):
        """
        Checks if 5-card combo contains a straight.

        """
        # Sorts the list of cards
        if not straight_flush:
            sorted_values = self.retrieve_values(combo)
        else:
            sorted_values = combo
        sorted_values.sort()
        # Checks if list is sequential
        for i in range(len(combo)-5, -1, -1):
            is_seq_straight = self.is_sequential(sorted_values[i:i+5])
            if is_seq_straight:
                ans = sorted_values[i:i+5]
                ans.reverse()
                return True, ans
        # Checks edge case of A2345
        if set([2, 3, 4, 5, 14]).issubset(set(sorted_values)):
            return True, [5, 4, 3, 2, 14]
        return False, []


    def is_flush(self, combo, num=5):
        """
        Checks if 5-card combo contains a flush

        Combo contains a tuple of (board, players).
        Combo[0] contains the board, which contains a list of cards (card, card, card...).

        """
        suit_count = [0, 0, 0, 0]
        for card in combo:
            suit_count[card.suit-1]+=1
        f_suit = None
        for i in range(4):
            if suit_count[i] >= 5:
                f_suit = i+1
        if f_suit == None:
            return False, []
        ans = []
        for card in combo:
            if card.suit == f_suit:
                ans.append(card)
        ans = self.retrieve_values(ans)
        ans.sort()
        ans.reverse()
        return True, ans[:min([num, len(ans)])]


    # %%Checked%%
    def is_full_house(self, combo):
        """
        Finds if five-card combo contains a full house.

        """
        combo_values = self.retrieve_values(combo)
        combo_values.reverse()
        new_combo_values = None
        three_of_kind_card = None
        for card in combo_values:
            if combo_values.count(card) == 3:
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                three_of_kind_card = card
                new_combo_values = combo_values[:]
                break
        if new_combo_values:
            for card in new_combo_values:
                if new_combo_values.count(card) >= 2:
                    return True, [three_of_kind_card, three_of_kind_card, three_of_kind_card, card, card]
        return False, []

    # %%Checked%%
    def is_four_kind(self, combo):
        """
        Finds if five-card combo contains four of a kind.

        """
        combo_values = self.retrieve_values(combo)
        combo_values.sort()
        for card in combo_values:
            if combo_values.count(card) == 4:
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                return True, [card, card, card, card, combo_values[2]]
        return False, []


    def is_straight_flush(self, combo):
        flush_list = self.is_flush(combo, 7)[1]
        if len(flush_list) >= 5:
            return self.is_straight(flush_list, 1)
        return False, []

    # %%Checked%%
    def find_possible_combos(self, hand):
        """
        Finds all possible 5-card combination for each player at showdown

        """
        possible_state = []
        # Adds the player's cards to the possible board combos
        self.board.append(hand.cards[0])
        self.board.append(hand.cards[1])
        # Finds all possible combos for the player
        for possible_board in itertools.combinations(self.board, 5):
            possible_state.append(possible_board)
        # Removes the player's cards to prepare for the next player
        self.board.remove(hand.cards[0])
        self.board.remove(hand.cards[1])
        return possible_state

    @classmethod
    def compare_best(cls, best1, best2):
        """
        Compares the current best with the state's best.
        Returns True if state's best is better, False otherwise.

        """
        for i in range(len(best1)-1, 1, -1):
            if best1[i] > best2[i]:
                return False
        return True

    def find_best(self, hand):
        """
        Finds the best five-card combination for each player.

        """
        # best represents [BoardScore, Primary High, Secondary, Kicker, Kicker2, Kicker3]
        best = [BoardScore.high_card, 0, 0, 0, 0, 0]
        all_states = self.find_possible_combos(hand)
        for state in all_states:
            # Straight-Flush
            # Possibly make each of these methods and implement better control-flow as an optimization.
            state_values = self.retrieve_values(state)
            state_values.sort()
            if self.is_flush(state) and self.is_straight(state):
                if BoardScore.straight_flush == best[0]:
                    if state_values[4] > best[1]:
                        best[1] = state_values[4]
                else:
                    best = [BoardScore.straight_flush, state_values[4], 0, 0, 0, 0]
            # Four of a Kind
            elif self.is_four_kind(state):
                # Determines which value is the Kicker and Which one is the x4.
                if state_values.count(state_values[0]) == 4:
                    primary = state_values[0]
                    kicker = state_values[4]
                else:
                    primary = state_values[4]
                    kicker = state_values[0]
                if BoardScore.four_kind == best[0]:
                    if kicker > best[3]:
                        best[3] = kicker
                else:
                    best = [BoardScore.four_kind, primary, 0, kicker, 0, 0]
            # Full House
            elif self.is_full_house(state):
                if state_values.count(state_values[0]) == 3:
                    primary = state_values[0]
                    secondary = state_values[4]
                else:
                    primary = state_values[4]
                    secondary = state_values[0]
                if BoardScore.full_house == best[0] and primary > best[1]:
                    if secondary > best[2]:
                        best[2] = secondary
                else:
                    best = [BoardScore.full_house, primary, secondary, 0, 0, 0]
            # Flush
            elif self.is_flush(state):
                if not self.compare_best(best[1:], state_values):
                    best = [BoardScore.flush] + state_values
            # Straight
            elif self.is_straight(state):
                if BoardScore.straight == best[0]:
                    if state_values[4] > best[1]:
                        best[1] = state_values[4]
                else:
                    best = [BoardScore.straight_flush, state_values[4], 0, 0, 0, 0]
            # 2-Pair
            elif self.is_two_pair(state):
                pair1, pair2, kicker = 0, 0, 0
                if state_values.count(state_values[0]) >= 2:
                    pair1 = state_values[0]
                    state_values.remove(state_values[0])
                    state_values.remove(state_values[0])
                    new_state_values = state_values[:]
                    if new_state_values.count(new_state_values[0]) >= 2:
                        pair2 = 0
                        new_state_values.remove(new_card)
                        new_state_values.remove(new_card)
                        kicker = new_state_values[0]
                else:
                    kicker = state_values[0]
                    pair1 = state_values[1]
                    state_values.remove(state_values[1])
                    state_values.remove(state_values[1])
                    pair2 = state_values[1]
                if pair2 > pair1:
                    pair1, pair2 = pair2, pair1
                # if BoardScore.two_pair == best[0]:
                #     if pair1 > best[1]:
                #         best[2] = pair2
                #         best[3] = kicker
                #     # If top pair is equal
                #     elif pair1 == best[1]:
                #         if pair2 > best[2]:
                #             best[3] = kicker
                #             best[2] = pair2
                #         elif pair2 == best[2] and kicker > best[3]:
                #             best[3] = kicker
                #             best[2] = pair2
                #         best[1] = pair1
                # This woks because we never compare better than 2pair with this
                if BoardScore.pair == best[0] and not self.compare_best(best[1:], [pair1, pair2, kicker, 0, 0]):
                    pass
                else:
                    best = [BoardScore.two_pair, pair1, pair2, kicker, 0, 0]
            # 1-pair
            elif self.is_pair(state):
                pair1, kicker1, kicker2, kicker3 = 0, 0, 0, 0
                for card in state_values:
                    if state_values.count(card) == 2:
                        pair1 = card
                        break
                state_values.remove(pair1)
                state_values.remove(pair1)
                kicker1 = state_values[2]
                kicker2 = state_values[1]
                kicker3 = state_values[0]
                if BoardScore.pair == best[0] and not self.compare_best(best[1:],
                                                                        [pair1, kicker1, kicker2, kicker3, 0]):
                    pass
                else:
                    best = [BoardScore.pair, pair1, kicker1, kicker2, kicker3, 0]
            else:
                state_values.reverse()
                if self.compare_best(best[1:], state_values):
                    best[1:] = state_values
        return best
