"""unit test for player_vs_computer.py."""
import unittest

from player_vs_computer import player_vs_computer
"""Test case for Player vs Computer class."""


class TestPlayerVsComputer(unittest.TestCase):
    """Test case for Player vs Computer class."""

    def test_player_vs_computer_game(self):
        """Test the player_vs_computer_game method."""
        game = player_vs_computer()
        game.player_vs_computer_game("easy")
        game.player_vs_computer_game("medium")
        game.player_vs_computer_game("hard")
        self.assertIsNotNone(game)
        self.assertIsInstance(game, player_vs_computer)
        # pragma: no cover
