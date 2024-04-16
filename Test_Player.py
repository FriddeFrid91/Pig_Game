"""Unittest for Player.py."""
import unittest
from Player import Player
from unittest.mock import patch, MagicMock
from io import StringIO
from Dice import Dice
"""unittest for Player.py"""


class Test_Player(unittest.TestCase):
    """Test for Player class."""

    def test_player_name(self):
        """Test for player_name method."""
        player1 = Player("TestPlayer1", 0)
        player2 = Player("TestPlayer2", 0)

        self.assertEqual(player1.get_name(), "TestPlayer1")
        self.assertEqual(player2.get_name(), "TestPlayer2") 

    def two_player_game(self):
        """Test for two_player_game method."""
        player1 = Player("TestPlayer1", 0)
        player2 = Player("TestPlayer2", 0)
        player1.player_move = MagicMock(return_value=0)
        player2.player_move = MagicMock(return_value=0)

        player1.two_player_game(player1, player2)
        player1.player_move.assert_called_once()
        player2.player_move.assert_called_once()

        dice = Dice()
        dice.roll = MagicMock(return_value=1)

        if dice.roll() == 1:
            self.assertEqual(player1.get_score(), 0)
            self.assertEqual(player2.get_score(), 0)

    def test_add_score(self):
        """Test for add_score method."""
        player = Player("TestPlayer", 0)
        player.add_score(50)
        self.assertEqual(player.get_score(), 50)

    def test_deduct_score(self):
        """Test for deduct_score method."""
        player = Player("TestPlayer", 100)
        player.deduct_score(50)
        if player.get_score() < 0:
            self.assertEqual(player.get_score(), 0)
        self.assertEqual(player.get_score(), 50)

    def test_get_score(self):
        """Test for get_score method."""
        player = Player("TestPlayer", 100)
        result = player.get_score()
        self.assertEqual(result, 100)

    def test_set_score(self):
        """Test for set_score method."""
        player = Player("TestPlayer", 0)
        player.set_score(100)
        self.assertEqual(player.get_score(), 100)


if __name__ == "__main__":
    unittest.main()
