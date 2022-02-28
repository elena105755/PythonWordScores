# !/usr/bin/env python
# -*- coding: utf8 -*-

# Python 3.10.2

__author__ = 'ameline'

import operator
from itertools import permutations


class HighScoringWords:
    MAX_LEADERBOARD_LENGTH = 100  # the maximum number of items that can appear in the leaderboard
    MIN_WORD_LENGTH = 3  # words must be at least this many characters long
    letter_values = {}
    valid_words = []

    def __init__(self, validwords='wordlist.txt', lettervalues='letterValues.txt'):
        """
        Initialise the class with complete set of valid words and letter values by parsing text files containing the data
        :param validwords: a text file containing the complete set of valid words, one word per line
        :param lettervalues: a text file containing the score for each letter in the format letter:score one per line
        :return:
        """
        self.top_word_list = []  # for building leaderboard from a list of words
        self.top_word_list_from_letters = []  # for building leaderboard from specified characters
        self.word_score_map = {}

        with open(validwords) as f:
            self.valid_words = f.read().splitlines()

        with open(lettervalues) as f:
            for line in f:
                (key, val) = line.split(':')
                self.letter_values[str(key).strip().lower()] = int(val)

    def build_leaderboard_for_word_list(self):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words from the complete set of valid words.
        :return: The list of top words.
        """
        list_discarded_words = []

        for word in self.valid_words:  # Create dictionary mapping of words and their respective scores.
            if len(word) >= self.MIN_WORD_LENGTH:
                self.word_score_map[word] = 0
                for letter in word:
                    self.word_score_map[word] += self.letter_values[letter]
            else:
                list_discarded_words.append(word)

        word_and_score = self._sort_word_scores(self.word_score_map, self.MAX_LEADERBOARD_LENGTH)
        self.top_word_list = [tpl[0] for tpl in word_and_score]

        return self.top_word_list

    def build_leaderboard_for_letters(self, starting_letters):
        """
        Build a leaderboard of the top scoring MAX_LEADERBOARD_LENGTH words that can be built using only the letters
        contained in the starting_letters String.

        The number of occurrences of a letter in the startingLetters String IS significant. If the starting letters are
        bulx, the word "bull" is NOT valid.

        There is only one l in the starting string but bull contains two l characters.

        Words are ordered in the leaderboard by their score (with the highest score first) and then alphabetically for
        words which have the same score.

        :param starting_letters: a random string of letters from which to build words that are valid against the
        contents of the wordlist.txt file
        :return: The list of top buildable words.
        """
        matched_words = []
        string = ""

        for word in self.valid_words:
            count = 0
            for x in starting_letters:
                if x in word:
                    count += 1
                if count == len(starting_letters):
                    matched_words.append(word)
                    break
        for matched_word in matched_words:
            if len(matched_word) > len(starting_letters) or len(matched_word) < self.MIN_WORD_LENGTH:
                continue
            string = matched_word
            break
        print(string)
        return string

        # for word in self.valid_words:
        #     if permutations(starting_letters) == word:
        #         matched_words.append(word)
        # return matched_words

    @staticmethod
    def _sort_word_scores(dictionary, limit):
        """
        Sorts the word:score dictionary mapping in reverse order of score.
        Words of equal scores are sorted alphabetically.
        :param dictionary: score dictionary
        """
        sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
        return sorted_dictionary[:limit]

    @staticmethod
    def permutation(input_string):
        if input_string == "":
            return [input_string]
        else:
            match = []
            for an in permutations(input_string[1:]):
                print(an)
                for pos in range(len(an) + 1):
                    match.append(an[:pos] + input_string[0] + an[pos:])
            return match


if __name__ == '__main__':
    hs_list = HighScoringWords(validwords='wordlist.txt', lettervalues='letterValues.txt')
    top_100 = hs_list.build_leaderboard_for_word_list()
    scrambled = hs_list.build_leaderboard_for_letters('deora')
