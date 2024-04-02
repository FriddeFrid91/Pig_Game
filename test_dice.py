import unittest
from Dice import Dice
"""Testing the Dice class."""


class test_dice(unittest.TestCase):
    """Test for Dice class."""

    def test_roll_the_dice(self):
        """Test for roll_the_dice method."""
        new_dice = Dice(6)
        result = new_dice.roll_the_dice()
        self.assertIsNotNone(result)

    def test_show_the_dice(self):
        """Test for show_the_dice method."""
        new_dice = Dice(6)
        result = new_dice.roll_the_dice()
        show = new_dice.show_the_dice(result)
        self.assertIsNotNone(show)

    def test_get_dice(self):
        """Test for get_dice method."""
        new_dice = Dice(6)
        result = new_dice.get_dice()
        self.assertIsNotNone(result)

    def test_set_dice(self):
        """Test for set_dice method."""
        new_dice = Dice(6)
        new_dice.set_dice(6)
        result = new_dice.get_dice()
        self.assertEqual(result, 6)
