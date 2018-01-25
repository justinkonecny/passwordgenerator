#!/usr/bin/env python
# Author: Justin Konecny

import argparse
import random
import os
import sys


# reads and stores all words from the given .txt file
def read_lines(text_file):
    with open(text_file) as file_words:
        return file_words.readlines()


# returns the given list of words, with CAPS number of words capitalized
def capitalize_words(word_list, caps):
    # indices used to keep track of which words are capitalized
    options = list(range(0, len(word_list)))

    # lists to hold the randomly capitalized words
    words_cap = []

    # repeats capitalization process for CAPS words
    for w in range(0, caps):
        choice = random.choice(word_list)

        # ensure duplicate words are not selected
        while choice.capitalize() in words_cap:
            choice = random.choice(word_list)

        options.remove(word_list.index(choice))
        words_cap.append(choice.capitalize())

    for w in options:
        words_cap.append(word_list[w])

    return words_cap


# returns a single string randomly composed of the elements in the given list
def append_words_rand(lst):
    word_string = ""

    for _ in range(0, len(lst)):
        word = random.choice(lst)
        word_string += str(word)
        lst.remove(word)

    return word_string


# executes the program
def main():

    # creates the command line argument parser
    parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")

    # adds the [-w, --words] command to the command line
    parser.add_argument('-w', '--words', nargs='?', type=int, action='store', default=4,
                        help="include WORDS words in the password (default=4)")

    # adds the [-c, --caps] command to the command line
    parser.add_argument('-c', '--caps', nargs='?', type=int, action='store', default=0,
                        help="capitalize the first letter of CAPS random words (default=0)")

    # adds the [-n, --numbers] command to the command line
    parser.add_argument('-n', '--numbers', nargs='?', type=int, action='store', default=0,
                        help="insert NUMBERS random numbers in the password (default=0)")

    # adds the [-s, --symbols] command to the command line
    parser.add_argument('-s', '--symbols', nargs='?', type=int, action='store', default=0,
                        help="insert SYMBOLS random symbols in the password (default=0)")

    # reads and stores the command arguments
    args = parser.parse_args()

    # stores each argument value as a variable: number of words, capitalized words, numbers, and symbols
    words = args.words
    caps = args.caps
    numbers = args.numbers
    symbols = args.symbols

    # checks to ensure the entered value for "words" is greater than zero
    if words < 1:
        words = 1

    # checks to ensure the entered value for "caps" is greater than the number of words
    if caps > words:
        caps = words

    # reads all words stored in the specified .txt file
    dictionary = read_lines(os.path.dirname(os.path.realpath(sys.argv[0])) + '/lowercase.txt')

    # lists to hold the randomly selected words
    word_list = []

    for _ in range(0, words):
        # gets random integer from zero to the length of dictionary
        rand = random.randint(0, len(dictionary) - 1)

        # selects a random work and removes the newline char
        # word_list.append(dictionary[rand][:-1])
        word_list.append(random.choice(dictionary).rstrip())

    # checks if any words should be capitalized
    if caps > 0:
        word_list = capitalize_words(word_list, caps)

    # checks if any numbers should be added to the password
    if numbers > 0:
        for _ in range(0, numbers):
            word_list.append(random.randint(0, 9))

    # checks if any symbols should be added to the password
    if symbols > 0:
        list_symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '.', ':', ';']
        for _ in range(0, symbols):
            word_list.append(random.choice(list_symbols))

    print(append_words_rand(word_list))


# invokes main() if program is run from the command line
if __name__ == '__main__':
    main()
