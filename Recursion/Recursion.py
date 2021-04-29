"""
file: double_add_5.py
language: python3
author: Dhruv Rajpurohit (dar1972@rit.edu)
description: cs1 Integer Sequences
"""

import math

"""
The function will generate and print the count steps recursively by taking the start value. 
The actual output will be always Count + 1 because it is printing the start.
The start value and count value are local variables
"""
def print_sequence_rec(start,count):
    if count<=0:
        print(start)
    else:
        print(start)
        return(print_sequence_rec(start*2+5,count-1))

"""
The function will generate and print the count steps by doubling and then adding 5 to the start value
iteratively. 
The actual output will be always Count + 1 because it is printing the start.
The start value and count value are local variables
"""
def print_sequence_iter(start,count):
    while count>=0:
        print(start)
        start=start*2+5
        count=count-1

"""
The function will recursively find and return the final value of the sequence.
"""
def find_end_rec(start, count):
    if count==0:
        return(start)
    else:
        return(find_end_rec(start*2+5,count-1))

"""
The function will iteratively find and return the final value of the sequence.
"""
def find_end_iter(start,count):
    while count!=0:
        start=start*2+5
        count=count-1
    if(count==0):
        return(start)


"""
the function will recursively search the forward value from an initial value 0, 
then return the smallest integer value that should reache or exceed the goal.
pre-conditions: goal >= 0 and count > 0.  
"""
def find_start_iter(goal,count):
    n=0
    while find_end_iter(n,count)<goal:
        n=n+1
    print(n)
"""
the function will iteratively search the forward value from an initial value 0, 
then return the smallest integer value that should reache or exceed the goal.
pre-conditions: goal >= 0 and count > 0.  
"""
def find_start(goal,count,n):
    if(find_end_rec(n,count)>=goal):
        return n
    else:
        return find_start(goal,count,n+1)

def find_start_rec(goal, count):
    print(find_start(goal,count,0))



print_sequence_rec(0,-1)
print_sequence_rec(0,0)
print_sequence_rec(1,2)
print_sequence_iter(2,5)
print_sequence_rec(1,0)
print_sequence_iter(1,1)
print_sequence_iter(3,19)
find_end_rec(100,3)
find_end_iter(100,3)
find_end_iter(1,10)
find_end_rec(2,40)
find_end_rec(1,1001)
find_end_iter(1,1001)
find_start_rec(7,3)
find_start_iter(8,3)
find_start_rec(9,2)
find_start_iter(100,1)
find_start_rec(100,3)
