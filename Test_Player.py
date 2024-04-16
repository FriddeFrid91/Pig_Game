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
        player = Player("TestPlayer", 0)
        result = player.player_name()
        self.assertEqual(result, "TestPlayer")

    def test_add_score(self):
        """Test for add_score method."""
        player = Player("TestPlayer", 0)
        player.add_score(50)
        self.assertEqual(player.get_score(), 50)

    def test_deduct_score(self):
        """Test for deduct_score method."""
        player = Player("TestPlayer", 100)
        player.deduct_score(50)
        self.assertEqual(player.get_score(), 50)

    def test_get_score(self):
        """Test for get_score method."""
        player = Player("TestPlayer", 100)
        result = player.get_score()
        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
