import unittest
from player_vs_player import player_vs_player


class TestPlayerVsPlayer(unittest.TestCase):
    """Test case for Player vs Player class."""

    def test_two_player_game(self):
        """Test the two_player_game method."""
        game = player_vs_player()
        winner = game.two_player_game('Player 1', 'Player 2')
        self.assertIsNotNone(winner)

        winner = game.two_player_game('Player 2', 'Player 1')
        self.assertIsNotNone(winner)

        self.assertIsInstance(winner, str)  # Check if the winner is a string

    def test_get_loser(self):
        """Test the get_loser method."""
        game = player_vs_player()
        game.two_player_game('Player 1', 'Player 2')
        loser = game.get_loser()
        self.assertIsNotNone(loser)

        self.assertIsInstance(loser, str)


if __name__ == '__main__':
    unittest.main()
