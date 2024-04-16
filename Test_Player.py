"""Unittest for Player.py."""
import unittest
from Player import Player
from unittest.mock import patch, MagicMock
"""unittest for Player.py"""


class Test_Player(unittest.TestCase):
    """Test for Player class."""
    @patch("builtins.input", side_effect=["yes", "no", "cheat", "quit"])
    def test_player_name(self):
        """Test for player_name method."""
        player1 = Player("TestPlayer1", 0)
        player2 = Player("TestPlayer2", 0)

        self.assertEqual(player1.get_name(), "TestPlayer1")
        self.assertEqual(player2.get_name(), "TestPlayer2") 

    def test_add_score(self):
        """Test for add_score method."""
        player = Player("TestPlayer", 0)
        player.add_score(50)
        self.assertEqual(player.get_score(), 50)

    def test_deduct_score(self):
        """Test for deduct_score method."""
        player = Player("TestPlayer", 100)
        player.deduct_score(50)
        if player.get_score() < 0:
            self.assertEqual(player.get_score(), 0)
        self.assertEqual(player.get_score(), 50)

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

    def test_player_move(self, mock_input):
        """Test for player_move method."""
        player = Player("TestPlayer", 0)

        with self.subTest(message="Test 'yes' input"):
            result = player.player_move()
            self.assertEqual(result, "yes")

        with self.subTest(message="Test 'no' input"):
            result = player.player_move()
            self.assertEqual(result, "no")

        with self.subTest(message="Test 'quit' input"):
            result = player.player_move()
            self.assertEqual(result, "quit")

        with self.subTest(message="Test 'cheat' input"):
            result = player.player_move()
            self.assertEqual(result, "cheat")

        player.dice.roll_the_dice = MagicMock(return_value=1)
        player.player_move()
        player.dice.roll_the_dice.assert_called_once()

        player.dice.roll_the_dice = MagicMock(return_value=2)
        player.player_move()
        player.dice.roll_the_dice.assert_called_once()

        player.dice.roll_the_dice = MagicMock(return_value=3)
        player.player_move()
        player.dice.roll_the_dice.assert_called_once()

        player.dice.roll_the_dice = MagicMock(return_value=4)
        player.player_move()
        player.dice.roll_the_dice.assert_called_once()

        player.dice.roll_the_dice = MagicMock(return_value=5)
        player.player_move()
        player.dice.roll_the_dice.assert_called_once()

        player.dice.roll_the_dice = MagicMock(return_value=6)
        player.player_move()
        player.dice.roll_the_dice.assert_called_once()


if __name__ == "__main__":
    unittest.main()
