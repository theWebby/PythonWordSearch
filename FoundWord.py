import matplotlib.pyplot as plt


class FoundWord:
    """
    This class will hold the x and y positions (in pixels) for the first and last letter for a given word
    in the word search.
    """

    def __init__(self, first_x, first_y, last_x, last_y):
        self.first_x = first_x
        self.first_y = first_y
        self.last_x = last_x
        self.last_y = last_y

    def draw_line(self):
        plt.plot([self.first_x, self.last_x], [self.first_y, self.last_y], color='K')

