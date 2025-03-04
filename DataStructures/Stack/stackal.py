import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from DataStructures.List import array_list as al

class EmptyStructureError(Exception):
    pass

def new_stack():
    return al.new_list()

def push(my_stack, element):
    al.add_last(my_stack, element)
    return my_stack

def pop(my_stack):
    if al.is_empty(my_stack):
        raise EmptyStructureError("stack is empty")
    return al.remove_last(my_stack)

def is_empty(my_stack):
    return al.is_empty(my_stack)

def top(my_stack):
    if al.is_empty(my_stack):
        raise EmptyStructureError("stack is empty")
    return al.first_element(my_stack)

def size(my_stack):
    return al.size(my_stack)

