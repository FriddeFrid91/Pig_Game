import unittest
from player_vs_player import player_vs_player


class test_player_vs_player(unittest.TestCase):
    """Test for Player vs Player class."""

    def test_two_player_game(self):
        """Test for two_player_game method."""
        new_game = player_vs_player()
        result = new_game.two_player_game()
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
