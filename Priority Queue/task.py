"""
Filename: task.py
Language: Python 3
Author: Dhruv Rajpurohit
Description: the code performs different task by calling functions from priority_queue.py
"""

from priority_queue import *
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int


def make_task(task_name, priority):
    """
    the function calls the class to create a task
    :param task_name: the name of the task
    :param priority: the priority of the task
    :return: the created task
    """
    return Task(task_name, priority)


def main():
    """
    The function performs tasks to check if priority_queue.py works.
    In the function various functions are called from priority_queue.py
    The first and last element of the queue is printed.
    """
    q = make_priority_queue()
    enqueue(q, Task("Task1", 1))
    enqueue(q, Task("Task2", 5))
    enqueue(q, Task("Task3", 7))
    enqueue(q, Task("Task4", 8))
    m = sorting(q)
    t = front(m)
    print("Highest priority task is", t.name, "with priority", t.priority)
    t = back(m)
    print("Lowest priority task is", t.name, "with priority", t.priority)

main()
