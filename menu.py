"""This is a module for the menu of the game."""
from colors import colors
from Rules import Rules
from player_vs_player import player_vs_player
from player_vs_computer import player_vs_computer
from highscore import highscore


class Menu:
    """This is a class for the menu of the game."""
    stupid_dict = {}

    def back_to_menu(self):
        """Generate the back to menu text."""
        back = input("Press enter to go back to the menu: ")
        if back == "":
            return
        else:
            print("Invalid input. Please press enter to "
                  + "go back to the menu.")

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

    def start_game(self):
        """Start the game."""
    stupid_dict = {}
    chart = highscore()

    print("Welcome to a Game of Pig!")
    print(colors.RED + "         __,---.__")
    print("    __,-'         `-.")
    print("   /_ /_,'           \\&")
    print("   _,''               \\")
    print("  (\")            .    |")
    print("    ``--|__|--..-'`.__|\n" + colors.RESET)

    print("Press any key to start the game.")
    input()
    while True:
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
        print(menu_text)
        try:
            user_choice = int(input("Enter your choice: \n"))

            if user_choice == 1:
                print("Player Vs Computer")
                game = player_vs_computer()
                wut = game.player_vs_computer_game()
                print(wut)

            if user_choice == 2:
                print("Player Vs Player")
                new_game = player_vs_player()
                winner = new_game.two_player_game()

            if user_choice == 3:
                the_rules = Rules()
                the_rules.show_rules()
                back = input("Press enter to go back to the menu: ")
                if back == "":
                    continue
                else:
                    print("Invalid input. Please press enter to "
                          + "go back to the menu.")

            if user_choice == 4:
                print("Highscore")
                try:
                    chart.add_highscore(winner, stupid_dict)
                    back = input("Press enter to go back to the menu: ")
                    if back == "":
                        continue
                    else:
                        print("Invalid input. Please press enter to "
                              + "go back to the menu.")
                except UnboundLocalError:
                    print("No winner yet!")
                    continue

            if user_choice == 5:
                print("Change name")
                back = input("Press enter to go back to the menu: ")
                if back == "":
                    continue
                else:
                    print("Invalid input. Please press enter to "
                          + "go back to the menu.")

            if user_choice == 6:
                print("Goodbye! Oink, oink!")
                break

            if user_choice not in [1, 2, 3, 4, 5, 6]:
                print("Invalid input. Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.") 
