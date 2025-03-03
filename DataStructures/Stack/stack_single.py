import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from DataStructures.List import single_linked_list as sl



"""Nueva pila"""
def new_stacks() -> dict:
    nueva_pila = sl.new_list()
    return nueva_pila



"""Agrega al tope de la pila"""
def pushs(my_stack:dict, element) -> dict:
    sl.add_last(my_stack, element)
    return my_stack



"""Elimina y retorna el elemento en el tope"""
def pops(my_stack:dict):
    elemento = sl.last_element(my_stack)
    sl.remove_last(my_stack)
    return elemento



"""¿Está vacia?"""
def is_emptys(my_stack:dict) -> bool:
    vacia = sl.is_empty(my_stack)
    return vacia



"""Retorna el primero"""
def tops(my_stack:dict):
    elemento = sl.last_element(my_stack)
    return elemento



"""Tamaño"""
def sizes(my_stack:dict) -> int:
    tamano = sl.size(my_stack)
    return tamano