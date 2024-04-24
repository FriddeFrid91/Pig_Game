"""This module contains the CheckingName class."""
from colors import colors


class CheckingName:
    """This class contains the checking_name function."""

    def __init__(self):
        """Empty constructor."""
        pass

    def checking_name_function(self):
        """Check the name of the players."""
        boolean = True
        while boolean:
            player_1 = input(colors.CYAN + "\nEnter the name of player 1: \n" + colors.RESET)
            if len(player_1) < 2 or len(player_1) > 10 or player_1 == "":
                print(colors.BLUE + "Please enter a name between 2 and 10 characters. \n" + colors.RESET)
                continue
            else:
                confirm_name = input(f"Is {player_1} " 
                                     + "the correct name (yes/no)?\n")
                if confirm_name.lower() == "no":
                    continue
                elif confirm_name.lower() == "yes":
                    boolean = False
                else:
                    print(colors.RED + "Invalid input. Please enter a name: \n"
                          + colors.RESET)
                    continue

        boolean = True
        while boolean:
            player_2 = input(colors.CYAN + "\nEnter the name of player 2: \n"
                             + colors.RESET)
            if len(player_2) < 2 or len(player_2) > 10 or player_2 == "":
                print(colors.BLUE + "Please enter a name between 2 and 10 characters. \n" + colors.RESET)
                continue
            elif player_2 == "quit":
                break
            elif player_2 == player_1:
                print(colors.RED + "The name can't be the same as player 1!\n" + colors.RESET)
                continue
            else:
                confirm_name = input(f"Is {player_2} the correct name (yes/no)?\n ")
                if confirm_name.lower() == "no":
                    continue
                elif confirm_name.lower() == "yes":
                    boolean = False
                else:
                    print(colors.RED + "Invalid input. Please enter a name: \n" + colors.RESET)
                    continue
        return player_1, player_2
