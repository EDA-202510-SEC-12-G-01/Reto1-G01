import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from DataStructures.List import single_linked_list as sl



"""Nueva cola"""
def new_queues() -> dict:
    nueva_queue = sl.new_list()
    return nueva_queue



"""Agrega elemento al final"""
def enqueues(my_queue:dict, element) -> dict:
    sl.add_last(my_queue, element)
    return my_queue



"""Elimina y retorna el primer elemento"""
def dequeues(my_queue:dict):
    elemento = sl.first_element(my_queue)
    sl.remove_first(my_queue)
    return elemento



"""Primer elemento"""
def peeks(my_queue:dict):
    elemento = sl.first_element(my_queue)
    return elemento



"""¿Está vacia?"""
def is_emptys(my_queue:dict) -> bool:
    vacia = sl.is_empty(my_queue)
    return vacia



"""Tamaño"""
def sizes(my_queue: dict) -> int:
    tamano = sl.size(my_queue)
    return tamano