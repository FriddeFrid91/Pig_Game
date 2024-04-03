"""unittest for Rules.py"""

import unittest
<<<<<<< HEAD
from rules import Rules

"""Test for Rules class."""
class RulesTestCase(unittest.TestCase):
    def test_get_rules(self):
        the_rules = Rules()
        result = the_rules.get_rules()
        self.assertIsNotNone(result)

if __name__ == '__main__':
=======
from Rules import Rules
"""Testing the Rules class"""


class Test_Rules(unittest.TestCase):
    """Test for Rules class."""
    def test_get_rules(self):
        the_rules = Rules()
        self.assertEqual(the_rules.get_rules(), "You can play the game with 1 players with the computer\nYou can play the game with 2 players\nFirst player to get 100 points wins\nIf you roll a 1, you lose all your points for that turn\nIf you hold, you keep your points for that turn")


if __name__ == "__main__":
>>>>>>> main
    unittest.main()
