"""
File: hw08.py
Author: Dhruv Rajpurohit
Language: Python 3
Description: The code compares the time taken by insertion, merge and quick sort on a list of data
"""

import time
import random
import merge_sort
import insertion_sort
import quick_sort


def merge_quick_sort(lst):
    """
    this sort first split the list in to two and then quick is run through the two lists.
    the sorted list are then merged
    :param lst: the length of the list
    :return: the two split lists which have been sorted
    """
    (lst1)= merge_sort.split(lst)
    (lst2)= merge_sort.split(lst)
    (l1)= quick_sort.quick_sort(lst1)
    (l2)=quick_sort.quick_sort(lst2)
    return l1, l2

def get_list1(n):
    """
    :param n: the length of a list
    :return: a list with random elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.random()]
    return L

def get_list2(n):
    """
    :param n: the length of a list
    :return: a list with many repeated elements (favorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L+[random.randint(1,100)]
    return L


def get_list3(n):
    """
    Expected behavior of quick sort: poor
    :param n: the length of a list
    :return: a list of elements increasing overall
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.random()*i]
    return L

def get_list4(n):
    """
    :param n: the length of a list
    :return: a list with many zeros but neither increasing nor decreasing
    (unfavorable to quick sort)
    """
    L = []
    for i in range(n):
        L = L + [random.randint(-8, 8)*i]
    return L

def test_compare(n):
    """
    The function test the time taken by different sorts to sort the given list
    :param n: the length of the list.
    """
    print("Time comparison test begins.")
    print("All lists used in this test are of length", n, ".")
    print("")

    print("Testing with list 1 - random elements")
    lst = get_list1(n)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("insertion_sort elapsed time:", end-start, "seconds")
    lst = get_list1(n)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("merge_sort elapsed time:", end-start, "seconds")
    lst = get_list1(n)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("merge_quick_sort elapsed time:", end-start, "seconds")
    lst = get_list1(n)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("quick_sort elapsed time:", end-start, "seconds")

    print("")
    print("Testing with list 2 - repeated elements")
    lst = get_list2(n)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("insertion_sort elapsed time:", end-start, "seconds")
    lst = get_list2(n)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("merge_sort elapsed time:", end-start, "seconds")
    lst = get_list2(n)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("merge_quick_sort elapsed time:", end-start, "seconds")
    lst = get_list2(n)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("quick_sort elapsed time:", end-start, "seconds")

    print("")
    print("Testing with list 3 - overall increasing elements, not favorable to quick sort")
    lst = get_list3(n)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("insertion_sort elapsed time:", end-start, "seconds")
    lst = get_list3(n)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("merge_sort elapsed time:", end-start, "seconds")
    lst = get_list3(n)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("merge_quick_sort elapsed time:", end-start, "seconds")
    lst = get_list3(n)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("quick_sort elapsed time:", end-start, "seconds")

    print("")
    print("Testing with list 4 - not favorable to quick sort")
    lst = get_list4(n)
    start = time.time()
    sorted_list = insertion_sort.insertion_sort(lst)
    end = time.time()
    print("insertion_sort elapsed time:", end-start, "seconds")
    lst = get_list4(n)
    start = time.time()
    sorted_list = merge_sort.merge_sort(lst)
    end = time.time()
    print("merge_sort elapsed time:", end-start, "seconds")
    lst = get_list4(n)
    start = time.time()
    sorted_list = merge_quick_sort(lst)
    end = time.time()
    print("merge_quick_sort elapsed time:", end-start, "seconds")
    lst = get_list4(n)
    start = time.time()
    sorted_list = quick_sort.quick_sort(lst)
    end = time.time()
    print("quick_sort elapsed time:", end-start, "seconds")

    print("")
    print("Time comparison test ends.")

def test_merge_quick_sort():
    """
    the function test whether the merge quick sort work efficiently or not.
    :return: the sorted list
    """
    print("Testing the correctness of merge_quick_sort:")
    print("Before sorted:")
    print("[4, 8, 6, 15, 17, 5, 2, 13, 1, 19, 16, 3, 11, 7, 9, 18, 0, 10, 14, 12]")
    merge_quick_sort( [4, 8, 6, 15, 17, 5, 2, 13, 1, 19, 16, 3, 11, 7, 9, 18, 0, 10, 14, 12] )
    print("After sorted:")
    print(merge_sort.merge([0, 1, 2, 4, 6, 9, 11, 14, 16, 17], [3, 5, 7, 8, 10, 12, 13, 15, 18, 19]))
    print("")

test_merge_quick_sort()
n = 10000
test_compare(n)

