"""This is a module for the menu of the game."""

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default color



class Menu:
    """This is a class for the menu of the game."""

    def __init__(self):
        """Menu constructor."""
        self.menu_options = 0

    def show_menu(self):
        """Show the menu."""
        print(colors.PINK + "Welcome to a game of Pig!" + colors.RESET)
        print(colors.YELLOW + "*************************" + colors.RESET)
        print(colors.BLUE + "* 1. Player Vs Computer *" + colors.RESET)
        print(colors.BLUE + "* 2. Player Vs Player   *" + colors.RESET)
        print(colors.BLUE + "* 3. Rules              *" + colors.RESET)
        print(colors.BLUE + "* 4. Highscore          *" + colors.RESET)
        print(colors.BLUE + "* 5. Change name        *" + colors.RESET)
        print(colors.YELLOW + "*************************" + colors.RESET)
        print(colors.GREEN + "* 6. Exit               *" + colors.RESET)
        print(colors.YELLOW + "*************************" + colors.RESET)
