import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from DataStructures.List import single_linked_list as sl

class EmptyStructureError(Exception):
    pass

def new_queue():
    return sl.new_list()

def enqueue(my_queue, element):
    return sl.add_last(my_queue, element)

def dequeue(my_queue):
    if is_empty(my_queue):
        raise EmptyStructureError("queue is empty")
    return sl.remove_first(my_queue)

def peek(my_queue):
    if is_empty(my_queue):
        raise EmptyStructureError("queue is empty")
    return sl.first_element(my_queue)

def is_empty(my_queue):
    return sl.is_empty(my_queue)

def size(my_queue):
    return sl.size(my_queue)