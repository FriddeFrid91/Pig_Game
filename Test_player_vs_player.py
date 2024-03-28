from playervsplayer import playervsplayer
from Player import Player
import unittest
"""Test for Player vs Player class."""


class Test_playervsplayer(unittest.TestCase):
    """Test for Player vs Player class."""

    def test_two_player_game(self):
        """Test for two_player_game method."""
        new_game = playervsplayer()
        result = new_game.two_player_game()
        self.assertIsNotNone(result)


if __name__ == 'main':
    unittest.main()
