import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from DataStructures.List import array_list as al



"""Nueva pila"""
def new_stacka() -> dict:
    nueva_pila = al.new_list()
    return nueva_pila



"""Agrega al tope de la pila"""
def pusha(my_stack:dict, element) -> dict:
    al.add_last(my_stack, element)
    return my_stack



"""Elimina y retorna el elemento en el tope"""
def popa(my_stack:dict):
    elemento = al.last_element(my_stack)
    al.remove_last(my_stack)
    return elemento



"""¿Está vacia?"""
def is_emptya(my_stack:dict) -> bool:
    vacia = al.is_empty(my_stack)
    return vacia



"""Retorna el primero"""
def topa(my_stack:dict):
    elemento = al.last_element(my_stack)
    return elemento



"""Tamaño"""
def sizea(my_stack:dict) -> int:
    tamano = al.size(my_stack)
    return tamano