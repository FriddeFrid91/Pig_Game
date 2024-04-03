import unittest
from menu import Menu
"""Testing the Menu class"""    


class test_menu(unittest.TestCase):
    """Test for Menu class."""

    def test_start_game(self):
        start = Menu()
        self.assertEqual(
            start.start_game(),
            "Welcome to Pig Dice Game!\n"
            "Would you like to play a game?\n"
            "1. Yes\n"
            "2. No\n"
            "Please enter your choice: ")


if __name__ == "__main__":
    unittest.main()