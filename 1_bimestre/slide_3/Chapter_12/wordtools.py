import sys
import string

def test(did_pass):

    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def cleanword(str):
    new_str = ''
    for letter in str:
        if letter not in string.punctuation:
            new_str += letter
    return new_str


def has_dashdash(str):
    return "--" in str


def extract_words(str):
    return cleanword(str.replace('--', ' ')).lower().split()


def wordcount(word, list):
    result = 0
    for element in list:
        if element == word:
            result += 1
    return result


def wordset(list):
    new_list = []
    for element in list:
        if element not in new_list:
            new_list.append(element)

    return sorted(new_list)


def longestword(list):
    max_number = 0
    for word in list:
        if len(word) > max_number:
            max_number = len(word)
    return max_number
