"""Test module for highscore."""
import unittest
from highscore import highscore
from unittest.mock import mock_open, patch
import pickle


class TestHighscore(unittest.TestCase):
    """Test class for highscore."""

    def setUp(self):
        """Set up a method to create an instance of highscore."""
        self.highscore_instance = highscore()
        self.test_highscore_data = {"Player1": 3, "Player2": 2}

    def test_change_name(self):
        """Test the change_name function."""
        # Mock the print function
        mock_file_open = mock_open()
        with patch('builtins.print') as mock_print:
            self.assertIsNone(self.highscore_instance.change_name())
            mock_print.assert_called()
        if input == "":
            self.assertEqual(input(), "Please enter a name from the scoreboard. \n")
        if input == "quit":
            self.assertEqual(input(), "Quitting the name change. \n")
        if input == "Player1":
            self.assertEqual(input(), "Enter the new name: \n")
        if input == "Player1":
            self.assertEqual(input(), "The name is the same as the old name.\n")
        if input == "Player2":
            self.assertEqual(input(), "The name is already in the highscore table.\n")
        if input == "Player3":
            self.assertEqual(input(), "Player3 is the new name.\n")

        if input in self.highscore_instance.highscore_dict:
            self.assertEqual(input(), "Player3")
        if input in self.highscore_instance.losses:
            self.assertEqual(input(), "Player3")

    def test_load_highscore(self):
        """Test the load_highscore function."""
        # Mock the pickle.load function to return sample data
        with patch('pickle.load', return_value={"Player1": 3, "Player2": 2}):
            self.highscore_instance.load_highscore()
            self.assertEqual(self.highscore_instance.get_highscore(),
                             self.test_highscore_data)

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

    def test_add_highscore_no_winner(self):
        """Test the add_highscore function when there is no winner."""
        # Mock the pickle.dump function
        with patch('pickle.dump') as mock_dump:
            self.highscore_instance.add_highscore("")
            mock_dump.assert_not_called()

    def test_add_highscore_eof_error(self):
        """Test the add_highscore function when EOFError is raised."""
        # Mock the pickle.dump function to raise EOFError
        with patch('pickle.dump', side_effect=EOFError):
            self.highscore_instance.add_highscore("Player1")
            self.assertEqual(self.highscore_instance.get_highscore(), {})

    def test_add_highscore_file_not_found(self):
        """Test the add_highscore function when the file is not found."""
        # Mock the pickle.dump function to raise FileNotFoundError
        with patch('pickle.dump', side_effect=FileNotFoundError):
            self.highscore_instance.add_highscore("Player1")
            self.assertEqual(self.highscore_instance.get_highscore(), {})

    def test_load_highscore_file_not_found(self):
        """Test the load_highscore function when the file is not found."""
        # Mock the pickle.load function to raise FileNotFoundError
        with patch('pickle.load', side_effect=FileNotFoundError):
            self.highscore_instance.load_highscore()
            self.assertEqual(self.highscore_instance.get_highscore(), {})

    def test_load_highscore_eof_error(self):
        """Test the load_highscore function when EOFError is raised."""
        # Mock the pickle.load function to raise EOFError
        with patch('pickle.load', side_effect=EOFError):
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

    def test_add_losses_eof_error(self):
        """Test the add_losses function when EOFError is raised."""
        # Mock the pickle.add function to raise EOFError
        with patch('pickle.load', side_effect=EOFError):
            self.highscore_instance.add_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {})

    def test_load_losses(self):
        """Test the load_losses function."""
        # Mock the pickle.load function to return sample data
        with patch('pickle.load', return_value={"Player1": 3, "Player2": 2}):
            self.highscore_instance.load_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {"Player1": 3,
                                                                    "Player2": 2})

    def test_load_losses_file_not_found(self):
        """Test the load_losses function when the file is not found."""
        # Mock the pickle.load function to raise FileNotFoundError
        with patch('pickle.load', side_effect=FileNotFoundError):
            self.highscore_instance.load_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {})

    def test_load_losses_eof_error(self):
        """Test the load_losses function when EOFError is raised."""
        # Mock the pickle.load function to raise EOFError
        with patch('pickle.load', side_effect=EOFError):
            self.highscore_instance.load_losses()
            self.assertEqual(self.highscore_instance.get_losses(), {})

    def test_get_highscore(self):
        """Test the get_highscore function."""
        self.assertEqual(self.highscore_instance.get_highscore(), {})

    def test_get_losses(self):
        """Test the get_losses function."""
        self.assertEqual(self.highscore_instance.get_losses(), {})


if __name__ == '__main__':
    unittest.main()