import pickle
from colors import colors


class highscore:
    """Class for highscore."""
    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}

    def show_highscore(self):
        """Show the highscore."""
        print(colors.YELLOW + "****************" + colors.RESET)
        print(colors.YELLOW + "* HALL OF FAME *" + colors.RESET)
        print(colors.YELLOW + "****************" + colors.RESET)
        for sorted_key in sorted(self.highscore_dict, key=self.highscore_dict.get,
                                 reverse=True):
            print(f"{sorted_key:8}: {self.highscore_dict[sorted_key]:>6}")

    def add_highscore(self, winner):
        """Add the winner to the highscore."""
        self.load_highscore()
        if winner == "":
            return
        if winner in self.highscore_dict:
            self.highscore_dict[winner] += 1
        else:
            self.highscore_dict[winner] = 1
        with open("highscore.pkl", "wb") as file:
            pickle.dump(self.highscore_dict, file)
        winner = ""
        return winner is None

    def load_highscore(self):
        """Load the highscore."""
        try:
            with open("highscore.pkl", "rb") as file:
                self.highscore_dict = pickle.load(file)
        except FileNotFoundError:
            self.highscore_dict = {}
        return self.highscore_dict
    
    def get_highscore(self):
        """Get the highscore."""
        return self.highscore_dict
