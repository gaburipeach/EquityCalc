from unittest import TestCase
from Simulator import Simulator
from Player import Player, Card

class TestSimulator(TestCase):

    def test_generate_random_showdown(self):
        s = Simulator()
        players = [Player([Card(14, 1), Card(13, 2)]), Player([Card(12, 1),
                                                               Card(12, 2)])]
        self.assertEqual(True, s.generate_random_showdown(players))
