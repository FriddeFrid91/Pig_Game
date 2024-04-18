import unittest
from Dice import Dice


class TestDice(unittest.TestCase):
    """Test for Dice class."""
    def test_roll_the_dice(self):
        """Test for roll_the_dice method."""
        dice = Dice(6)
        result = dice.roll_the_dice()
        self.assertTrue(1 <= result <= 6)


if __name__ == "__main__":
    unittest.main()