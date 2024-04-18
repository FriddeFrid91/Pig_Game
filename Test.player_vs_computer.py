"""This module tests the player_vs_computer.py module."""
import unittest
from unittest.mock import patch
from player_vs_computer import PlayerVsComputer


class TestPlayerVsComputer(unittest.TestCase):
    """Test the PlayerVsComputer class."""
    @patch("builtins.input", side_effect=["Player1", "easy"])
    def test_player_vs_computer_game(self, mock_input):
        """Test the player_vs_computer_game method."""
        game = PlayerVsComputer()
        result = game.player_vs_computer_game()
        self.assertEqual(result, "Player1")


if __name__ == "__main__":
    unittest.main()


