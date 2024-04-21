"""unittest for Rules."""

import unittest
from Rules import Rules
"""Testing the Rules class"""


class Test_Rules(unittest.TestCase):
    """Test Rules class."""

    def test_show_rules(self):
        """Test show_rules method."""
        rules = Rules()
        self.assertEqual(rules.show_rules(),
                         "The rules are simple: \n"
                         "1. The game has 2 players, a human and a computer.\n"
                         "2. Each turn, a player repeatedly rolls a die ",
                         " until either a 1 is rolled or the player ",
                         "decides to hold.\n"
                         "3. If the player rolls a 1, ",
                         "they score nothing and it becomes ",
                         "the opponent's turn.\n"
                         "4. If the player rolls any other number, ",
                         "it is added to their turn total and the ",
                         "player's turn continues.\n"
                         "5. If a player chooses to hold, ",
                         "their turn total is added to their score, ",
                         "and it becomes the opponent's turn.\n"
                         "6. The first player to score ",
                         "100 or more points wins.\n")


if __name__ == '__main__':
    unittest.main()
