"""Module for highscore."""
import pickle
from colors import colors


class highscore:
    """Class for highscore."""

    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}
        self.losses = {}
        self.wins = {}

    def change_name(self):
        """Change the name of the player at the highscore board."""
        print("Change the name of the player. \n")
        name_loop = True
        while name_loop:
            self.show_losses(), self.show_highscore()
            old_name = input("Enter name you want to change (quit for quit): \n")

            if old_name == "":
                print("Please enter a name from the scoreboard. \n")
                continue
            elif old_name.lower() == "quit":
                print("Quitting the name change. \n")
                return
            elif old_name in self.highscore_dict or old_name in self.losses:
                print(f"{old_name}\n")
                name_loop = False
            else:
                print("The name is not in the highscore table. \n")
                continue

        boolean = True
        print(f"{old_name} is the old name.\n")
        while boolean:
            new_name = input("Enter the new name: \n")
            if new_name == old_name:
                print("The name is the same as the old name.\n")
                continue
            elif new_name in self.highscore_dict or new_name in self.losses:
                print("The name is already in the highscore table.\n")
                continue
            else:
                print(f"{new_name} is the new name.\n")
                boolean = False

        if old_name in self.highscore_dict:
            self.highscore_dict[new_name] = self.highscore_dict.pop(old_name)
        if old_name in self.losses:
            self.losses[new_name] = self.losses.pop(old_name)
        # pragma: no cover
        try:
            with open("highscore.pkl", "wb") as file:
                pickle.dump(self.highscore_dict, file)
        except (FileNotFoundError, EOFError):
            print("No highscore at the moment.")

        try:
            with open("losses.pkl", "wb") as file:
                pickle.dump(self.losses, file)
        except (FileNotFoundError, EOFError):
            print("No highscore at the moment.")
        print(">> The name has been changed and the highscore table board updated <<\n")
        self.show_losses(), self.show_highscore()

    def show_losses(self):
        """Show the losses for all players."""
        hall_of_fame = [
            colors.BLUE + "*****************" + colors.RESET + "\n" +
            colors.BLUE + "* HALL OF SHAME *" + colors.RESET + "\n" +
            colors.BLUE + "*****************" + colors.RESET]
        print("\n".join(hall_of_fame))
        print(f"{'Name':8}: {'Losses':>6}")
        for sorted_losses in sorted(self.losses,
                                    key=self.losses.get,
                                    reverse=True):
            print(f"{sorted_losses:8}: {self.losses[sorted_losses]:>6}")

    def add_losses(self, loser):
        """Update the losses."""
        self.load_losses()
        if loser == "":
            return
        if loser in self.losses:
            self.losses[loser] += 1
        else:
            self.losses[loser] = 1
        try:
            with open("losses.pkl", "wb") as file:
                pickle.dump(self.losses, file)
        except FileNotFoundError:
            print("No lowscores at the moment.")
        except EOFError:
            print("No lowscores at the moment.")
            loser = ""
        return loser is None

    def load_losses(self):
        """Load the losses."""
        try:
            with open("losses.pkl", "rb") as file:
                self.losses = pickle.load(file)
        except FileNotFoundError:
            print("No highscore at the moment")
        except EOFError:
            print("No highscore at the moment")
        return self.losses

    def show_highscore(self):
        """Show the highscore."""
        hall_of_fame = [
            colors.YELLOW + "****************" + colors.RESET + "\n" +
            colors.YELLOW + "* HALL OF FAME *" + colors.RESET + "\n" +
            colors.YELLOW + "****************" + colors.RESET]

        print("\n".join(hall_of_fame))

        print(f"{'Name':8}: {'Wins':>6}")
        for sorted_scores in sorted(self.highscore_dict,
                                    key=self.highscore_dict.get,
                                    reverse=True):
            if sorted_scores is not None:
                print(f"{sorted_scores:8}: {self.highscore_dict[sorted_scores]:>6}")
            else:
                return

    def add_highscore(self, winner):
        """Add the winner to the highscore."""
        self.load_highscore()
        if winner == "" or winner is None:
            return
        if winner in self.highscore_dict:
            self.highscore_dict[winner] += 1
        else:
            self.highscore_dict[winner] = 1
        try:
            with open("highscore.pkl", "wb") as file:
                pickle.dump(self.highscore_dict, file)
        except FileNotFoundError:
            self.highscore_dict = {}
        except EOFError:
            self.highscore_dict = {}
            winner = ""
        return winner is None

    def load_highscore(self):
        """Load the highscore."""
        try:
            with open("highscore.pkl", "rb") as file:
                self.highscore_dict = pickle.load(file)
        except FileNotFoundError:
            self.highscore_dict = {}
        except EOFError:
            self.highscore_dict = {}
        return self.highscore_dict

    def get_highscore(self):
        """Get the highscore."""
        return self.highscore_dict

    def get_losses(self):
        """Get the losses."""
        return self.losses
