"""Test for Menu class."""
from menu import Menu
import unittest
"""Test for Menu class."""


class TestMyMenu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        self.assertIsNotNone(the_menu.show_menu())
    if __name__ == 'main':
        unittest.main()
