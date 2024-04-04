import unittest
from highscore import highscore


class TestHighscore(unittest.TestCase):
    """Test class for highscore."""
 
    show = highscore()

    def test_show_highscore(self):
        """Test the show highscore function."""
        self.show.show_highscore()
        expected_output = [
            "****************",
            "* HALL OF FAME *",
            "****************"
        ]
        self.assertEqual(expected_output)

    def test_load_highscore(self):
        """Test the load highscore function."""
        self.show.load_highscore()
        self.assertEqual(self.show.load_highscore(), {})

    def test_add_highscore(self):
        """Test the add highscore function."""
        winner = "Player 1"
        self.show.add_highscore(winner)
        self.assertIsNotNone(winner)


if __name__ == '__main__':
    unittest.main()
