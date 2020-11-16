import unittest
from src.card import *
from src.card_game import *

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.game = CardGame()
        self.card1 = Card("hearts", 3)
        self.card2 = Card("diamonds", 1)
        self.cards = [self.card1, self.card2]

    def test_card_has_value(self):
        self.assertEqual(1, self.card2.value)
    
    def test_card_has_suit(self):
        self.assertEqual("hearts", self.card1.suit)

    def test_check_for_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card1, self.game.highest_card(self.card1, self.card2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 4", self.game.cards_total(self.cards))