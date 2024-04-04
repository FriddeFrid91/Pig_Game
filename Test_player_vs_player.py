import unittest
from player_vs_player import player_vs_player


class TestPlayerVsPlayer(unittest.TestCase):
    """Test case for Player vs Player class."""

    def test_two_player_game(self):
        """Test the two_player_game method."""
        game = player_vs_player()
        winner = game.two_player_game('Player 1')
        self.assertIsNotNone(winner)


if __name__ == '__main__':
    unittest.main()
