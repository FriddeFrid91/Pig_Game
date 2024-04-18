import unittest
from Dice import Dice


class TestDice(unittest.TestCase):
    """Test for Dice class."""
    def test_roll_the_dice(self):
        """Test for roll_the_dice method."""
        dice = Dice()
        result = dice.roll_the_dice()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 6)


if __name__ == "__main__":
    unittest.main()