"""
Filename: ball_puzzle.py
Language: Python3
Author: Dhruv Rajpurohit
Description: The function solves the ball puzzle
"""
from ball_puzzle_animate import *


def make_stack(can):
    """
    The function makes the stack
    :param can: the string
    :return: the stack
    """
    st = make_empty_stack()
    for balls in can:
        push(st, balls)
    return st


def solve(rc, bc, gc):
    """
    Thr function solves the puzzle and also keeps the count of the moves
    :param rc: red can
    :param bc: blue can
    :param gc: green can
    :return: count of the moves
    """
    c = 0
    cans = [rc, gc, bc]
    while is_empty(rc) is not True:
        if rc.top.value == "G":
            push(gc, pop(rc))
            animate_move(cans, 0, 1)
            c += 1
        else:
            push(bc, pop(rc))
            animate_move(cans, 0, 2)
            c += 1
    while is_empty(bc) is not True:
        if bc.top.value == "B":
            push(gc, pop(bc))
            animate_move(cans, 2, 1)
            c += 1
        else:
            push(rc, pop(bc))
            animate_move(cans, 2, 0)
            c += 1
    while is_empty(gc) is not True:
        if gc.top.value == "B":
            push(bc, pop(gc))
            animate_move(cans, 1, 2)
            c += 1
        else:
            break
    return c


def main():
    """
    The function calls all the other function
    """
    x = input("Enter the sequence of balls: ")
    animate_init(x)
    rc = make_stack(x)
    gc = make_empty_stack()
    bc = make_empty_stack()
    count = solve(rc, gc, bc)
    print("The puzzle was solved in", count, "moves")
    print("To quit the animation close the window")
    animate_finish()


main()

