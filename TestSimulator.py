from unittest import TestCase
from Simulator import Simulator
from Player import Player, Card

class TestSimulator(TestCase):
    def test_generate_random_cards(self):
        self.fail()

    def test_generate_random_showdown(self):
        s = Simulator
        players = [Player([Card(14, 1), Card(14, 2)])]
        self.assertEqual([[Card(14, 1), Card(14, 2)]],
                         s.generate_random_showdown([players]))
