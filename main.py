"""Main module of the program."""
from menu import Menu


def main():
    """Run the main function."""
    menu = Menu()
    menu.show_menu()

    user_choice = int(input("Select an option: "))
    result_of_menu_choice = menu.menu_choices(user_choice)
    print(result_of_menu_choice)
    print(f"You chose: {user_choice}")


if __name__ == "__main__":
    main()