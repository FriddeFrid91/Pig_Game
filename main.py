from menu import Menu
from Rules import Rules
from player_vs_player import player_vs_player
from player_vs_computer import player_vs_computer
from highscore import highscore
from colors import colors


def main():
    """Main function for the program."""
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
        the_menu = Menu()
        menu = the_menu.show_menu()

        print(menu)

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
                print(the_rules)

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
                except UnboundLocalError:
                    print("No winner yet!")
                    continue

            if user_choice == 5:
                print("Change name")

            if user_choice == 6:
                print("Exit")
                break

            if user_choice not in [1, 2, 3, 4, 5, 6]:
                print("Invalid input. Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
