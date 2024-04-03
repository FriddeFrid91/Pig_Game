"""This is a module for the menu of the game."""
from colors import colors


class Menu:
    """Menu class."""
    def __init__(self):
        """Menu constructor."""
        self.menu_options = 0

    """This is a class for the menu of the game."""

    def show_menu(self):
        """Generate the menu text."""
        menu_text = ""
        menu_text += colors.PINK + "Welcome to a game of Pig!" + colors.RESET + "\n"
        menu_text += colors.YELLOW + "*************************" + colors.RESET + "\n"
        menu_text += colors.BLUE + "* 1. Player Vs Computer *" + colors.RESET + "\n"
        menu_text += colors.BLUE + "* 2. Player Vs Player   *" + colors.RESET + "\n"
        menu_text += colors.BLUE + "* 3. Rules              *" + colors.RESET + "\n"
        menu_text += colors.BLUE + "* 4. Highscore          *" + colors.RESET + "\n"
        menu_text += colors.BLUE + "* 5. Change name        *" + colors.RESET + "\n"
        menu_text += colors.YELLOW + "*************************" + colors.RESET + "\n"
        menu_text += colors.GREEN + "* 6. Exit               *" + colors.RESET + "\n"
        menu_text += colors.YELLOW + "*************************" + colors.RESET + "\n"

        return menu_text
