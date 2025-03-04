import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from DataStructures.List import single_linked_list as sl

class EmptyStructureError(Exception):
    pass

def new_stack():
    return sl.new_list()

def push(my_stack, element):
    sl.add_last(my_stack, element)
    return my_stack

def pop(my_stack):
    if sl.is_empty(my_stack):
        raise EmptyStructureError("stack is empty")
    return sl.remove_last(my_stack)

def is_empty(my_stack):
    return sl.is_empty(my_stack)

def top(my_stack):
    if sl.is_empty(my_stack):
        raise EmptyStructureError("stack is empty")
    return sl.first_element(my_stack)

def size(my_stack):
    return sl.size(my_stack)
