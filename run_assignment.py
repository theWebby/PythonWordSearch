import pickle
import given_methods
import numpy as np

# extracting the data from the pickle file
data = pickle.load(open("data/assignment2.pkl", "rb"))
train_data = data['train_data']
train_labels = data['train_labels']
test1 = data['test1']
test2 = data['test2']
words = data['words']


def get_word_search_letters(matrix, letter_size):
    """
    Takes a matrix representing a word search. Letters must be equally spaced in a grid
    and each letter must be contained within the grid boundaries (letter_size x letter_size)

    :param matrix: matrix representing a word search grid
    :param letter_size: the number of pixels that is the length of one side of the squares that contain each letter.
    :return: a list of all of the pixels for each character in the grid.
    """

    letters = []

    for letter_col in range(0, len(matrix[0]), letter_size):
        for letter_row in range(0, len(matrix), letter_size):
            letter = []
            for pixel_col in range(letter_col, letter_col + 30):
                for pixel_row in range(letter_row, letter_row + 30):
                    letter.append(matrix[pixel_col, pixel_row])
            letters.append(letter)

    return letters

word_search_letters = get_word_search_letters(test1, 30)
print(len(word_search_letters[0]))








