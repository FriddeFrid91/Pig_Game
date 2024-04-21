"""unittest for Rules."""

import unittest
from Rules import Rules
"""Testing the Rules class"""


class Test_Rules(unittest.TestCase):
    """Test Rules class."""

    def test_show_rules(self):
        """Test show_rules method."""
        the_rules = Rules()
        self.assertEqual(the_rules.show_rules(), [
            "\033[95m**RULES OF PIG GAME**\033[0m",
            "\033[93m********************************************\033[0m",
            "\033[94mYou can play the game with 1 player with the computer\033[0m",
            "\033[94mYou can play the game with 2 players\033[0m",
            "\033[94mFirst player to get 100 points wins\033[0m",
            "\033[92mIf you roll a 1, you lose all your points for that turn\033[0m",
            "\033[94mIf you hold, you keep your points for that turn\033[0m",
            "\033[93m*********************************************\033[0m"])


if __name__ == '__main__':
    unittest.main()