from menu import Menu
from Rules import Rules
from playervsplayer import playervsplayer


def main():
    """Main function for the program."""
    if __name__ == "__main__":
        print("Welcome to a Game of Pig!")
        press_enter = input("Press enter to continue.")
        if press_enter == "":
            while True:
                the_menu = Menu()
                the_menu.show_menu()

                try:
                    user_choice = int(input("Enter your choice: "))

                    if user_choice == 1:
                        print("Player Vs Computer")

                    if user_choice == 2:
                        print("Player Vs Player")

                        new_game = playervsplayer()
                        result = new_game.two_player_game()
                        print(result)

                    if user_choice == 3:
                        the_rules = Rules()
                        print(the_rules)

                        back = input("Press any key to go back to the menu: ")
                        if back == "":
                            continue
                        else:
                            print("Invalid input. Please press any key to go back to the menu.")

                    if user_choice == 4:
                        print("Highscore")

                    if user_choice == 5:
                        print("Change name")

                    if user_choice == 6:
                        print("Exit")
                        break

                    if user_choice != 1 or 2 or 3 or 4 or 5 or 6:
                        print("Invalid input. Please enter a number between 1 and 7.")

                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 7.")


main()
