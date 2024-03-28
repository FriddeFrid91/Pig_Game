"""This is a module for the menu of the game."""

from colors import colors


class Menu:
    """This is a class for the menu of the game."""

    def __init__(self):
        """Menu constructor."""
        self.menu_options = [
            (colors.BLUE, "1. Player Vs Computer"),
            (colors.BLUE, "2. Player Vs Player"),
            (colors.BLUE, "3. Rules"),
            (colors.BLUE, "4. Highscore"),
            (colors.BLUE, "5. Change name"),
            (colors.GREEN, "6. Exit")
        ]

    def show_menu(self):
        """Show the menu."""
        for color, option in self.menu_options:
            print(colors.YELLOW, color + option + colors.RESET)
