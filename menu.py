"""This is a module for the menu of the game."""
from colors import colors


class Menu:
    """This is a class for the menu of the game."""

    def show_menu(self):
        """Generate the menu text."""
        menu_text = ""
        menu_text += colors.PINK + "A Game Of Pig" + colors.RESET + "\n"
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

    def back_to_menu(self):
        """Generate the back to menu text."""
        back = input("Press enter to go back to the menu: ")
        if back == "":
            return
        else:
            print("Invalid input. Please press enter to "
                  + "go back to the menu.")
