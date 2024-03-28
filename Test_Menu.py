import unittest
from menu import Menu
"""Test for Menu class."""


class Test_Menu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        menu = the_menu.show_menu()
        self.assertIsNotNone(menu)


if __name__ == "__main__":
    unittest.main()
