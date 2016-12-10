import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from found_word import FoundWord
from search import Search
from given_methods import GivenMethods


class WordSearch:
    """
    This class contains the word search (in multiple formats) and a list of found words within the word search.
    """

    def __init__(self, pixel_matrix, letter_size, words, train_data, train_labels):
        """
        Creates a word search object from an image of a word search, the size of each letter (in pixels),
        all of the words to be found and training data.
        :param pixel_matrix: The image of the word search to be solved.
        :param letter_size: The size of each letter in the word search grid (in pixels).
        :param words: The list of words to find in the word search.
        :param train_data: The training data
        :param train_labels: The training labels
        """

        self.pixel_matrix = pixel_matrix
        self.letter_size = letter_size
        self.grid_size = int(len(pixel_matrix) / self.letter_size)
        self.words = words
        self.letter_pixels = self.get_letters_from_image(pixel_matrix)
        self.word_search_grid = np.reshape(GivenMethods.classify(train_data, train_labels, self.letter_pixels),
                                           (self.grid_size, self.grid_size), order='F')
        self.found_words = []
        print(self.word_search_grid)

    def get_letters_from_image(self, matrix):
        """
        Takes a matrix representing a word search. Letters must be equally spaced in a grid
        and each letter must be contained within the grid boundaries (letter_size x letter_size)

        :param matrix: matrix representing a word search grid
        :return: a list of all of the pixels for each character in the grid.
        """

        letters = []

        for letter_row in range(0, len(matrix), self.letter_size):
            for letter_col in range(0, len(matrix[0]), self.letter_size):
                letter = []
                for pixel_row in range(letter_row, letter_row + self.letter_size):
                    for pixel_col in range(letter_col, letter_col + self.letter_size):
                        letter.append(matrix[pixel_col][pixel_row])
                letters.append(letter)

        return np.array(letters)

    def find_word(self, word):
        """
        Searches an entire word search grid for a single word
        :param word_search: The word search grid
        :param word: The word to be searched for
        """
        found = False

        for y in range(0, len(self.word_search_grid)):
            for x in range(0, len(self.word_search_grid[0])):
                if self.word_search_grid[y][x] == FoundWord.letter_to_int(word[0]):
                    if self.find_word_at_point(word, x, y):
                        found = True
                        break
            if found:
                break

    def find_word_at_point(self, word, x, y):
        """
        Searches horizontally, vertically and diagonally to try and find a given word from a given letter
        in a word search (given letter location)
        :param word_search: The word search
        :param word: The word that is being search for
        :param x: The x pos of the start letter in the word search grid
        :param y: The y pos of that start letter in the word search grid
        :return: True if the given word was found at the given letter position, otherwise false
        """
        letter_is_word = False

        found_word = Search.look_horizontal(self.word_search_grid, word, x, y)
        if found_word is not None:
            letter_is_word = True
        else:
            found_word = Search.look_vertical(self.word_search_grid, word, x, y)
            if found_word is not None:
                letter_is_word = True
            else:
                found_word = Search.look_diagonal(self.word_search_grid, word, x, y)
                if found_word is not None:
                    letter_is_word = True

        if found_word is not None:
            self.found_words.append(found_word)
            print(x, y, word)

        return letter_is_word

    def solve(self):
        for word in self.words:
            self.find_word(word.upper())

    def show(self):
        plt.imshow(self.pixel_matrix, cmap=cm.Greys_r)
        for word in self.found_words:
            word.draw_line(self.letter_size)
        plt.show()



































