"""Test for Menu class."""
from menu import Menu
import unittest
"""Test for Menu class."""


class TestMyMenu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        self.assertEquals(the_menu.show_menu(), "Welcome to a game of Pig!\n*************************\n* 1. Player Vs Computer *\n* 2. Player Vs Player   *\n* 3. Rules              *\n* 4. Highscore          *\n* 5. Change name        *\n*************************\n* 6. Exit               *\n*************************")

    if __name__ == 'main':
        unittest.main()
