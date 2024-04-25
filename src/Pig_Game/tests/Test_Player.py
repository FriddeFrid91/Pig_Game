"""Unittest for Player.py."""
import unittest
from Player import Player
from unittest.mock import patch
"""unittest for Player.py"""


class Test_Player(unittest.TestCase):
    """Test for Player class."""

    def test_player_name(self):
        """Test for player_name method."""
        player_1 = Player("TestPlayer1", 0)
        player_2 = Player("TestPlayer2", 0)
        self.assertEqual(player_1.name, "TestPlayer1")
        self.assertEqual(player_2.name, "TestPlayer2")
        self.assertNotEqual(player_1.name, player_2.name)

    def test_add_score(self):
        """Test for add_score method."""
        player = Player("TestPlayer", 0)
        player.add_score(6)
        self.assertEqual(player.get_score(), 6)

    def test_deduct_score(self):
        """Test for deduct_score method."""
        player = Player("TestPlayer", 26)
        player.deduct_score(26)
        if player.get_score() < 0:
            self.assertEqual(player.get_score(), 0)
        self.assertEqual(player.get_score(), 26)

    def test_get_score(self):
        """Test for get_score method."""
        player = Player("TestPlayer", 100)
        result = player.get_score()
        self.assertEqual(result, 100)

    def test_set_score(self):
        """Test for set_score method."""
        player = Player("TestPlayer", 0)
        player.set_score(100)
        self.assertEqual(player.get_score(), 100)

    @patch('builtins.input', side_effect=['yes', 'no', 'quit', 'cheat'])
    def test_player_move(self, mocked_input):
        """Test for player_move method."""
        mocked_input.side_effect = ['yes', 'no', 'quit', 'cheat']
        """Test for player_move method."""
        player = Player("TestPlayer", 0)


if __name__ == "__main__":
    unittest.main()
