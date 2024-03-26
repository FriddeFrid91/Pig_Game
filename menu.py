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
        print("*************************")
        print("* 5. Exit               *")
        print("*************************")

    def menu_choices(self, user_choice):
        """Menu choices."""
        if user_choice == 1:
            return "Player Vs Computer"

        elif user_choice == 2:
            return "Player Vs Player"

        elif user_choice == 3:
            return "Rules"
       
        elif user_choice == 4:
            return "Highscore"
       
        elif user_choice == 5:
            return "Goodbye!"