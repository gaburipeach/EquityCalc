from unittest import TestCase
import unittest
from Simulator import Simulator
from Player import Player, Card

class TestSimulator(TestCase):

    def test_generate_random_showdown(self):
        s = Simulator()
        players = [Player([Card(14, 1), Card(13, 2)]), Player([Card(12, 1),Card(12, 2)]), Player([Card(8,2), Card(8,3)])]
        a,b,c = s.generate_random_showdown(players)
        print(a, b, c)
        self.assertEqual(True, 1)

if __name__ == '__main__':
    unittest.main()
