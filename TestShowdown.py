from unittest import TestCase
import unittest
from Showdown import Showdown
from Player import Player, Card, BoardScore


class TestShowdown(TestCase):

    def test_retrieve_values(self):
        # Test if method detects pair
        gen = [Card(2, 1), Card(3, 1), Card(3, 1), Card(4, 1), Card(5, 1),
               Card(12, 1), Card(9, 4)]
        s = Showdown(None, None)
        self.assertEqual(12, s.retrieve_values(gen)[0].value)

    def test_is_pair1(self):
        # Test if method detects pair
        gen = [Card(2, 1), Card(3, 1), Card(3, 1), Card(4, 1), Card(5, 1),
               Card(12, 1), Card(9, 4)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [3, 3, 12, 9, 5]), s.is_pair(gen))

    def test_is_pair2(self):
        # Test if method detects no pair
        gen = [Card(2, 1), Card(3, 4), Card(6, 1), Card(4, 2), Card(5, 1),
               Card(8, 2), Card(10, 1)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_pair(gen))

    def test_is_pair3(self):
        # Test if method detects pair
        gen = [Card(2, 1), Card(5, 3), Card(11, 3), Card(7, 4), Card(4, 2),
               Card(10, 2), Card(11, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [11, 11, 10, 7, 5]), s.is_pair(gen))

    def test_is_two_pair1(self):
        # Test if method detects 2 pair with highest pair
        gen = [Card(14, 3), Card(3, 2), Card(3, 4), Card(4, 2), Card(14, 3),
               Card(6, 1), Card(7, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 14, 3, 3, 7]), s.is_two_pair(gen))

    def test_is_two_pair2(self):
        # Test if method detects no 2 pair
        gen = [Card(14, 3), Card(3, 2), Card(3, 4), Card(4, 2), Card(13, 3),
               Card(2, 4), Card(6, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_two_pair(gen))

    def test_is_two_pair3(self):
        # Test if method detects 2 pair with high card
        gen = [Card(14, 3), Card(13, 2), Card(2, 1), Card(7, 4), Card(13, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [13, 13, 2, 2, 14]), s.is_two_pair(gen))

    def test_is_two_pair4(self):
        # Test if method detects 2 pair in full house
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(13, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 14, 13, 13, 14]), s.is_two_pair(gen))

    def test_is_two_pair5(self):
        # Test if method detects no 2 pair
        gen = [Card(14, 1), Card(4, 2), Card(8, 4), Card(3, 2), Card(3, 3),
               Card(6, 3), Card(12, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_two_pair(gen))

    def test_is_two_pair6(self):
        # Test if method detects 2 pair for highest 2 pairs
        gen = [Card(14, 3), Card(14, 2), Card(2, 1), Card(8, 4), Card(3, 3),
               Card(2, 2), Card(8, 1)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 14, 8, 8, 3]), s.is_two_pair(gen))

    def test_is_three_kind1(self):
        # Test if method detects three of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(12, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 14, 14, 13, 12]), s.is_three_kind(gen))

    def test_is_three_kind2(self):
        # Test if method detects no three of a kind
        gen = [Card(2, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(12, 3),
               Card(13, 2), Card(2, 1)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_three_kind(gen))

    def test_is_three_kind3(self):
        # Test if method detects three of a kind when there is 1 higher card
        gen = [Card(13, 3), Card(13, 2), Card(13, 1), Card(14, 4), Card(12, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [13, 13, 13, 14, 12]), s.is_three_kind(gen))

    def test_is_three_kind4(self):
        # Test if method detects three of a kind when there are 2 higher card
        gen = [Card(2, 3), Card(12, 2), Card(2, 1), Card(14, 4), Card(13, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [2, 2, 2, 14, 13]), s.is_three_kind(gen))

    def test_is_straight1(self):
        # Test if method detects straight
        gen = [Card(5, 3), Card(7, 2), Card(6, 1), Card(8, 4), Card(4, 3),
               Card(9, 1), Card(11, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [9, 8, 7, 6, 5]), s.is_straight(gen))

    def test_is_straight2(self):
        # Test if method detects no straight
        gen = [Card(7, 3), Card(7, 2), Card(6, 1), Card(5, 4), Card(4, 3),
               Card(14, 2), Card(13, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_straight(gen))

    def test_is_straight3(self):
        # Test if method detects edge case of wheel straight
        gen = [Card(5, 3), Card(4, 2), Card(3, 1), Card(2, 4), Card(14, 3),
               Card(7, 3), Card(9, 1)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [5, 4, 3, 2, 14]), s.is_straight(gen))

    def test_is_flush1(self):
        # Test if method detects flush from 5 flush values
        gen = [Card(5, 3), Card(4, 3), Card(3, 3), Card(14, 3), Card(11, 3),
               Card(2, 2), Card(13, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 11, 5, 4, 3]), s.is_flush(gen))

    def test_is_flush2(self):
        # Test if method detects no flush
        gen = [Card(5, 2), Card(4, 3), Card(3, 3), Card(14, 3), Card(11, 3),
               Card(2, 2), Card(6, 4)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_flush(gen))

    def test_is_flush3(self):
        # Test if method detects flush from 7 flush values
        gen = [Card(5, 3), Card(4, 3), Card(3, 3), Card(14, 3), Card(11, 3),
               Card(2, 2), Card(6, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 11, 6, 5, 4]), s.is_flush(gen))

    def test_is_full_house1(self):
        # Test if method detects full house
        gen = [Card(5, 2), Card(5, 3), Card(14, 3), Card(14, 2), Card(5, 4),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [5, 5, 5, 14, 14]), s.is_full_house(gen))

    def test_is_full_house2(self):
        # Test if method detects no full house
        gen = [Card(5, 2), Card(5, 3), Card(14, 3), Card(11, 2), Card(14, 4),
               Card(2, 1), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_full_house(gen))

    def test_is_full_house3(self):
        # Check if Full house not found in 2 three of a kinds
        gen = [Card(5, 2), Card(5, 3), Card(5, 1), Card(2, 4), Card(14, 4),
               Card(14, 1), Card(14, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 14, 14, 5, 5]), s.is_full_house(gen))

    def test_is_four_kind(self):
        # Test if method detects four of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 4), Card(12, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 14, 14, 14, 12]), s.is_four_kind(gen))

    def test_is_four_kind2(self):
        # Test if method detects no four of a kind
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(13, 4), Card(12, 3),
               Card(2, 1), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_four_kind(gen))

    def test_is_straight_flush1(self):
        # Test if method detects no straight flush
        gen = [Card(14, 3), Card(14, 2), Card(14, 1), Card(14, 4), Card(12, 3),
               Card(2, 2), Card(3, 3)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_straight_flush(gen))

    def test_is_straight_flush2(self):
        # Test if method detects straight flush
        gen = [Card(14, 3), Card(11, 3), Card(12, 3), Card(13, 3), Card(10, 3),
               Card(2, 1), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 13, 12, 11, 10]),
                         s.is_straight_flush(gen))

    def test_is_straight_flush3(self):
        # Test if method detects straight flush with 6 straight flush
        gen = [Card(9, 3), Card(11, 3), Card(12, 3), Card(13, 3), Card(10, 3),
               Card(14, 3), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [14, 13, 12, 11, 10]),
                         s.is_straight_flush(gen))

    def test_is_straight_flush4(self):
        # Test if method if no straight flush when straight and flush present
        gen = [Card(9, 3), Card(11, 4), Card(12, 3), Card(13, 3), Card(10, 3),
               Card(14, 3), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((False, []), s.is_straight_flush(gen))

    def test_is_straight_flush5(self):
        # Test if method detects wheel straight flush
        gen = [Card(5, 3), Card(4, 3), Card(14, 3), Card(13, 3), Card(2, 3),
               Card(3, 3), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [5, 4, 3, 2, 14]), s.is_straight_flush(gen))

    def test_is_straight_flush6(self):
        # Test if method detects straight-flush from 7
        gen = [Card(5, 3), Card(4, 3), Card(7, 3), Card(6, 3),
               Card(2, 3), Card(3, 3), Card(2, 2)]
        s = Showdown(None, None)
        gen = s.retrieve_values(gen)
        self.assertEqual((True, [7, 6, 5, 4, 3]),
                         s.is_straight_flush(gen))

    # Tests of find_best
    def test_find_best_high_card(self):
        # Test if method correctly finds the best high card combo
        gen = [Card(2, 3), Card(3, 2), Card(14, 1), Card(13, 4), Card(12, 3),
               Card(5, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.high_card, 14, 13, 12, 9, 5],
                         s.find_best(players[0]))

    def test_find_best_pair(self):
        # Test if method correctly finds the best pair combo
        gen = [Card(2, 3), Card(3, 2), Card(14, 1), Card(14, 4), Card(12, 3),
               Card(5, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.pair, 14, 14, 12, 9, 5],
                         s.find_best(players[0]))

    def test_find_best_two_pair(self):
        # Test if method correctly finds the best two pair combo
        gen = [Card(2, 3), Card(2, 2), Card(14, 1), Card(14, 4), Card(12, 3),
               Card(5, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.two_pair, 14, 14, 2, 2, 12],
                         s.find_best(players[0]))

    def test_find_best_two_pair2(self):
        # Test if method correctly finds the best two pair combo in three pairs
        gen = [Card(12, 3), Card(2, 2), Card(14, 1), Card(14, 4), Card(12, 3),
               Card(9, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.two_pair, 14, 14, 12, 12, 9],
                         s.find_best(players[0]))

    def test_find_best_three_kind(self):
        # Test if method correctly finds the best three of a kind combo
        gen = [Card(14, 3), Card(2, 2), Card(14, 1), Card(14, 4), Card(12, 3),
               Card(8, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.three_kind, 14, 14, 14, 12, 9],
                         s.find_best(players[0]))

    def test_find_best_straight(self):
        # Test if method correctly finds the best straight combo
        gen = [Card(14, 3), Card(2, 2), Card(6, 1), Card(7, 4), Card(5, 3),
               Card(8, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.straight, 9, 8, 7, 6, 5],
                         s.find_best(players[0]))

    def test_find_best_straight2(self):
        # Test if method correctly finds the best straight combo in 7 cards
        gen = [Card(10, 3), Card(11, 2), Card(6, 1), Card(7, 4), Card(5, 3),
               Card(8, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.straight, 11, 10, 9, 8, 7],
                         s.find_best(players[0]))

    def test_find_best_flush(self):
        # Test if method correctly finds the best flush combo
        gen = [Card(4, 4), Card(11, 4), Card(6, 1), Card(12, 4), Card(5, 4),
               Card(13, 3), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.flush, 12, 11, 9, 5, 4],
                         s.find_best(players[0]))

    def test_find_best_flush2(self):
        # Test if method correctly finds the best flush combo in 7 flush cards
        gen = [Card(4, 4), Card(11, 4), Card(6, 4), Card(12, 4), Card(5, 4),
               Card(13, 4), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.flush, 13, 12, 11, 9, 6],
                         s.find_best(players[0]))

    def test_find_best_full_house(self):
        # Test if method correctly finds the best full house
        gen = [Card(4, 4), Card(4, 3), Card(6, 4), Card(4, 1), Card(5, 4),
               Card(5, 2), Card(9, 4)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.full_house, 4, 4, 4, 5, 5],
                         s.find_best(players[0]))

    def test_find_best_full_house2(self):
        # Test if method correctly finds the best full house in 2 three kinds
        gen = [Card(4, 4), Card(4, 3), Card(6, 4), Card(4, 1), Card(5, 4),
               Card(5, 2), Card(5, 1)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.full_house, 5, 5, 5, 4, 4],
                         s.find_best(players[0]))

    def test_find_best_full_house3(self):
        # Test if method correctly finds the best full house in FH+Pair
        gen = [Card(4, 4), Card(4, 3), Card(6, 4), Card(6, 1), Card(5, 4),
               Card(5, 2), Card(5, 1)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.full_house, 5, 5, 5, 6, 6],
                         s.find_best(players[0]))

    def test_find_best_four_kind(self):
        # Test if method correctly finds the best four of a kind combo
        gen = [Card(4, 4), Card(4, 3), Card(4, 1), Card(4, 2), Card(5, 4),
               Card(5, 2), Card(5, 1)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual([BoardScore.four_kind, 4, 4, 4, 4, 5],
                         s.find_best(players[0]))

    def test_find_best_straight_flush(self):
        # Test if method correctly finds the best straight flush
        gen = [Card(14, 3), Card(11, 3), Card(12, 3), Card(13, 3), Card(10, 3),
               Card(2, 1), Card(2, 2)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual((True, [14, 13, 12, 11, 10]),
                         s.is_straight_flush(gen))

    def test_find_best_straight_flush2(self):
        # Test if method correctly finds the best straight flush
        # from 7-card straight flush
        gen = [Card(14, 3), Card(11, 3), Card(12, 3), Card(13, 3), Card(10, 3),
               Card(9, 3), Card(8, 3)]
        players = [Player([gen[1], gen[0]])]
        board = gen[2:]
        s = Showdown(players, board)
        self.assertEqual((True, [14, 13, 12, 11, 10]),
                         s.is_straight_flush(gen))

    # Tests for find_winners()
    def test_find_winners1(self):
        # Test if method accurately finds the winning player + hand from
        # 2 inputs
        gen = [Card(9, 1), Card(9, 2), Card(13, 4), Card(12, 4), Card(14, 1),
               Card(5, 4), Card(7, 2), Card(3, 1), Card(8, 3)]
        players = [Player([gen[0], gen[1]]), Player([gen[2], gen[3]])]
        board = gen[4:]
        s = Showdown(players, board)
        s.find_winners()
        self.assertEqual([players[0]], s.winners)
        self.assertEqual([1, 9, 9, 14, 8, 7], s.rank)

    def test_find_winners2(self):
        # Test if method accurately finds the winning player + hand from 3
        # inputs
        gen = [Card(9, 1), Card(9, 2), Card(13, 4), Card(12, 4),
               Card(14, 2), Card(14, 3), Card(14, 1),
               Card(5, 4), Card(7, 2), Card(3, 1), Card(8, 3)]
        players = [Player([gen[0], gen[1]]), Player([gen[2], gen[3]]),
                   Player([gen[4], gen[5]])]
        board = gen[6:]
        s = Showdown(players, board)
        s.find_winners()
        self.assertEqual([players[2]], s.winners)
        self.assertEqual([3, 14, 14, 14, 8, 7], s.rank)

    def test_find_winners3(self):
        # Test if method accurately finds the winning player + hand when
        # there exists a tie
        gen = [Card(9, 1), Card(9, 2), Card(13, 4), Card(12, 4),
               Card(9, 4), Card(9, 3), Card(14, 1),
               Card(5, 4), Card(7, 2), Card(3, 1), Card(8, 3)]
        players = [Player([gen[0], gen[1]]), Player([gen[2], gen[3]]),
                   Player([gen[4], gen[5]])]
        board = gen[6:]
        s = Showdown(players, board)
        s.find_winners()
        self.assertEqual([players[0], players[2]], s.winners)
        self.assertEqual([1, 9, 9, 14, 8, 7], s.rank)

    def test_find_winners4(self):
        # Test if method accurately finds the winning player + hand when
        # there exists a 3 - way tie
        gen = [Card(9, 1), Card(9, 2), Card(13, 4), Card(12, 4),
               Card(9, 4), Card(9, 3), Card(14, 1),
               Card(14, 2), Card(14, 3), Card(14, 4), Card(13, 3)]
        players = [Player([gen[0], gen[1]]), Player([gen[2], gen[3]]),
                   Player([gen[4], gen[5]])]
        board = gen[6:]
        s = Showdown(players, board)
        s.find_winners()
        self.assertEqual([players[0], players[1], players[2]], s.winners)
        self.assertEqual([7, 14, 14, 14, 14, 13], s.rank)

    def test_find_winners5(self):
        # Test if method accurately finds the winning player + hand from
        # 2 inputs
        gen = [Card(14, 1), Card(14, 2), Card(2, 4), Card(4, 4), Card(6, 1),
               Card(6, 4), Card(6, 2), Card(10, 1), Card(10, 3)]
        players = [Player([gen[0], gen[1]]), Player([gen[2], gen[3]])]
        board = gen[4:]
        s = Showdown(players, board)
        s.find_winners()
        self.assertEqual([players[0]], s.winners)
        self.assertEqual([6, 6, 6, 6, 14, 14], s.rank)

if __name__ == '__main__':
    unittest.main()
