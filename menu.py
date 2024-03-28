"""This is a module for the menu of the game."""

from colors import colors


class Menu:
    """This is a class for the menu of the game."""

    def __init__(self):
        """Menu constructor."""
        self.menu_options = [
            (colors.BLUE, "Player Vs Computer"),
            (colors.BLUE, "Player Vs Player"),
            (colors.BLUE, "Rules"),
            (colors.BLUE, "Highscore"),
            (colors.BLUE, "Change name"),
            (colors.GREEN, "Exit")
        ]

    def show_menu(self):
        """Show the menu."""
        for color, option in self.menu_options:
            print(color + option + colors.RESET)
