"""This module contains the rules of the game."""

from colors import colors


class Rules:
    """This class contains the rules of the game."""
    def __init__(self):  # pragma: no cover
        self.rules = "You can play the game with 1 players with the computer\nYou can" \
            "play the game with 2 players\nFirst player to get 100 points wins\nIf " \
            "You roll a 1, you lose all your points for that turn\nIf you hold," \
            "you keep your points for that turn"
        # prints the rules of the game

    def show_rules(self):  # pragma: no cover
        """Prints the rules of the game."""
        print(colors.PINK + "**RULES OF PIG GAME**" + colors.RESET)
        print(colors.YELLOW + "********************************************" +
              colors.RESET)
        print(colors.BLUE + "You can play the game with 1 player with the computer" +
              colors.RESET)
        print(colors.BLUE + "You can play the game with 2 players" +
              colors.RESET)
        print(colors.BLUE + "First player to get 100 points wins" +
              colors.RESET)
        print(colors.GREEN + "If you roll a 1, you lose all your points for that turn" +
              colors.RESET)
        print(colors.BLUE + "If you hold, you keep your points for that turn" +
              colors.RESET)
        print(colors.YELLOW + "*********************************************"
              + colors.RESET)

    def get_rules(self):  # pragma: no cover
        return self.rules
