import unittest
from player_vs_player import player_vs_player


class TestPlayerVsPlayer(unittest.TestCase):
    """Test case for Player vs Player class."""

    def test_two_player_game(self):
        """Test the two_player_game method."""
        game = player_vs_player()
        winner = game.two_player_game('Player 1', 'Player 2')
        self.assertIsNotNone(winner)
        self.assertIsInstance(winner, str)

        winner = game.two_player_game('Player 2', 'Player 1')
        self.assertIsNotNone(winner)
        self.assertIsInstance(winner, str)  # Check if the winner is a string
        self.name = winner
        if self.name == 'Player 1':
            self.assertEqual(winner, 'Player 1')
        else:  # Check if the winner is the second player
            self.assertEqual(winner, 'Player 2')

        current_winner = game.winner
        self.assertIsNotNone(current_winner)

        # pragma: no cover

    def test_get_loser(self):
        """Test the get_loser method."""
        game = player_vs_player()
        game.two_player_game('Player 1', 'Player 2')
        loser = game.get_loser()
        self.assertIsNotNone(loser)
        self.assertIsInstance(loser, str)

        # pragma: no cover


if __name__ == '__main__':
    unittest.main()
