"""This is a module for the menu of the game."""


class Menu:
    """This is a class for the menu of the game."""

    def __init__(self):
        """Menu constructor."""
        self.menu_options = 0
    while True:
        def show_menu(self):

            """Show the menu."""
            print("_______________________")
            print("|   >>  Main Menu <<  |")
            print("|1. Player Vs Computer|")
            print("|2. Player Vs Player  |")
            print("|3. Rules             |")
            print("|4. Highscore         |")
            print("|---------------------|")
            print("|5. Exit              |")
            print("_______________________")
            
            self.menu_options = int(input("Select an option: "))

            if self.menu_options == 1:
                print("Player Vs Computer")

            elif self.menu_options == 2:
                print("Player Vs Player")
                pass

            elif self.menu_options == 3:
                print("Rules")
                pass

            elif self.menu_options == 4:
               print("Highscore")
               pass

            elif self.menu_options == 5:
               print("Goodbye!")
               break