import pickle
from colors import colors


class highscore:
    """Class for highscore."""
    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}

    def add_highscore(self, name):
        """Add a highscore."""
        highscore_list = [""]
        highscore_list.append(name)
        print(highscore_list)

        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "*********** HIGHSCORE ***********" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)
        print(colors.YELLOW + "********* HALL OF FAME **********" + colors.RESET)
        print(colors.YELLOW + "*********************************" + colors.RESET)

        if name in self.highscore_dict:
            self.highscore_dict[name] += 1
            self.highscore_dict.update(self.highscore_dict)
        else:
            self.highscore_dict[name] = 1
            self.highscore_dict.update(self.highscore_dict)

        with open("highscore.txt", "wb") as file:
            pickle.dump(self.highscore_dict, file)

        return self.highscore_dict

    def get_highscore(self):
        """Get the highscore."""
        with open("highscore.txt", "rb") as file:
            self.highscore_dict = pickle.load(file)

        for key, value in self.highscore_dict.items():
            print(f"WHAT {key}: {value}")

    def recent_winner(self, name):
        """Set the recent winner."""
        self.highscore_name = name
        print(name)

    def __str__(self):
        return f"Most recent winner is: {self.highscore_name}."
