import pickle


class highscore:
    """Class for highscore."""
    def __init__(self):
        """Initialize the highscore."""
        self.highscore_dict = {}
        self.highscore_name = ""

    def add_highscore(self, name):
        """Add a highscore."""

        if name in self.highscore_dict:
            self.highscore_dict[name] += 1
        else:
            self.highscore_dict[name] = 1

        with open("highscore.txt", "wb") as file:
            pickle.dump(self.highscore_dict, file)

    def get_highscore(self):
        """Get the highscore."""
        with open("highscore.txt", "rb") as file:
            self.highscore_dict = pickle.load(file)
        return self.highscore_dict

    def recent_winner(self, name):
        """Set the recent winner."""
        self.highscore_name = name
        print(name)

    def __str__(self):
        return f"Most recent winner is: {self.highscore_name}."
