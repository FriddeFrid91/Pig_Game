import unittest
from player_vs_player import player_vs_player
from unittest.mock import patch


class test_player_vs_player(unittest.TestCase):
    """Test for Player vs Player class."""
    @patch("builtins.input", side_effect=["Player1"], side_effect=["Player2"])
    def test_two_player_game(self, mock_input):
        """Test for player_vs_player method."""
        new_game = player_vs_player()
        result = new_game.two_player_game(mock_input)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
