import matplotlib.pyplot as plt


class FoundWord:
    """
    This class will hold the x and y positions (in pixels) for the first and last letter for a given word
    in the word search.
    """

    def __init__(self, first_grid_x, first_grid_y, last_grid_x, last_grid_y, word, error_count):
        """
        Constructor for FoundWord objects.
        :param first_grid_x: The column of the first letter in the word search grid.
        :param first_grid_y: The row of the first letter in the word search grid.
        :param last_grid_x: The column of the last letter in the word search grid.
        :param last_grid_y: The row of the last letter in the word search grid.
        """
        self.first_grid_x = first_grid_x
        self.first_grid_y = first_grid_y
        self.last_grid_x = last_grid_x
        self.last_grid_y = last_grid_y
        self.word = word
        self.error_count = error_count
        self.color = 'K'

    def draw_line(self, letter_size):
        """
        Plots a line from the coordinates of the first letter to the coordinates of the last letter.
        """
        plt.plot(self.grid_coordinates_to_pixels([self.first_grid_x, self.last_grid_x], letter_size),
                 self.grid_coordinates_to_pixels([self.first_grid_y, self.last_grid_y], letter_size), color=self.color)

    @staticmethod
    def letter_to_int(letter):
        """
        converts a character to an integer value (A = 1; B = 2; ect.)
        :param letter: The letter as a char to be converted to an int
        :return:
        """
        return ord(letter) - 64

    def grid_coordinates_to_pixels(self, grid_coordinates, letter_size):
        """
        Converts grid coordinates (ie. [5, 11]) to a pixel coordinate using letter_size in pixels as a scale
        :param grid_coordinates: The list of grid coordinates to be converted
        :param letter_size: The number of pixels used to represent a single row or column of a letter in the image
        of the word search.
        :return: A list of pixel coordinates
        """
        pixel_coordinates = []
        for grid_coordinate in grid_coordinates:
            pixel_coordinates.append(self.to_pixel_coordinates(grid_coordinate, letter_size))

        return pixel_coordinates

    @staticmethod
    def to_pixel_coordinates(i, letter_size):
        """
        Calculates the pixel coordinates of a given row or column based off the size of the word search grid.
        :return: The pixel coordinates of a given row or column
        """
        return (i * letter_size) + (letter_size / 2)










