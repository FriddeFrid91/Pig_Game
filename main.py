from menu import Menu
from Rules import Rules
from player_vs_player import player_vs_player
from player_vs_computer import player_vs_computer
from highscore import highscore
from colors import colors


def main():
    """Main function for the program."""

    chart = highscore()
    winner = ""

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
                game.player_vs_computer_game()

            if user_choice == 2:
                print("Player Vs Player")
                boolean = True
                while boolean:
                    player_1 = input("Enter the name of player 1: ")
                    if player_1 == "":
                        print("Please enter a name: ")
                        continue
                    else:
                        boolean = False

                boolean = True
                while boolean:
                    player_2 = input("Enter the name of player 2: ")
                    if player_2 == "":
                        print("Please enter a name: ")
                        continue
                    elif player_2 == player_1:
                        print("Oink, oink! You can't have the same name as player 1!")
                        continue
                    else:
                        boolean = False

                    new_game = player_vs_player()
                    winner = new_game.two_player_game(player_1, player_2)
                    loser = new_game.get_loser()
                    print(f"{winner} wins!")
                    print(f"{loser} loses!")

            if user_choice == 3:
                the_rules = Rules()
                the_rules.show_rules()
                print("Press any key to go back to the menu.")
                input()

            if user_choice == 4:
                try:
                    chart.add_highscore(winner)
                    chart.add_losses(loser)
                    chart.scoreboard()
                    winner = ""
                    loser = ""
                    print("Press any key to go back to the menu.")
                    input()
                except UnboundLocalError:
                    chart.scoreboard()
                    print("Press any key to go back to the menu.")
                    input()

            if user_choice == 5:
                print("Change name")
                print("Press any key to go back to the menu.")
                input()

            if user_choice == 6:
                print("Goodbye!")
                break

            if user_choice == 7:
                chart.scoreboard()

            if user_choice not in [1, 2, 3, 4, 5, 6, 7]:
                print("Invalid input. Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
