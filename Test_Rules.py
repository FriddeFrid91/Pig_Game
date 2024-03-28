from Rules import Rules

import unittest

class Test_Rules(unittest.TestCase):
    def test_get_rules(self):
        the_rules = Rules()
        self.assertEqual(the_rules.get_rules(), "You can play the game with 1 players with the computer\nYou can play the game with 2 players\nFirst player to get 100 points wins\nIf you roll a 1, you lose all your points for that turn\nIf you hold, you keep your points for that turn")
