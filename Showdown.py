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

    def update_board(self, board):
        self.board = board

    @classmethod
    def retrieve_values(cls, combo):
        """
        Take in a list of cards and strips the values.
        Then returns the list of values in reverse sorted order.
        """
        # combo_values = []
        combo.sort(key=lambda x: x.value, reverse=True)
        # for card in combo:
        #     combo_values.append(card.value)
        # combo_values.sort(reverse=True)
        return combo

    def is_pair(self, combo):
        """
        Finds if five-card combo contains a pair.
        Returns the best 5-card combination with a pair if so.
        """
        # combo_values = self.retrieve_values(combo)
        # for card in combo_values:
        #     if combo_values.count(card) == 2:
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         return True, [card, card, combo_values[0], combo_values[1],
        #                       combo_values[2]]
        # return False, []

        size = len(combo)
        i = 0
        while i < size-1:
            if combo[i].value == combo[i+1].value:
                j = min(i, 3)
                left = [card.value for card in combo[0:j]]
                right = [card.value for card in combo[j+2:max(j+2, 5)]]
                return True, [combo[i].value, combo[i+1].value] + left + right
            i+=1
        return False, []

    def is_two_pair(self, combo):
        """
        Finds if five-card combo contains two pairs.
        Returns the best 5-card combination with a two pair if so.
        """
        # combo_values = self.retrieve_values(combo)
        # pair1 = None
        # pair2 = None
        # for card in combo_values:
        #     if combo_values.count(card) >= 2:
        #         # Removing while iterating is ok here because there are only 5
        #         # cards and by removing we skip 1 iteration, so max there will
        #         # only be 3 cards left and it doesn't matter if we skip 1
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         if not pair1:
        #             pair1 = card
        #         else:
        #             pair2 = card
        #         if pair2:
        #             if pair1 < pair2:
        #                 pair1, pair2 = pair2, pair1
        #             return True, [pair1, pair1, pair2, pair2, combo_values[0]]
        # return False, []

        pair1 = None
        pair2 = None
        size = len(combo)
        i = 0
        while i < size-1:
            if combo[i].value == combo[i+1].value:
                # Removing while iterating is ok here because there are only 5
                # cards and by removing we skip 1 iteration, so max there will
                # only be 3 cards left and it doesn't matter if we skip 1
                if not pair1:
                    pair1 = i+1
                else:
                    pair2 = i
                if pair2:
                    k = 0
                    if pair1 == 1:
                        k += 2
                        if pair2 == 2:
                            k += 2
                    return True, [combo[pair1].value, combo[pair1].value, combo[pair2].value, combo[pair2].value, combo[k].value]
                i += 1
            i+=1
        return False, []

    def is_three_kind(self, combo):
        """
        Finds if five-card combo contains three of a kind.
        Returns the best 5-card combination with a three of a kind if so.
        """
        # combo_values = self.retrieve_values(combo)
        # for card in combo_values:
        #     if combo_values.count(card) >= 3:
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         return True, [card, card, card, combo_values[0],
        #                       combo_values[1]]
        # return False, []

        # size = len(combo)
        # i = 0
        # while i < size-2:
        #     if combo[i].value == combo[i+1].value and combo[i+1].value == combo[i+2].value:
        #         j = min(i, 2)
        #         left = [card.value for card in combo[0:j]]
        #         right = [card.value for card in combo[j+3:max(j+3, 5)]]
        #         return True, [combo[i].value, combo[i+1].value, combo[i+2].value] + left + right
        #     i+=1
        # return False, []

        size = len(combo)
        i = 0
        while i < size-2:
            if combo[i].value == combo[i+1].value:
                i += 1
                if combo[i].value == combo[i+1].value:
                    j = min(i-1, 2)
                    left = [card.value for card in combo[0:j]]
                    right = [card.value for card in combo[j+3:max(j+3, 5)]]
                    return True, [combo[i].value, combo[i].value, combo[i].value] + left + right
            i+=1
        return False, []

    @classmethod
    def is_sequential(cls, sorted_board):
        """
        Checks if the sorted board passed in is sequential.
        Used in is_straight().
        """
        it = (card.value for card in sorted_board)
        first = next(it)
        return all(first-a == b for a, b in enumerate(it, 1))

    def is_straight(self, combo):
        """
        Checks if 5-card combo contains a straight.
        Returns the best 5-card combination with a straight if so.
        """
        # if not straight_flush:
        #     sorted_values = self.retrieve_values(combo)
        # else:
        #     sorted_values = combo
        # sorted_values.reverse()
        # # This loop is weird because we account for straight-flush case with
        # # the optional argument
        # for i in range(len(combo)-5, -1, -1):
        #     is_seq_straight = self.is_sequential(sorted_values[i:i+5])
        #     if is_seq_straight:
        #         ans = sorted_values[i:i+5]
        #         ans.reverse()
        #         return True, ans
        # # Checks edge case of A2345
        # if {2, 3, 4, 5, 14}.issubset(set(sorted_values)):
        #     return True, [5, 4, 3, 2, 14]
        # return False, []

        # size = len(combo)-4
        # for i in range(size):
        #     is_seq_straight = self.is_sequential(combo[i:i+5])
        #     if is_seq_straight:
        #         ans = [card.value for card in combo[i:i+5]]
        #         return True, ans
        # # Checks edge case of A2345
        # cards = [card.value for card in combo]
        # if {2, 3, 4, 5, 14}.issubset(set(cards)):
        #     return True, [5, 4, 3, 2, 14]
        # return False, []

        if self.is_sequential(combo[2:5]):
            run = 3
            size = len(combo)-5
            if combo[1].value-1 == combo[2].value:
                run += 1
                if combo[0].value-1 == combo[1].value:
                    return True, [card.value for card in combo[0:5]]
            for i in range(size):
                i += 1
                if combo[4].value == combo[4+i].value+i:
                    run += 1
                else:
                    break
                if run >= 5:
                    ans = [card.value for card in combo[i:i+5]]
                    return True, ans
        # Checks edge case of A2345
        cards = [card.value for card in combo]
        if {2, 3, 4, 5, 14}.issubset(set(cards)):
            return True, [5, 4, 3, 2, 14]
        return False, []


    def is_flush(self, combo, num=5, straight_flush=False):
        """
        Checks if 5-card combo contains a flush
        Returns the best 5-card combination with a flush if so.
        """
        suit_count = [[], [], [], []]
        for card in combo:
            suit_count[card.suit-1].append(card.value) if not straight_flush\
                else suit_count[card.suit-1].append(card)
        f_suit = None
        for i in range(4):
            if len(suit_count[i]) >= 5:
                f_suit = i+1
                break
        if not f_suit:
            return False, []
        return True, suit_count[f_suit-1][:min(num, len(suit_count[f_suit-1]))]

    def is_full_house(self, combo):
        """
        Finds if five-card combo contains a full house.
        Returns the best 5-card combination with a full house if so.
        """
        # combo_values = self.retrieve_values(combo)
        # new_combo_values = None
        # three_of_kind_card = None
        # for card in combo_values:
        #     if combo_values.count(card) == 3:
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         three_of_kind_card = card
        #         new_combo_values = combo_values[:]
        #         break
        # if new_combo_values:
        #     for card in new_combo_values:
        #         if new_combo_values.count(card) >= 2:
        #             return True, [three_of_kind_card, three_of_kind_card,
        #                           three_of_kind_card, card, card]
        # return False, []

        three_of_kind = None
        pair = None
        # f_pair = None
        size = len(combo)
        i = 0
        while i < size-1:
            # if pair == combo[i+1].value and not three_of_kind:
            #     three_of_kind = pair
            # if combo[i].value == combo[i+1].value:
            #     if not three_of_kind or three_of_kind == f_pair:
            #         f_pair = pair
            #     pair = combo[i].value
            # if f_pair and three_of_kind and (f_pair != three_of_kind):
            #    return True, [three_of_kind, three_of_kind, three_of_kind, f_pair, f_pair]
            if i < size-2:
                if not three_of_kind and combo[i].value == combo[i+1].value and combo[i+1].value == combo[i+2].value:
                    three_of_kind = combo[i].value
            if (not pair or pair == three_of_kind) and combo[i].value == combo[i+1].value:
                pair = combo[i].value
            if pair is not None and three_of_kind is not None and pair != \
                    three_of_kind:
                return True, [three_of_kind, three_of_kind, three_of_kind, pair, pair]
            i+=1
        return False, []

    def is_four_kind(self, combo):
        """
        Finds if five-card combo contains four of a kind.
        Returns the best 5-card combination with a four of a kind if so.
        """
        # combo_values = self.retrieve_values(combo)
        # for card in combo_values:
        #     if combo_values.count(card) == 4:
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         combo_values.remove(card)
        #         return True, [card, card, card, card, combo_values[0]]
        # return False, []

        size = len(combo)
        i = 0
        while i < size-3:
            if combo[i].value == combo[i+3].value:
                top = combo[4].value if i == 0 else combo[0].value
                four_kind = combo[i].value
                return True, [four_kind, four_kind, four_kind, four_kind, top]
            i += 1
        return False, []

    def is_straight_flush(self, combo):
        """
        Finds if five-card combo contains a straight flush.
        Returns the best 5-card combination with a pair if so.
        """
        flush_list = self.is_flush(combo, 7, True)
        if flush_list[0]:
            return self.is_straight(flush_list[1])
        return False, []

    def find_best(self, participant):
        """
        Finds the best five-card combination for each player.
        """
        # best represents [BoardScore, Best 5 cards]
        best = [BoardScore.high_card, 0, 0, 0, 0, 0]
        combo = participant.cards + self.board
        combo = self.retrieve_values(combo)

        # current_hand = self.is_straight_flush(combo)
        # if current_hand[0]:
        #     best = [BoardScore.straight_flush] + current_hand[1]
        #     return best
        # current_hand = self.is_four_kind(combo)
        # if current_hand[0]:
        #     best = [BoardScore.four_kind] + current_hand[1]
        #     return best
        # current_hand = self.is_full_house(combo)
        # if current_hand[0]:
        #     best = [BoardScore.full_house] + current_hand[1]
        #     return best
        # current_hand = self.is_flush(combo)
        # if current_hand[0]:
        #     best = [BoardScore.flush] + current_hand[1]
        #     return best
        # current_hand = self.is_straight(combo)
        # if current_hand[0]:
        #     best = [BoardScore.straight] + current_hand[1]
        #     return best
        # current_hand = self.is_three_kind(combo)
        # if current_hand[0]:
        #     best = [BoardScore.three_kind] + current_hand[1]
        #     return best
        # current_hand = self.is_two_pair(combo)
        # if current_hand[0]:
        #     best = [BoardScore.two_pair] + current_hand[1]
        #     return best
        # current_hand = self.is_pair(combo)
        # if current_hand[0]:
        #     best = [BoardScore.pair] + current_hand[1]
        #     return best

        current_hand = self.is_flush(combo, 7, True)
        if current_hand[0]:
            new_hand = self.is_straight(current_hand[1])
            if new_hand[0]:
                best = [BoardScore.straight_flush] + new_hand[1]
                return best
            else:
                # Impossible to have 4-kind with Flush
                # Impossible to have Full house with Flush
                best = [BoardScore.flush] + [card.value for card in current_hand[1][:5]]
                return best
        current_hand = self.is_straight(combo)
        if current_hand[0]:
            best = [BoardScore.straight] + current_hand[1]
            return best
        current_hand = self.is_pair(combo)
        if current_hand[0]:
            new_hand1 = self.is_three_kind(combo)
            if new_hand1[0]:
                new_hand2 = self.is_four_kind(combo)
                if new_hand2[0]:
                    best = [BoardScore.four_kind] + new_hand2[1]
                    return best
                new_hand2 = self.is_full_house(combo)
                if new_hand2[0]:
                    best = [BoardScore.full_house] + new_hand2[1]
                    return best
                best = [BoardScore.three_kind] + new_hand1[1]
                return best
            new_hand1 = self.is_two_pair(combo)
            if new_hand1[0]:
                best = [BoardScore.two_pair] + new_hand1[1]
                return best
            best = [BoardScore.pair] + current_hand[1]
            return best
        # Find the best high-card combination
        high_card_values = [card.value for card in combo]
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
                if current_hand[i] > best_hands[0][1][i]:
                    best_hands = [(participant, current_hand)]
                    break
                elif current_hand[i] == best_hands[0][1][i]:
                    continue
                else:
                    break

        for hand in best_hands:
            self.winners.append(hand[0])
        self.rank = best_hands[0][1]
