"""This is a module for the menu of the game."""
from colors import colors


class Menu:
    """This is a class for the menu of the game."""

    def __init__(self):
        """This class initializes the menu of the game."""
        pass

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
        menu_text = (
            f"{colors.PINK}{colors.TextStyles.BOLD}" + "Welcome to a game of Pig!" + colors.RESET + "\n"
            f"{colors.YELLOW}" + "*************************" + colors.RESET + "\n"
            f"{colors.BLUE}{colors.TextStyles.ITALIC}" + "* 1. Player Vs Computer *" + colors.RESET + "\n"
            f"{colors.BLUE}{colors.TextStyles.ITALIC}" + "* 2. Player Vs Player   *" + colors.RESET + "\n"
            f"{colors.BLUE}{colors.TextStyles.ITALIC}" + "* 3. Rules              *" + colors.RESET + "\n"
            f"{colors.BLUE}{colors.TextStyles.ITALIC}" + "* 4. Highscore          *" + colors.RESET + "\n"
            f"{colors.BLUE}{colors.TextStyles.ITALIC}" + "* 5. Change name        *" + colors.RESET + "\n"
            f"{colors.YELLOW}{colors.TextStyles.ITALIC}" + "*************************" + colors.RESET + "\n"
            f"{colors.GREEN}{colors.TextStyles.ITALIC}" + "* 6. Exit               *" + colors.RESET + "\n"
            f"{colors.YELLOW}{colors.TextStyles.ITALIC}" + "*************************" + colors.RESET + "\n"
        )
        return menu_text

    def show_credits(self):
        """Generate the credits text."""
        credits = (
            f"{colors.PINK}{colors.TextStyles.BOLD}Thank you for playing Pig!{colors.RESET}\n"
            f"{colors.YELLOW}*************************{colors.RESET}\n"
            f"{colors.CYAN}{colors.TextStyles.ITALIC}***CREDITS TO STUDENT DEVELOPERS!***{colors.RESET}\n"
            f"{colors.YELLOW}*************************{colors.RESET}\n"
            f"{colors.GREEN}{colors.TextStyles.ITALIC}* ~Frida Johannesson~{colors.RESET}\n"
            f"{colors.GREEN}{colors.TextStyles.ITALIC}* ~Merjam Farj-Beibani~{colors.RESET}\n"
            f"{colors.GREEN}{colors.TextStyles.ITALIC}* ~Sara Shmerti~{colors.RESET}\n"
            f"{colors.YELLOW}*************************{colors.RESET}\n"
            f"{colors.PINK}{colors.TextStyles.BOLD}Goodbye!{colors.RESET}"
)
        return credits
