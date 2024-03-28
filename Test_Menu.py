"""Test for Menu class."""
import unittest
from menu import Menu
"""Test for Menu class."""


class TestMyMenu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        the_menu.show_menu()
        self.assertIsNotNone(the_menu.menu_options)
    if __name__ == 'main':
        unittest.main()
