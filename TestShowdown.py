from unittest import TestCase
import unittest
from Showdown import Showdown
import random
from Player import Player, Card, BoardScore
import itertools


class TestShowdown(TestCase):

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
        pass

    def test_is_pair1(self):
        # Test if method detects pair
        gen = [Card(2, 1), Card(3, 1), Card(3, 1), Card(4, 1), Card(5, 1), Card(12, 1), Card(9, 4)]
        s = Showdown(None, None)
        self.assertEqual((True, [3,3,12,9,5]), s.is_pair(gen))

    def test_is_pair2(self):
        # Test if method detects no pair
        gen = [Card(2, 1), Card(3, 4), Card(6, 1), Card(4, 2), Card(5, 1), Card(8, 2), Card(10,1)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_pair(gen))

    def test_is_pair3(self):
        # Test if method detects pair
        gen = [Card(2, 1), Card(5, 3), Card(4, 3), Card(7, 4), Card(4, 2), Card(10,2), Card(11,3)]
        s = Showdown(None, None)
        self.assertEqual((True, [4,4,11,10,7]), s.is_pair(gen))

    def test_is_two_pair1(self):
        # Test if method detects 2 pair
        gen = [Card(14, 3), Card(3, 2), Card(3, 4), Card(4, 2), Card(14, 3), Card(6, 1), Card(7,2)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 3, 3, 7]), s.is_two_pair(gen))

    def test_is_two_pair2(self):
        # Test if method detects no 2 pair
        gen = [Card(14, 3), Card(3, 2), Card(3, 4), Card(4, 2), Card(13, 3), Card(2, 4), Card(6, 2)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_two_pair(gen))

    def test_is_two_pair3(self):
        # Test if method detects 2 pair in four of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 4), Card(13, 3), Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 14, 14, 13]), s.is_two_pair(gen))

    def test_is_two_pair4(self):
        # Test if method detects 2 pair in full house
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(13, 3), Card(2,2), Card(3,3)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 13, 13, 14]), s.is_two_pair(gen))

    def test_is_two_pair5(self):
        # Test if method detects 2 pair
        gen = [Card(14, 1), Card(4, 2), Card(8, 4), Card(3, 2), Card(3, 3), Card(6, 3), Card(12, 2)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_two_pair(gen))

    def test_is_two_pair6(self):
        # Test if method detects 2 pair with 3 of a kind
        gen = [Card(14, 3), Card(14, 2), Card(2, 1), Card(8, 4), Card(3, 3), Card(2,2), Card(8, 1)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 8, 8, 3]), s.is_two_pair(gen))

    def test_is_three_kind(self):
        # Test if method detects three of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(12, 3), Card(2, 2), Card(3,3)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 14, 13, 12]), s.is_three_kind(gen))

    def test_is_three_kind2(self):
        # Test if method detects no three of a kind
        gen = [Card(2, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(12, 3), Card(13, 2), Card(2, 1)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_three_kind(gen))

    def test_is_three_kind3(self):
        # Test if method detects three of a kind from four kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 4), Card(12, 3), Card(2,2), Card(3,3)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 14, 14, 12]), s.is_three_kind(gen))

    def test_is_straight1(self):
        # Test if method detects straight
        gen = [Card(5, 3), Card(7, 2), Card(6, 1), Card(8, 4), Card(4, 3), Card(9, 1), Card(11, 3)]
        s = Showdown(None, None)
        self.assertEqual((True, [9, 8, 7, 6, 5]), s.is_straight(gen))

    def test_is_straight2(self):
        # Test if method detects no straight
        gen = [Card(7, 3), Card(7, 2), Card(6, 1), Card(5, 4), Card(4, 3), Card(14, 2), Card(13, 2)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_straight(gen))

    def test_is_straight3(self):
        # Test if method detects edge case of wheel straight
        gen = [Card(5, 3), Card(4, 2), Card(3, 1), Card(2, 4), Card(14, 3), Card(7, 3), Card(9, 1)]
        s = Showdown(None, None)
        self.assertEqual((True, [5, 4, 3, 2, 14]), s.is_straight(gen))

    def test_is_flush(self):
        gen = [Card(5, 3), Card(4, 3), Card(3, 3), Card(14, 3), Card(11, 3), Card(2, 2), Card(13, 2)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 11, 5, 4, 3]), s.is_flush(gen))

    def test_is_flush2(self):
        gen = [Card(5, 2), Card(4, 3), Card(3, 3), Card(14, 3), Card(11, 3), Card(2, 2), Card(6, 4)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_flush(gen))

    def test_is_full_house(self):
        gen = [Card(5, 2), Card(5, 3), Card(14, 3), Card(14, 2), Card(5, 4), Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        self.assertEqual((True, [5, 5, 5, 14, 14]), s.is_full_house(gen))

    def test_is_full_house2(self):
        gen = [Card(5, 2), Card(5, 3), Card(14, 3), Card(11, 2), Card(14, 4), Card(2, 1), Card(2, 2)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_full_house(gen))

    def test_is_full_house3(self):
        # Check if Full house not found in four of a kind
        gen = [Card(5, 2), Card(5, 3), Card(5, 1), Card(5, 4), Card(14, 4), Card(14, 1), Card(14, 2)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 14, 5, 5]), s.is_full_house(gen))

    def test_is_four_kind(self):
        # Test if method detects three of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 4), Card(12, 3), Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 14, 14, 14, 12]), s.is_four_kind(gen))

    def test_is_four_kind2(self):
        # Test if method detects no three of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(12, 3), Card(2, 1), Card(2, 2)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_four_kind(gen))

    def test_is_straight_flush1(self):
        # Test if method detects no straight flush
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 4), Card(12, 3), Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_straight_flush(gen))

    def test_is_straight_flush2(self):
        # Test if method detects straight flush
        gen = [Card(14, 3), Card(11, 3), Card(12, 3), Card(13, 3), Card(10, 3), Card(2, 1), Card(2, 2)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 13, 12, 11, 10]), s.is_straight_flush(gen))

    def test_is_straight_flush3(self):
        # Test if method detects straight flush with 6
        gen = [Card(9, 3), Card(11, 3), Card(12, 3), Card(13, 3), Card(10, 3), Card(14, 3), Card(2, 2)]
        s = Showdown(None, None)
        self.assertEqual((True, [14, 13, 12, 11, 10]), s.is_straight_flush(gen))

    def test_is_straight_flush4(self):
        # Test if method detects no straight flush when straight and flush present
        gen = [Card(9, 3), Card(11, 4), Card(12, 3), Card(13, 3), Card(10, 3), Card(14, 3), Card(2, 2)]
        s = Showdown(None, None)
        self.assertEqual((False, []), s.is_straight_flush(gen))

    # def test_find_possible_combos(self):
    #     gen1 = self.generate_random_cards(11)
    #     players = [Player([gen1[0], gen1[1]]), Player([gen1[2], gen1[3]]), Player([gen1[9], gen1[10]])]
    #     board = [gen1[4], gen1[5], gen1[6], gen1[7], gen1[8]]
    #     s = Showdown(players, board)
    #     combos = s.find_possible_combos(Player([gen1[0], gen1[1]]))
    #     # for x in combos:
    #     #      print(s.retrieve_values(x[0]))
    #     #      print(len(combos))
    #
    # def test_find_best_high_card(self):
    #     gen = [Card(2, 3), Card(3, 2), Card(14, 1), Card(13, 4), Card(12, 3), Card(5, 3), Card(9, 4)]
    #     players = [Player([gen[1], gen[0]])]
    #     board = gen[2:]
    #     s = Showdown(players, board)
    #     self.assertEqual([BoardScore.high_card, 14, 13, 12, 9, 5], s.find_best(players[0]))
    #
    # def test_find_best_pair(self):
    #     gen = [Card(2, 3), Card(3, 2), Card(14, 1), Card(14, 4), Card(12, 3), Card(5, 3), Card(9, 4)]
    #     players = [Player([gen[1], gen[0]])]
    #     board = gen[2:]
    #     s = Showdown(players, board)
    #     self.assertEqual([BoardScore.pair, 14, 13, 12, 9, 0], s.find_best(players[0]))

if __name__ == '__main__':
    unittest.main()
