from found_word import FoundWord


class Search:

    error_tolerance = 3

    @classmethod
    def look_horizontal(cls, word_search, word, x, y):
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
        found_direction = 0

        # looking both directions
        for direction in range(1, -2, -2):
            found = True
            wrong_count = 0
            found_direction = direction
            for i in range(1, len(word)):  # for each letter in the word
                if x + (i * direction) >= len(word_search[0]) or x + (i * direction) < 0:
                    # off the grid
                    found = False
                    break
                # if the next letter in the grid is not the next letter of the word
                if word_search[y][x + (i * direction)] != (FoundWord.letter_to_int(word[i])):
                    wrong_count += 1
                    if wrong_count > cls.error_tolerance:
                        found = False
                        break
            if found:
                break

        if found:
            last_x = x + ((len(word) - 1) * found_direction)
            return FoundWord(x, y, last_x, y, word, wrong_count)  # horizontal word therefore y stays the same
        else:
            return None

    @classmethod
    def look_vertical(cls, word_search, word, x, y):
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
        found_direction = 0

        for direction in range(1, -2, -2):
            found = True
            wrong_count = 0
            found_direction = direction
            for i in range(1, len(word)):
                if y + (i * direction) >= len(word_search) or y + (i * direction) < 0:
                    # off the grid
                    found = False
                    break
                # if the next letter in the grid is not the next letter of the word
                if word_search[y + (i * direction)][x] != (FoundWord.letter_to_int(word[i])):
                    wrong_count += 1
                    if wrong_count > cls.error_tolerance:
                        found = False
                        break
            if found:
                break

        if found:
            last_y = y + ((len(word) - 1) * found_direction)
            return FoundWord(x, y, x, last_y, word, wrong_count)  # vertical word therefore x stays the same
        else:
            return None

    @classmethod
    def look_diagonal(cls, word_search, word, x, y):
        """
        Will perform a search for a given word vertically along a given direction from a starting point.
        If the word is found it will return true, otherwise it will return false

        :param word_search: The word search grid
        :param word: The word that is being search for in the grid
        :param x: The starting x position in the grid
        :param y: The starting y position in the grid
        :param direction_x: The horizontal direction to search in (1 = Search Right; -1 = Search Left)
        :param direction_y: The vertical direction to search in (1 = Search Down; -1 = Search Up)
        :return: True if the word is found and false if the word is not found
        """

        wrong_count = 0
        found = True
        found_direction_x = 0
        found_direction_y = 0

        for direction_y in range(1, -2, -2):
            found_direction_y = direction_y
            for direction_x in range(1, -2, -2):
                found = True
                wrong_count = 0
                found_direction_x = direction_x
                for i in range(1, len(word)):
                    if y + (i * direction_y) >= len(word_search) or y + (i * direction_y) < 0:
                        # off the grid
                        found = False
                        break
                    if x + (i * direction_x) >= len(word_search[0]) or x + (i * direction_x) < 0:
                        # off the grid
                        found = False
                        break
                    # if the next letter in the grid is not the next letter of the word
                    if word_search[y + (i * direction_y)][x + (i * direction_x)] != (FoundWord.letter_to_int(word[i])):
                        wrong_count += 1
                        if wrong_count > cls.error_tolerance:
                            found = False
                            break
                if found:
                    break
            if found:
                break

        if found:
            last_x = x + ((len(word) - 1) * found_direction_x)
            last_y = y + ((len(word) - 1) * found_direction_y)
            return FoundWord(x, y, last_x, last_y, word, wrong_count)  # diagonal word therefore x and y change
        else:
            return None


