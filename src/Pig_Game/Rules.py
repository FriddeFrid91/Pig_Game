"""This module contains the rules of the game."""

from colors import colors


class Rules:
    """This class contains the rules of the game."""
    def __init__(self):
        self.rules = []

    def show_rules(self):
        rules = [
          colors.PINK + "**RULES OF PIG GAME**" + colors.RESET,
          colors.YELLOW + "********************************************" + colors.RESET,
          colors.BLUE + "You can play the game with 1 player with the computer"
          + colors.RESET,
          colors.BLUE + "You can play the game with 2 players" + colors.RESET,
          colors.BLUE + "First player to get 100 points wins" + colors.RESET,
          colors.GREEN + "If you roll a 1, you lose all your points for that turn"
          + colors.RESET,
          colors.BLUE + "If you hold, you keep your points for that turn"
          + colors.RESET,
          colors.YELLOW + "*********************************************"
          + colors.RESET]
        return rules

    def __str__(self):
        return "\n".join(self.show_rules())
