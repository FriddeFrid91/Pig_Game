"""Main module for the program."""
from menu import Menu
from Rules import Rules
from player_vs_player import player_vs_player
from player_vs_computer import player_vs_computer
from highscore import highscore
from colors import colors


def main():
    """Doing what the main function does."""
    chart = highscore()
    winner = ""

    piggy = Menu()
    pig = piggy.show_pig()
    print(pig)

    print(colors.BLUE
          + colors.TextStyles.BOLD
          + colors.TextStyles.ITALIC
          + "Press any key to start the game."
          + colors.RESET)
    input()
    while True:
        the_menu = Menu()
        menu = the_menu.show_menu()
        print(menu)

        try:
            user_choice = int(input(colors.PINK
                                    + colors.TextStyles.ITALIC
                                    + colors.TextStyles.BOLD
                                    + "Enter your choice: \n"
                                    + colors.RESET))

            if user_choice == 1:
                print(colors.BLUE + colors.TextStyles.BOLD
                      + "Player Vs Computer" + colors.RESET)
                boolean = True
                while boolean:
                    difficulty = input(colors.RED
                                       + "Enter the difficulty level "
                                       + "(easy, medium, hard): "
                                       + colors.RESET)
                    if difficulty.lower() not in ["easy", "medium", "hard"]:
                        print(colors.RED
                              + "Invalid input. Please try again. "
                              + "easy, medium, or hard." + colors.RESET)
                        continue

                    else:
                        boolean = False
                game = player_vs_computer()
                game.player_vs_computer_game(difficulty)

            if user_choice == 2:
                print(colors.BLUE + colors.TextStyles.BOLD
                      + "Player Vs Player" + colors.RESET)
                
                boolean = True
                while boolean:
                    player_1 = input(colors.CYAN + "Enter the name "
                                     + "of player 1: " + colors.RESET)
                    if len(player_1) < 2 or len(player_1) > 10 or player_1 == "":
                        print(colors.BLUE + "Please enter a between "
                              + "2 and 10 characters." + colors.RESET)
                        continue
                    else:
                        confirm_name = input(f"Is {player_1} the correct name (yes/no)? ")
                        if confirm_name.lower() == "no":
                            continue
                        elif confirm_name.lower() == "yes":
                            boolean = False
                        else:
                            print(colors.RED + "Invalid input. Please write the name again."
                                  + colors.RESET)
                            continue
                boolean = True
                while boolean:
                    player_2 = input(colors.CYAN + "Enter the name "
                                     + "of player 2: " + colors.RESET)
                    if len(player_2) < 2 or len(player_2) > 10 or player_2 == "":
                        print(colors.BLUE + "Please enter a between "
                              + "2 and 10 characters." + colors.RESET)
                        continue
                    elif player_2 == player_1:
                        print(colors.RED + "The name can't be the same as player 1!"
                              + colors.RESET)
                        continue
                    else:
                        confirm_name = input(f"Is {player_2} the correct name (yes/no)? ")
                        if confirm_name.lower() == "no":
                            continue
                        elif confirm_name.lower() == "yes":
                            boolean = False
                        else:
                            print(colors.RED + "Invalid input. Please write the name again."
                                  + colors.RESET)
                            continue
                new_game = player_vs_player()
                winner = new_game.two_player_game(player_1, player_2)
                loser = new_game.get_loser()
                try:
                    chart = highscore()
                    chart.add_highscore(winner)
                    chart.add_losses(loser)
                except UnboundLocalError:
                    pass

            if user_choice == 3:
                # Display the rules of the game.
                the_rules = Rules()
                print(the_rules)
                print(colors.BLUE + colors.TextStyles.BOLD + "Press any "
                      + "key to go back to the menu." + colors.RESET)
                input()

            if user_choice == 4:
                # Display the highscore board.
                chart.load_highscore()
                chart.load_losses()
                chart.show_highscore()
                chart.show_losses()
                print(colors.BLUE + colors.TextStyles.BOLD + "Press any key"
                      + " to go back to the menu." + colors.RESET)
                input()

            if user_choice == 5:
                # Change the name of the player in the highscore board.
                print(colors.CYAN + "Change name" + colors.RESET)
                chart.load_highscore()
                chart.load_losses()
                chart.change_name()
                print(colors.BLUE + "Press any key to go back to the menu."
                      + colors.RESET)
                input()

            if user_choice == 6:
                # Display the credits and quit the game.
                student_credit = piggy.credits_message()
                print(student_credit)
                break

            if user_choice not in [1, 2, 3, 4, 5, 6]:
                print(colors.RED + "Invalid input. Please enter a number "
                      + "between 1 and 6." + colors.RESET)

        except ValueError:
            print(colors.RED + "Invalid input. Please enter a "
                  + "number between 1 and 6." + colors.RESET)


if __name__ == "__main__":
    main()
