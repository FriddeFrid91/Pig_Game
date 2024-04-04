"""Intelligence class for the AI of the game."""

import random


class Intelligence:
    """Class for the Intelligence move"""
    def __init__(self):
        pass

    def ai_move(self):
        """Method to get the AI move"""
        return random.randint(1, 6)

    def ai_hold(self):
        """Method to get the AI hold"""
        return random.randint(1, 6)

    def ai_name(self):
        """Method to get the AI name"""
        return "Computer"
