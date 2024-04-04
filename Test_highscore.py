import unittest
from highscore import highscore
from unittest.mock import patch, Mock


class test_highscore(unittest.TestCase):
    """Test class for highscore."""


show = highscore()


@patch('builtins.print')
def test_show_highscore(self, mocked_print):
    """Test the show highscore function."""

    show.show_highscore()

    expected_output = ["****************",
                       "* HALL OF FAME *",
                       "****************"]
    calls = [Mock(call=output) for output in expected_output]
    mocked_print.assert_has_calls(calls, any_order=False)


def test_load_highscore(self):
    """Test the load highscore function."""
    show.load_highscore()


def test_add_highscore(self, winner):
    """Test the add highscore function."""
    show.add_highscore(winner)


if __name__ == "main":
    unittest.main()
