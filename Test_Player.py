import unittest
from Player import Player

"""unittest for Player.py"""


class Test_Player(unittest.TestCase):
    """Test for Player class."""
    def test_player_move(self):
        """Test for player_move method."""
        player = Player("TestPlayer", 0)
        result = player.player_move()
        self.assertIsNone(result)

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

    def test_player_name(self):
        """Test for player_name method."""
        Player("TestPlayer", 0)
        self.assertEqual("TestPlayer", "TestPlayer")


if __name__ == "__main__":
    unittest.main()
