"""unittest for Rules.py"""

import unittest
from rules import Rules

"""Test for Rules class."""
class RulesTestCase(unittest.TestCase):
    def test_get_rules(self):
        the_rules = Rules()
        result = the_rules.get_rules()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
