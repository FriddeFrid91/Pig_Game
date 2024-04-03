import unittest
from menu import Menu
"""Testing the Menu class"""    


class test_menu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        result = the_menu.show_menu()
        self.assertIsNotNone(result)

    def test_back_to_menu(self):
        """Test for back_to_menu method."""
        the_menu = Menu()
        result = the_menu.back_to_menu()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()