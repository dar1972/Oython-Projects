"""
file: store_location.py
version: python3
author: Dhruv Rajpurohit
purpose: Implementation of the quick-sort algorithm to locate the least distance of the new store
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

def partition( pivot, L ):
    ( less, same, more ) = ( [], [], [] )
    for e in L:
        if e < pivot:
            less.append( e )
        elif e > pivot:
            more.append( e )
        else:
            same.append( e )
    return ( less, same, more )

def quick_sort( L ):
    """
    sorts the list using quick sort algorithm
    :param L: the list
    :return: the sorted list
    """
    if L == []:
        return []
    else:
        pivot = L[0]
        ( less, same, more ) = partition( pivot, L )
        return quick_sort( less ) + same + quick_sort( more )

def median(thelist):
    """
    calculates the median of the sorted list
    :param thelist: the unsorted list
    :return: the median
    """
    if len(thelist) % 2 == 1:
        med = (len(thelist)//2)
    else:
        med = ((thelist[len(thelist)//2-1]) + thelist[len(thelist)//2])/2
    return med

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
    the function ask for the list input
    then calculates the time quick sort takes to sort the list
    """
    filename = input("Enter data file: ")
    lst = list(filename)
    start = time.time()
    med = median((quick_sort(lst)))
    end = time.time()
    distance = distance_calc(lst, med)
    duration = end - start
    print("Optimum store location: ", med)
    print("Sum of distances to new store: ", distance)
    print()
    print("elapsed time: ", duration)

main()
