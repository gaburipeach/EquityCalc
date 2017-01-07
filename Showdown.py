"""
Showdown

Class representing the hierarchy of 5-card combinations at
showdown for Texas Hold'em Poker.

Takes in an n amount of player's cards and the board state and determines
the winner.

"""
from Player import BoardScore


class Showdown(object):
    """
    Rank class that calculates final showdown rank.

    """
    def __init__(self, players, board):
        # Players is a list of players
        self.players = players
        # Board is a list of cards
        self.board = board
        # Rank is organized as [Best combo, best 5 combos]
        self.rank = []
        self.winners = []

    @classmethod
    def retrieve_values(cls, combo):
        """
        Take in a list of cards and strips the values.
        Then returns the list of values in reverse sorted order.

        """
        combo_values = []
        for card in combo:
            combo_values.append(card.value)
        combo_values.sort(reverse=True)
        return combo_values

    def is_pair(self, combo):
        """
        Finds if five-card combo contains a pair.
        Returns the best 5-card combination with a pair if so.

        """
        combo_values = self.retrieve_values(combo)
        for card in combo_values:
            if combo_values.count(card) == 2:
                combo_values.remove(card)
                combo_values.remove(card)
                return True, [card, card, combo_values[0], combo_values[1],
                              combo_values[2]]
        return False, []

    def is_two_pair(self, combo):
        """
        Finds if five-card combo contains two pairs.
        Returns the best 5-card combination with a two pair if so.

        """
        combo_values = self.retrieve_values(combo)
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

    def is_three_kind(self, combo):
        """
        Finds if five-card combo contains three of a kind.
        Returns the best 5-card combination with a three of a kind if so.

        """
        combo_values = self.retrieve_values(combo)
        for card in combo_values:
            if combo_values.count(card) >= 3:
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                return True, [card, card, card, combo_values[0],
                              combo_values[1]]
        return False, []

    @classmethod
    def is_sequential(cls, sorted_board):
        """
        Checks if the sorted board passed in is sequential.
        Used in is_straight().

        """
        it = (card_val for card_val in sorted_board)
        first = next(it)
        return all(a == b for a, b in enumerate(it, first + 1))

    def is_straight(self, combo, straight_flush=None):
        """
        Checks if 5-card combo contains a straight.
        Returns the best 5-card combination with a straight if so.

        """
        if not straight_flush:
            sorted_values = self.retrieve_values(combo)
        else:
            sorted_values = combo
        sorted_values.reverse()
        # This loop is weird because we account for straight-flush case with
        # the optional argument
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
        Returns the best 5-card combination with a flush if so.

        """
        suit_count = [0, 0, 0, 0]
        for card in combo:
            suit_count[card.suit-1] += 1
        f_suit = None
        for i in range(4):
            if suit_count[i] >= 5:
                f_suit = i+1
        if not f_suit:
            return False, []
        ans = []
        for card in combo:
            if card.suit == f_suit:
                ans.append(card)
        ans = self.retrieve_values(ans)
        return True, ans[:min([num, len(ans)])]

    def is_full_house(self, combo):
        """
        Finds if five-card combo contains a full house.
        Returns the best 5-card combination with a full house if so.

        """
        combo_values = self.retrieve_values(combo)
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
                    return True, [three_of_kind_card, three_of_kind_card,
                                  three_of_kind_card, card, card]
        return False, []

    def is_four_kind(self, combo):
        """
        Finds if five-card combo contains four of a kind.
        Returns the best 5-card combination with a four of a kind if so.

        """
        combo_values = self.retrieve_values(combo)
        for card in combo_values:
            if combo_values.count(card) == 4:
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                combo_values.remove(card)
                return True, [card, card, card, card, combo_values[0]]
        return False, []

    def is_straight_flush(self, combo):
        """
        Finds if five-card combo contains a straight flush.
        Returns the best 5-card combination with a pair if so.

        """
        flush_list = self.is_flush(combo, 7)[1]
        if len(flush_list) >= 5:
            return self.is_straight(flush_list, 1)
        return False, []

    def find_best(self, participant):
        """
        Finds the best five-card combination for each player.

        """
        # best represents [BoardScore, Best 5 cards]
        best = [BoardScore.high_card, 0, 0, 0, 0, 0]
        combo = participant.cards + self.board
        current_hand = self.is_straight_flush(combo)
        if current_hand[0]:
            best = [BoardScore.straight_flush] + current_hand[1]
            return best
        current_hand = self.is_four_kind(combo)
        if current_hand[0]:
            best = [BoardScore.four_kind] + current_hand[1]
            return best
        current_hand = self.is_full_house(combo)
        if current_hand[0]:
            best = [BoardScore.full_house] + current_hand[1]
            return best
        current_hand = self.is_flush(combo)
        if current_hand[0]:
            best = [BoardScore.flush] + current_hand[1]
            return best
        current_hand = self.is_straight(combo)
        if current_hand[0]:
            best = [BoardScore.straight] + current_hand[1]
            return best
        current_hand = self.is_three_kind(combo)
        if current_hand[0]:
            best = [BoardScore.three_kind] + current_hand[1]
            return best
        current_hand = self.is_two_pair(combo)
        if current_hand[0]:
            best = [BoardScore.two_pair] + current_hand[1]
            return best
        current_hand = self.is_pair(combo)
        if current_hand[0]:
            best = [BoardScore.pair] + current_hand[1]
            return best
        # Find the best high-card combination
        high_card_values = self.retrieve_values(participant.cards + self.board)
        best[1:] = high_card_values[:5]
        return best

    def find_winners(self):
        """
        Find the player with the best hand.
        Updates rank variable to hold the best hand and the winners list
        with the winning player.

        """
        best_hands = [(None, [0, 0, 0, 0, 0, 0])]
        for participant in self.players:
            current_hand = self.find_best(participant)
            if set(current_hand).issubset(best_hands[0][1]):
                best_hands.append((participant, current_hand))
                continue
            for i in range(6):
                if current_hand[i] >= best_hands[0][1][i]:
                    best_hands = [(participant, current_hand)]
                    break
                else:
                    break

        for hand in best_hands:
            self.winners.append(hand[0])
        self.rank = best_hands[0][1]

