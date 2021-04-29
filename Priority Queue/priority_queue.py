"""
Filename: task.py
Language: Python 3
Author: Dhruv Rajpurohit
Description: The code calls different function which is used to performed tasks in task.py
"""

from dataclasses import dataclass
from typing import Union
from node import Node


@dataclass
class PriorityQueue:
    size: int
    front: Union[None, Node]
    back: Union[None, Node]


def make_priority_queue():
    return PriorityQueue(0, None, None)


def enqueue(queue, element):
    """
    Insert an element into the queue.
    :param queue: the queue in which element is inserted
    :param element: the element to be inserted
    :return: the new list
    """
    newnode = Node(element, None)
    if is_empty(queue):
        queue.front = newnode
    else:
        queue.back.rest = newnode
    queue.back = newnode
    queue.size = queue.size + 1

def dequeue(queue):
    """
    Remove the front element from the queue.
    precondition: queue is not empty.
    :param queue: the queue from which element is removed
    :return: the removed element
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue")
    removed = queue.front.value
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed

def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    :param queue: the queue
    :return: the first element of the queue
    """
    if is_empty(queue):
        raise IndexError("front on empty queue")
    return queue.front.value

def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    :param queue: a queue
    :return: the last element of the queue
    """
    if is_empty(queue):
        raise IndexError("back on empty queue")
    return queue.back.value

def is_empty(queue):
    """
    to check if the queue is empty or not
    :param queue: the queue to be checked
    :return: the answer
    """
    return queue.front == None


def sorting(queue):
    """
    The code is used to sort the queue by making a new queue
    :param queue: the queue to be sorted
    :return: the sorted queue
    """
    q = make_priority_queue()
    while True:
        if queue.size != 1:
            first = dequeue(queue)
            queue_size = queue.size
            for count in range(queue_size):
                if first.priority >= front(queue).priority:
                    rem = dequeue(queue)
                    enqueue(queue, rem)
                else:
                    rem = dequeue(queue)
                    enqueue(queue, first)
                    first = rem
            enqueue(q, first)
        else:
            break
        v = front(queue)
        enqueue(q, v)
    return q




