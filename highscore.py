import pickle
from colors import colors
from Player import Player


class highscore:
    """Class for highscore."""
    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}
        self.winner = Player("", 0)

    def add_highscore(self, winner, highscore_dict):
        """Add a highscore."""
        try:
            with open("highscore.txt", "rb") as file:
                highscore_table = pickle.load(file)
        except FileNotFoundError:
            highscore_table = {}

        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "*********** HIGHSCORE ***********" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "********* HALL OF FAME **********" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        
        highscore_table.update

        if winner in highscore_dict:
            highscore_dict[winner] += 1
        else:
            highscore_dict[winner] = 1

        with open("highscore.txt", "wb") as file:
            pickle.dump(highscore_dict, file)

        with open("highscore.txt", "rb") as file:
            highscore_table = pickle.load(file)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "*********** HIGHSCORE ***********" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "********* HALL OF FAME **********" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        for name, wins in highscore_table.items():
            print(f"{name}: {wins}")
