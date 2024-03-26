"""This is a module for the menu of the game."""


class Menu:
    """This is a class for the menu of the game."""

    def __init__(self):
        """Menu constructor."""
        self.menu_options = 0

    def show_menu(self):
        """Show the menu."""
        print("Welcome to a game of Pig!")
        print("*************************")
        print("* 1. Player Vs Computer *")
        print("* 2. Player Vs Player   *")
        print("* 3. Rules              *")
        print("* 4. Highscore          *")
        print("* 5. Change name        *")
        print("*************************")
        print("* 6. Exit               *")
        print("*************************")
