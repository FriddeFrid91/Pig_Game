"""Unittesting for the Menu class."""
import unittest
from menu import Menu


class test_menu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_pig(self):
        """Test for show_pig method."""
        the_menu = Menu()
        piggy = the_menu.show_pig()
        self.assertIsNotNone(piggy)

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        menu = the_menu.show_menu()
        self.assertIsNotNone(menu)


if __name__ == "__main__":
    unittest.main()
