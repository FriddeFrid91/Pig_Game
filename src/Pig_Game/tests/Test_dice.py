import unittest
from Dice import Dice


class TestDice(unittest.TestCase):
    """Test for Dice class."""
    def test_roll_the_dice(self):
        """Test for roll_the_dice method."""
        dice = Dice(6)
        result = dice.roll_the_dice()
        self.assertTrue(1 <= result <= 6)

    def show_the_dice(self):
        """Test for show_the_dice method."""
        dice = Dice(6)
        result = dice.roll_the_dice()
        if result == 1:
            self.assertEqual(dice.show_the_dice(result), 0)
        else:
            self.assertIsNotNone(dice.show_the_dice(result))

    def test_get_dice(self):
        """Test for get_dice method."""
        dice = Dice(6)
        self.assertEqual(dice.get_dice(), 6)

    def test_set_dice(self):
        """Test for set_dice method."""
        dice = Dice(6)
        dice.set_dice(8)
        self.assertEqual(dice.get_dice(), 8)


if __name__ == "__main__":
    unittest.main()