"""Test case for the computer class."""
import unittest

from Computer import Computer
"""Test case for the Computer class."""
class TestComputer(unittest.TestCase): 
    """Test case for the Computer class."""
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

