"""
file: select_median.py
version: python3
author: Dhruv Rajpurohit
purpose: Implementation of the quick-select algorithm to locate the least distance of the new store
"""

import time
import math



def list(file):
    """
    the function opens a file and the adds the numeric values to the list
    :param file: the file from which numeric values are added from
    :return: the numeric values which have been added to the list
    """
    lst =[]
    text = open(file)
    for line in text:
        for charecters in line.split():
            if charecters.isdigit():
                lst.append(int(charecters))
    return lst

def quick_select(alist, k):
    """
    the function selects the smallest element in an unordered list
    :param alist: the list which contains the numeric values
    :param k: the smallest number
    :return: the numeric values in the ascending order
    """
    smallerList = []
    largerList = []
    sameList = []
    if alist == []:
        return []
    else:
        pivot = alist[len(alist)//2]
        for c in alist:
            if c < pivot:
                smallerList.append(c)
            elif c > pivot:
                largerList.append(c)
            else:
                sameList.append(c)
        m = len(smallerList)
        count = len(sameList)
        if k >= m and k < m + count:
            return pivot
        elif m > k:
            return quick_select(smallerList, k)
        else:
            return quick_select(largerList, k - m - count)


def distance_calc(L, med):
    """
    calculates the sum of distance to the store
    :param L: the list values
    :param med: median of the list
    :return: the distance calculated
    """
    dist = 0
    for c in L:
        dist += abs(med - int(c))
    return dist

def main():
    """
    the function ask for the input and then quick selects the file.
    calculates the time taken by selection sort.
    """
    filename = input("Enter data file: ")
    lst = list(filename)
    if len(lst)%2 == 1:
        start = time.time()
        med = quick_select(lst, len(lst)//2)
        end = time.time()
    else:
        start = time.time()
        med = (quick_select(lst, (len(lst))//2) + quick_select(lst, (len(lst))//2-1))/2
        end = time.time()
    distance = distance_calc(lst, med)
    duration = end - start
    print("Optimum store location: ", med)
    print("Sum of distances to new store: ", distance)
    print()
    print("elapsed time: ", duration)

main()
