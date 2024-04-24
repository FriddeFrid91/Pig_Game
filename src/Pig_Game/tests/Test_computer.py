"""Test case for the computer class."""
import unittest
from unittest.mock import Mock
from Computer import Computer
from Dice import Dice
"""Test case for the Computer class."""


class TestComputer(unittest.TestCase):
    """Test case for the Computer class."""

    def test_easy_difficulty(self):
        """Test the easy_difficulty method."""
        computer = Computer()
        computer.Dice = Mock()
        computer.Dice.roll_the_dice.return_value = 1
        computer.easy_difficulty()
        computer.Dice.roll_the_dice.return_value = 6
        computer.easy_difficulty()
        computer.Dice.roll_the_dice.return_value = 2
        computer.easy_difficulty()
        self.assertIsNotNone(computer)
        self.assertIsInstance(computer, Computer)

    def test_computer_move(self):
        """Test the computer_move method."""
        computer = Computer()
        computer.set_difficulty("easy")
        computer.computer_move()
        computer.set_difficulty("medium")
        computer.computer_move()
        computer.set_difficulty("hard")
        computer.computer_move()
        self.assertIsNotNone(computer)
        self.assertIsInstance(computer, Computer)
        # pragma: no cover
