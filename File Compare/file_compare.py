"""
file name: file_compare.py
author: Dhruv Rajpurohit
language: python 3
description: compares 2 text files for the differences.
"""


def char_by_char(file1,file2):
    """
    This function will open 2 text files and will compare each line of the two files.
    The function will output the difference point where there is difference and the number of charecters in each.
    """
    file1 = open('t1.txt')
    file2 = open('t2.txt')
    line1 = " "
    line2 = " "
    line_num = 1
    total_char1 = 0
    total_char2 = 0
    total_char_diff = 0
    total_line_diff = 0
    print("Unmatched character:", sep = "", end = "")
    while line1 != "" or line2 != "":
        line1 = file1.readline().strip()
        line2 = file2.readline().strip()
        if len(line1) != len(line2):
            print(str(line_num) + ", ", sep = "", end = "")
            total_char1 += len(line1)
            total_char2 += len(line2)
            total_line_diff += 1
        elif len(line1) == len(line2):
            index = 0
            while index < len(line1):
                if line1[index] != line2[index]:
                    print(line_num, ":", index + 1, " , ", sep = "", end = "")
                    total_char_diff += 1
                index = index + 1
            total_char1 += len(line1)
            total_char2 += len(line2)
        line_num += 1
    print("There are", total_char1, "characters in the first file")
    print("There are", total_char2, "characters in the first file")
    print("There were", total_char_diff, "unmatched characters")
    print("There were", total_line_diff, "lines of different length")

def main():
    """
    this will ask for the input and will run char_by_char()
    """
    print("Character by character:")
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")
    char_by_char(file1, file2)

main()
