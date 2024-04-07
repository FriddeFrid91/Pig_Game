import pickle
from colors import colors


class highscore:
    """Class for highscore."""
    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}
        self.losses = {}
        self.wins = {}

    def show_losses(self):
        """Show the losses."""
        print(colors.YELLOW + "****************" + colors.RESET)
        print(colors.YELLOW + "* LOSER BOARD *" + colors.RESET)
        print(colors.YELLOW + "****************" + colors.RESET)
        print(f"{'Name':8}: {'Losses':>6}")
        for sorted_losses in sorted(self.losses,
                                    key=self.losses.get,
                                    reverse=True):
            print(f"{sorted_losses:8}: {self.losses[sorted_losses]:>6}")

    def add_losses(self, loser):
        """Update the losses."""
        self.show_losses()
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
            self.losses = {}
        except EOFError:
            self.losses = {}
        return loser is None

    def load_losses(self):
        """Load the losses."""
        try:
            with open("losses.pkl", "rb") as file:
                self.losses = pickle.load(file)
        except FileNotFoundError:
            self.losses = {}
        except EOFError:
            self.losses = {}
        return self.losses

    def show_highscore(self):
        """Show the highscore."""
        print(colors.YELLOW + "****************" + colors.RESET)
        print(colors.YELLOW + "* HALL OF FAME *" + colors.RESET)
        print(colors.YELLOW + "****************" + colors.RESET)
        print(f"{'Name':8}: {'Wins':>6}")
        for sorted_scores in sorted(self.highscore_dict,
                                    key=self.highscore_dict.get,
                                    reverse=True):
            print(f"{sorted_scores:8}: {self.highscore_dict[sorted_scores]:>6}")

    def add_highscore(self, winner):
        """Add the winner to the highscore."""
        self.load_highscore()
        if winner == "":
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
