"""This is a module for the menu of the game."""
from colors import colors


class Menu:
    """Menu class."""

    def __init__(self):
        """Menu constructor."""
        self.menu_options = 0

    """This is a class for the menu of the game."""

    def show_pig(self):
        """Show the pig."""
        ascii_pig = ""
        ascii_pig += colors.PINK + colors.TextStyles.BOLD + colors.TextStyles.ITALIC + ">> A GAME OF PIG <<\n" + colors.RESET
        ascii_pig += colors.PINK + "       __,---.__" + "\n"
        ascii_pig += "  __,-'         `-." + "\n"
        ascii_pig += " /_ /_,'           \\&" + "\n"
        ascii_pig += " _,''               \\" + "\n"
        ascii_pig += "(\")            .    |" + "\n"
        ascii_pig += "  ``--|__|--..-'`.__|\n" + colors.RESET + "\n"
        return ascii_pig

    def show_menu(self):
        """Generate the menu text."""
        menu_text = ""
        menu_text += colors.PINK + colors.TextStyles.BOLD + "Welcome to a game of Pig!" + colors.RESET + "\n"
        menu_text += colors.YELLOW + "*************************" + colors.RESET + "\n"
        menu_text += colors.BLUE + colors.TextStyles.ITALIC + "* 1. Player Vs Computer *" + colors.RESET + "\n"
        menu_text += colors.BLUE + colors.TextStyles.ITALIC + "* 2. Player Vs Player   *" + colors.RESET + "\n"
        menu_text += colors.BLUE + colors.TextStyles.ITALIC + "* 3. Rules              *" + colors.RESET + "\n"
        menu_text += colors.BLUE + colors.TextStyles.ITALIC + "* 4. Highscore          *" + colors.RESET + "\n"
        menu_text += colors.BLUE + colors.TextStyles.ITALIC + "* 5. Change name        *" + colors.RESET + "\n"
        menu_text += colors.YELLOW + colors.TextStyles.ITALIC + "*************************" + colors.RESET + "\n"
        menu_text += colors.GREEN + colors.TextStyles.ITALIC + "* 6. Exit               *" + colors.RESET + "\n"
        menu_text += colors.YELLOW + colors.TextStyles.ITALIC + "*************************" + colors.RESET + "\n"
        return menu_text

    def credits_message(self):
        """Return the credits message."""
        message = (
            colors.PINK + colors.TextStyles.BOLD + "Thank you "
            + "for playing Pig!" + colors.RESET + "\n"
            + colors.YELLOW + "*************************" + colors.RESET + "\n"
            + colors.CYAN + colors.TextStyles.ITALIC
            + "***CREDITS TO STUDENT DEVELOPERS!***" + colors.RESET + "\n"
            + colors.YELLOW + "*************************" + colors.RESET + "\n"
            + colors.GREEN + colors.TextStyles.ITALIC
            + "* ~Frida Johannesson~" + colors.RESET + "\n"
            + colors.GREEN + colors.TextStyles.ITALIC
            + "* ~Merjam Farj-Beibani~" + colors.RESET + "\n"
            + colors.GREEN + colors.TextStyles.ITALIC
            + "* ~Sara Shmerti~" + colors.RESET + "\n"
            + colors.YELLOW + "*************************" + colors.RESET + "\n"
            + colors.PINK + colors.TextStyles.BOLD + "Goodbye!" + colors.RESET)
        return message
