import pickle
from colors import colors


class highscore:
    """Class for highscore."""
    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}
        self.losses = {}
        self.wins = {}

    def change_name(self, old_name):
        print("Change the name of the player.")
        print(f"{old_name} wishes to change name.")
        boolean = True
        while boolean:
            new_name = input("Enter the new name: ")
            if new_name == old_name:
                print("The name is the same.")
                continue
            else:
                print(f"{new_name} is the new name.")
                boolean = False
        if old_name in self.highscore_dict:
            self.highscore_dict[new_name] = self.highscore_dict.pop(old_name)
        if old_name in self.losses:
            self.losses[new_name] = self.losses.pop(old_name)

        for name, score in self.highscore_dict.items():
            print(name, score)
        for name, score in self.losses.items():
            print(name, score)

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

    def show_losses(self):
        """Show the losses."""
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
