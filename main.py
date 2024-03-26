<<<<<<< HEAD

"""Main module of the program."""
=======
"""Main function for the program."""
>>>>>>> FriddeFrid_branch
from menu import Menu
from Rules import Rules


def main():
    """Functionality for menu in menu."""
    print("Hello World!")

    while True:
        the_menu = Menu()
        the_menu.show_menu()

        try:
            user_choice = int(input("Enter your choice: "))

            if user_choice == 1:
                print("Player Vs Computer")

            if user_choice == 2:
                print("Player Vs Player")

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


if __name__ == "__main__":
    main()
<<<<<<< HEAD


 
=======
>>>>>>> FriddeFrid_branch
