import unittest
from menu import Menu
<<<<<<< HEAD
=======
"""Testing the Menu class"""    
>>>>>>> main


class test_menu(unittest.TestCase):
    """Test for Menu class."""

    def test_show_menu(self):
        """Test for show_menu method."""
        the_menu = Menu()
        result = the_menu.show_menu()
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()