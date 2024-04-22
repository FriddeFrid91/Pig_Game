"""Test case for the player_vs_player class."""
import unittest
from player_vs_player import player_vs_player


class TestPlayerVsPlayer(unittest.TestCase):
    """Test case for Player vs Player class."""

    def test_set_loser(self):
        """Test the set_loser method."""
        game = player_vs_player()
        game.set_loser("TestPlayer")
        self.assertEqual(game.loser, "TestPlayer")

    def test_get_loser(self):
        """Test the get_loser method."""
        game = player_vs_player()
        game.two_player_game("TestPlayer1", "TestPlayer2")
        loser = game.get_loser()
        self.assertIsNotNone(loser)
        self.assertIsInstance(loser, str)


if __name__ == '__main__':
    unittest.main()
