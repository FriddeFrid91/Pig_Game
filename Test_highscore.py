import unittest
from highscore import highscore
from unittest.mock import patch, mock_open, Mock


class TestHighscore(unittest.TestCase):
    """Test class for highscore."""

    def setUp(self):
        """Set up method to create an instance of highscore."""
        self.highscore_instance = highscore()

    def test_show_highscore(self):
        """Test the show_highscore function."""
        # Mock the print function
        self.assertIsNone(self.highscore_instance.show_highscore())

    def test_add_highscore(self):
        """Test the add_highscore function."""
        # Mock the pickle.dump function
        with patch('pickle.dump') as mock_dump:
            self.highscore_instance.add_highscore("Player1")
            mock_dump.assert_called_once()
    
    def test_add_highscore_eof_error(self):
        """Test the add_highscore function when EOFError is raised."""
        # Mock the pickle.dump function to raise EOFError
        with patch('pickle.dump', side_effect=EOFError) as mock_dump:
            self.highscore_instance.add_highscore("Player1")
            self.assertEqual(self.highscore_instance.get_highscore(), {})

    def test_load_highscore(self):
        """Test the load_highscore function."""
        # Mock the pickle.load function to return sample data
        with patch('pickle.load', return_value={"Player1": 3, "Player2": 2}) as mock_load:
            self.highscore_instance.load_highscore()
            self.assertEqual(self.highscore_instance.get_highscore(), {"Player1": 3, "Player2": 2})

    def test_load_highscore_file_not_found(self):
        """Test the load_highscore function when the file is not found."""
        # Mock the pickle.load function to raise FileNotFoundError
        with patch('pickle.load', side_effect=FileNotFoundError) as mock_load:
            self.highscore_instance.load_highscore()
            self.assertEqual(self.highscore_instance.get_highscore(), {})

    def test_load_highscore_eof_error(self):
        """Test the load_highscore function when EOFError is raised."""
        # Mock the pickle.load function to raise EOFError
        with patch('pickle.load', side_effect=EOFError) as mock_load:
            self.highscore_instance.load_highscore()
            self.assertEqual(self.highscore_instance.get_highscore(), {}) 

    def test_show_losses(self):
        """Test the show_losses function."""
        # Mock the print function
        self.assertIsNone(self.highscore_instance.show_losses())

    def test_add_losses(self):
        """Test the add_losses function."""
        # Mock the pickle.dump function
        with patch('pickle.dump') as mock_dump:
            self.highscore_instance.add_losses("Player1")
            mock_dump.assert_called_once()

    def test_load_losses(self):
        """Test the load_losses function."""
        # Mock the pickle.load function to return sample data
        with patch('pickle.load', return_value={"Player1": 3, "Player2": 2}) as mock_load:
            self.highscore_instance.load_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {"Player1": 3, "Player2": 2})

    def test_load_losses_file_not_found(self):
        """Test the load_losses function when the file is not found."""
        # Mock the pickle.load function to raise FileNotFoundError
        with patch('pickle.load', side_effect=FileNotFoundError) as mock_load:
            self.highscore_instance.load_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {})

    def test_load_losses_eof_error(self):
        """Test the load_losses function when EOFError is raised."""
        # Mock the pickle.load function to raise EOFError
        with patch('pickle.load', side_effect=EOFError) as mock_load:
            self.highscore_instance.load_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {})


if __name__ == '__main__':
    unittest.main()
