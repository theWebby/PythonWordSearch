import pickle
import given_methods
import found_word
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from word_search import WordSearch

# extracting the data from the pickle file
data = pickle.load(open("data/assignment2.pkl", "rb"))
train_data = data['train_data']
train_labels = data['train_labels']
test1 = data['test1']
test2 = data['test2']
words = data['words']







##
word_search = WordSearch(test1, 30, words, train_data, train_labels)
#word_search.solve()
#word_search.find_word_at_point("LANGLEY", 8, 0)
word_search.find_word("PETO")
word_search.show()
##






#
# letters = get_word_search_letters(test1, 30)
# #word_search = (np.reshape(given_methods.classify(train_data, train_labels, letters), (15, 15), order='F'))
#
# print(words)
#
# print(word_search)
#
# find_words(word_search, words)
# #find_word(word_search, "NEEJ")
# #find_word(word_search, "JEEN")
#
# letter_image = np.reshape(letters, (450, 450), order='F')
# plt.imshow(test1, cmap=cm.Greys_r)
# #foundWord = FoundWord.FoundWord(0, 0, 450, 450)
# #foundWord.draw_line()
#
# for word in foundWords:
#     word.draw_line()
#
# plt.show()
#



















