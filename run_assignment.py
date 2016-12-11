import pickle
from word_search import WordSearch

# extracting the data from the pickle file
data = pickle.load(open("data/assignment2.pkl", "rb"))
train_data = data['train_data']
train_labels = data['train_labels']
test1 = data['test1']
test2 = data['test2']
words = data['words']
letter_size = 30


def wordsearch(matrix, words, train_data, train_labels):
    """
    This is the function that we have been asked to write for the assignment. This function takes a word search image
    (as pixels), a list of words and some training data and labels and will output the solved word search.
    :param matrix: A matrix representing an image of the word search grid to be processed.
    :param words: A list of words to be found in the word search.
    :param train_data: Training data to classify letters in the word search.
    :param train_labels: Training labels for the training data.
    :return:
    """
    word_search = WordSearch(matrix, letter_size, words, train_data, train_labels)
    word_search.solve()
    #word_search.find_word("EE")
    word_search.print()
    word_search.show()


wordsearch(test1, words, train_data, train_labels)


















