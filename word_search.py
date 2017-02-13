import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from found_word import FoundWord
from search import Search
from classifier import Classifier


class WordSearch:
    """
    This class contains the word search (in multiple formats) and a list of found words within the word search.
    """

    def __init__(self, pixel_matrix, letter_size, words, train_data, train_labels, dimred=False):
        """
        Creates a word search object from an image of a word search, the size of each letter (in pixels),
        all of the words to be found and training data.
        :param pixel_matrix: The image of the word search to be solved.
        :param letter_size: The size of each letter in the word search grid (in pixels).
        :param words: The list of words to find in the word search.
        :param train_data: The training data
        :param train_labels: The training labels
        :param dimred: When true a dimensionality reduction technique will be applied, false and it will not
        """

        self.pixel_matrix = pixel_matrix
        self.letter_size = letter_size
        self.grid_size = int(len(pixel_matrix) / self.letter_size)
        self.words = words
        self.letter_pixels = self.get_letters_from_image(pixel_matrix)

        # apply a dimension reduction technique
        if dimred:
            train_data, self.letter_pixels = self.reduce_dimensions(train_data, self.letter_pixels)

        # creating the word search represented as number in a matrix (1 = A; 2 = B; ect.)
        self.grid = np.reshape(Classifier.classify(train_data, train_labels, self.letter_pixels),
                               (self.grid_size, self.grid_size), order='F')

        self.found_words = []

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

    @staticmethod
    def reduce_dimensions(train_data, test_data):
        """
        Takes in training data and the test data and return the data with a reduced number of dimensions
        :param train_data: The training data
        :param test_data: The test data
        :return: reduced_train and reduced_test where the number of dimensions is less
        """
        nAxes = 10
        [pca_axes, mean_vector] = Classifier.learnPCA(train_data, nAxes)

        reduced_train = Classifier.reducePCA(train_data, pca_axes, mean_vector)
        reduced_test = Classifier.reducePCA(test_data, pca_axes, mean_vector)

        return reduced_train, reduced_test

    def find_word(self, word):
        """
        Searches an entire word search grid for a single word. This is done by looking for the first letter of the word
        and then checking if the word starts at that point in the grid.
        :param word: The word to be searched for.
        """
        found = False

        for y in range(0, self.grid_size):
            for x in range(0, self.grid_size):
                if self.grid[y][x] == FoundWord.letter_to_int(word[0]):
                    if self.find_word_at_point(word, x, y):
                        found = True
                        break
            if found:
                break

    def find_word_at_point(self, word, x, y):
        """
        Searches horizontally, vertically and diagonally to try and find a given word from a given grid point
        in the word search grid.
        :param word: The word that is being search for
        :param x: The x pos of the start letter in the word search grid
        :param y: The y pos of that start letter in the word search grid
        :return: True if the given word was found at the given letter position, otherwise false
        """
        letter_is_word = False
        local_words = [None] * 3

        # words with incorrect letters are not marked as found but can still be added to found_words
        local_words[0] = Search.look_horizontal(self.grid, word, x, y)
        if local_words[0] is not None and local_words[0].error_count == 0:
            letter_is_word = True
        else:
            local_words[1] = Search.look_vertical(self.grid, word, x, y)
            if local_words[1] is not None and local_words[1].error_count == 0:
                letter_is_word = True
            else:
                local_words[2] = Search.look_diagonal(self.grid, word, x, y)
                if local_words[2] is not None and local_words[2].error_count == 0:
                    letter_is_word = True

        #checks all of the words found from a point
        for found_word in local_words:
            if found_word is not None:
                self.found_words.append(found_word)
                if found_word.error_count > 0:  # to try and find a more accurate match for a word
                    letter_is_word = False

        return letter_is_word

    def filter_found_words(self):
        """
        This method will look through the list of found words for duplicate words and keep only the word with the lowest
         error tolerance.
        """
        words_to_delete = []

        self.found_words.sort(key=lambda x: x.error_count)

        for i in range(0, len(self.found_words) - 1):
            for j in range(i + 1, len(self.found_words)):
                if self.found_words[i].word == self.found_words[j].word:
                    #  duplicate words found
                    if self.found_words[i].error_count < self.found_words[j].error_count:
                        words_to_delete.append(self.found_words[j])
                    elif self.found_words[i].error_count > self.found_words[j].error_count:
                        words_to_delete.append(self.found_words[i])

        #  there are some duplicate words to delete so delete them from a set
        delete_set = set(words_to_delete)
        for word in delete_set:
            self.found_words.remove(word)

    def solve(self):
        """
        Will try to find every word in the word search
        """
        for word in self.words:
            self.find_word(word.upper())

    def show(self):
        """
        Will show the completed word search.
        """
        self.filter_found_words()
        plt.imshow(self.pixel_matrix, cmap=cm.Greys_r)
        for word in self.found_words:
            word.draw_line(self.letter_size)
        plt.show()

    def print(self):
        """
        Prints the numeric word search grid to the console
        """
        print(self.grid)
