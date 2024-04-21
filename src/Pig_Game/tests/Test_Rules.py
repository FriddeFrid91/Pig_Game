"""unittest for Rules"""

import unittest
from Rules import Rules
"""Testing the Rules class"""


class Test_Rules(unittest.TestCase):
    
    """Test for Rules class."""
    def test_get_rules(self):
        the_rules = Rules()
        self.assertEqual(
            the_rules.get_rules().strip(),
            "You can play the game with 1 players with the computer\nYou can"
            "play the game with 2 players\nFirst player to get 100 points wins\nIf "
            "You roll a 1, you lose all your points for that turn\nIf you hold,"
            "you keep your points for that turn")
        
        # pragma: no cover


if __name__ == '__main__':
    unittest.main()