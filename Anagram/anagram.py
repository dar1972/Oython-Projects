"""
File name: anagram.py
Language: Python 3
Author: Dhruv Rajpurohit
Description: The program performs various task which includes
            to identify anagrams in sorted order of the inputted word.
            to identify the maximum number of anagrams for a certain word length
            to identify maximum number of good jumble words which has no anagram available for the certain word length
"""

def dictionary(path):
    """
    The function adds words from the file to a list.
    The function also sorts the words in alphabetical order same as a dictionary.
    :param path: the file to be opened
    :return: the sorted key
    """
    letter = {}
    file = open(path, "r", encoding="utf-8")
    for line in file.readlines():
        line = line.strip()
        key = sorted_line(line)

        # Add each line to a dictionary based on its sorted key.
        if key in letter:
            v = letter.get(key) + "," + line
            letter[key] = v
        else:
            letter[key] = line
    return letter

def sorted_line(line):
    """
    The function sorts the line in the Chars
    :param line: a specific line in the list
    :return: a string
    """
    chars = [c for c in line]
    chars.sort()
    return "".join(chars)

def task_1(letter, line):
    """
    The function performs the analysis of the anagrams from the list sorts the output
    :param letter: each letter from the word asked to be anagramed
    :param line: line from the list
    :return: list of anagrams from the dictionary.
    """
    key = sorted_line(line)
    values = letter.get(key)
    return values.split(",")

def task_3(size):
    """
    The function identifies the maximum size list of the word which are anagrams of each other.
    :param size: the size of the word length of a words to be identified
    :return: the list of anagrams
    """
    lst = []
    word = dictionary("american-english.txt")
    max_length = 0
    for key in word:
        if len(key)== size:
            if max_length < len(word[key]):
                max_length = len(word[key])
                lst[:] = []
                lst = (word[key].split(","))
    print("Max numbers of words for length", size,":", len(lst))
    print("Anagram list:" ,lst)



def task_4(size):
    """
    Identifies words which are good jumble words and have no anagrams by asking for the word length.
    :param size: word length
    :return: the number of words which do not have any anagrams.
    """
    count = 0
    word = dictionary("american-english.txt")
    for key in word:
        if len(key) == size:
            if len(word[key].split(",")) == 1:
                count = count + 1
    print("Number of jumble usable words of length 5 : ", count)




def main():
    """
    performs all the task in the loop until the user does not quit.
    """
    while True:
        word = dictionary("american-english.txt")
        text = input("Enter input string (hit enter key to go to task 3): ")
        if text == "":
            print("")
            while True:
                text = input("Enter word length (hit enter key to go to task 4): ")
                if text == "":
                    print("")
                    while True:
                        text = input("Enter word length (hit enter key to quit): ")
                        if text == "":
                            break
                        else:
                            text = int(text)
                            task_4(text)
                    break
                else:
                    text = int(text)
                    task_3(text)
            break
        if sorted_line(text) in word:
            results = task_1(word, text)
            print("Corresponding words: ", results)
        else:
            print("No corresponding words found for: ", text)
main()




