import unittest
from Player import Player
from unittest.mock import patch, MagicMock
from io import StringIO
from Player import Player
from Dice import Dice

"""unittest for Player.py"""


class Test_Player(unittest.TestCase):
    """Test for Player class."""

    def setUp(self):
        """Set up method to create an instance of Player."""
        self.player = Player("TestPlayer")

    @patch('player.Player.dice')  # Mock the Dice object
    def test_player_move(self, mock_dice):
        """Test the player_move method."""
        # Mock the roll_the_dice method of the Dice object
        mock_dice.roll_the_dice.side_effect = [4, 3, 1]

        # Capture printed output
        with patch('sys.stdout', new_callable=StringIO):
            self.player.player_move()

        # Test input handling for "no"
        with patch('builtins.input', side_effect=["no"]):
            self.player.player_move()
            self.assertEqual(self.player.get_score(), 0)

        # Test input handling for "yes"
        with patch('builtins.input', side_effect=["yes", "yes", "no"]):
            self.player.player_move()
            self.assertEqual(self.player.get_score(), 7)

        # Test input handling for "cheat"
        with patch('builtins.input', side_effect=["cheat"]):
            self.player.player_move()
            self.assertEqual(self.player.get_score(), 100)

    def test_add_score(self):
        """Test for add_score method."""
        player = Player("TestPlayer", 0)
        player.add_score(50)
        self.assertEqual(player.get_score(), 50)

    def test_deduct_score(self):
        """Test for deduct_score method."""
        player = Player("TestPlayer", 100)
        player.deduct_score(50)
        self.assertEqual(player.get_score(), 50)

    def test_get_score(self):
        """Test for get_score method."""
        player = Player("TestPlayer", 100)
        result = player.get_score()
        self.assertEqual(result, 100)


if __name__ == "__main__":
    unittest.main()
