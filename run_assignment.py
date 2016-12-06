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

#number of letters allowed to be wrong in a found word (in case a letter is classified wrong)
error_tolerance = 1

def get_word_search_letters(matrix, letter_size):
    """
    Takes a matrix representing a word search. Letters must be equally spaced in a grid
    and each letter must be contained within the grid boundaries (letter_size x letter_size)

    :param matrix: matrix representing a word search grid
    :param letter_size: the number of pixels that is the length of one side of the squares that contain each letter.
    :return: a list of all of the pixels for each character in the grid.
    """

    letters = []

    for letter_row in range(0, len(matrix), letter_size):
        for letter_col in range(0, len(matrix[0]), letter_size):
            letter = []
            for pixel_row in range(letter_row, letter_row + 30):
                for pixel_col in range(letter_col, letter_col + 30):
                    letter.append(matrix[pixel_col][pixel_row])
            letters.append(letter)

    return np.array(letters)


# converts a character to an integer value (A = 1; B = 2; ect.)
def letter_to_int(letter):
    return ord(letter) - 64


# converts an integer into a character (1 = A; 2 = B; ect.)
def int_to_letter(i):
    return chr(i + 64)


def look_horizontal(word_search, word, x, y, direction):
    """
    Will perform a search for a given word horizontally along a given direction from a starting point.
    If the word is found it will return true, otherwise it will return false

    :param word_search: The word search grid
    :param word: The word that is being search for in the grid
    :param x: The starting x position in the grid
    :param y: The starting y position in the grid
    :param direction: The direction to search in (1 = Search Right; -1 = Search Left)
    :return: True if the word is found and false if the word is not found
    """

    wrong_count = 0
    found = True

    for i in range(1, len(word)):
        if x + (i * direction) >= len(word_search[0]) or x + (i * direction) < 0:
            #off the grid
            found = False
            break
        if word_search[y][x + (i * direction)] != (letter_to_int(word[i])): # if the next letter in the grid is not the next letter of the word
            wrong_count += 1
            if wrong_count > error_tolerance:
                found = False
                break

    return found


def look_vertical(word_search, word, x, y, direction):
    """
    Will perform a search for a given word vertically along a given direction from a starting point.
    If the word is found it will return true, otherwise it will return false

    :param word_search: The word search grid
    :param word: The word that is being search for in the grid
    :param x: The starting x position in the grid
    :param y: The starting y position in the grid
    :param direction: The direction to search in (1 = Search Down; -1 = Search Up)
    :return: True if the word is found and false if the word is not found
    """

    wrong_count = 0
    found = True

    for i in range(1, len(word)):
        if y + (i * direction) >= len(word_search) or y + (i * direction) < 0:
            #off the grid
            found = False
            break
        if word_search[y + (i * direction)][x] != (letter_to_int(word[i])):  # if the next letter in the grid is not the next letter of the word
            wrong_count += 1
            if wrong_count > error_tolerance:
                found = False
                break

    return found

def look_diagonal(word_search, word, x, y, x_direction, y_direction):
    """
    Will perform a search for a given word vertically along a given direction from a starting point.
    If the word is found it will return true, otherwise it will return false

    :param word_search: The word search grid
    :param word: The word that is being search for in the grid
    :param x: The starting x position in the grid
    :param y: The starting y position in the grid
    :param x_direction: The horizontal direction to search in (1 = Search Right; -1 = Search Left)
    :param y_direction: The vertical direction to search in (1 = Search Down; -1 = Search Up)
    :return: True if the word is found and false if the word is not found
    """

    wrong_count = 0
    found = True

    for i in range(1, len(word)):
        if y + (i * y_direction) >= len(word_search) or y + (i * y_direction) < 0:
            #off the grid
            found = False
            break
        if x + (i * x_direction) >= len(word_search[0]) or x + (i * x_direction) < 0:
            #off the grid
            found = False
            break
        if word_search[y + (i * y_direction)][x + (i * x_direction)] != (letter_to_int(word[i])):  # if the next letter in the grid is not the next letter of the word
            wrong_count += 1
            if wrong_count > error_tolerance:
                found = False
                break

    return found


def check_letter_is_word(word_search, word, x, y):
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

    for direction in range(1, -2, -2): # for loop that gives 1 and -1 before terminating
        if (look_horizontal(word_search, word, x, y, direction) or
                look_vertical(word_search, word, x, y, direction)):
            letter_is_word = True
        else:
            for direction2 in range(1, -2, -2):
                if look_diagonal(word_search, word, x, y, direction, direction2):
                    letter_is_word = True
                    break

        if letter_is_word:
            break

    return letter_is_word


def find_word(word_search, word):
    """
    Searches an entire word search grid for a word
    :param word_search: The word seach grid
    :param word: The word to be searched for
    """
    found = False

    for x in range(0, len(word_search[0])):
        for y in range(0, len(word_search)):
            if word_search[x][y] == word[0]:
                if check_letter_is_word(word_search, word, x, y):
                    found = True
                    break
        if found:
            break


letters = get_word_search_letters(test1, 30)
word_search = (np.reshape(given_methods.classify(train_data, train_labels, letters), (15, 15), order='F'))

print(words)
print(look_horizontal(word_search, "LANGLEY", 8, 0, -1))
print(look_vertical(word_search, "CANE", 0, 2, 1))
print(look_diagonal(word_search, "NNN", 2, 2, -1, -1))
print(look_diagonal(word_search, "YNC", 2, 0, -1, 1))
print(word_search)

check_letter_is_word(word_search, "BANTER", 0, 0)






















