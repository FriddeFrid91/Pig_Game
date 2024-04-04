import unittest
from highscore import highscore
from unittest.mock import patch, mock_open
from io import StringIO


class TestHighscore(unittest.TestCase):
    """Test class for highscore."""

    def setUp(self):
        """Set up method to create an instance of highscore."""
        self.highscore_instance = highscore()

    def test_show_highscore(self):
        """Test the show_highscore function."""
        # Replace standard output with a StringIO object to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.highscore_instance.show_highscore()
            expected_output = "****************\n* HALL OF FAME *\n****************\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_add_highscore(self):
        """Test the add_highscore function."""
        # Mock the pickle.dump function
        with patch('pickle.dump') as mock_dump:
            self.highscore_instance.add_highscore("Player1")
            mock_dump.assert_called_once()

    def test_load_highscore(self):
        """Test the load_highscore function."""
        # Mock the pickle.load function to return sample data
        with patch('pickle.load', return_value={"Player1": 3, "Player2": 2}) as mock_load:
            self.highscore_instance.load_highscore()
            self.assertEqual(self.highscore_instance.get_highscore(), {"Player1": 3, "Player2": 2})


if __name__ == '__main__':
    unittest.main()
