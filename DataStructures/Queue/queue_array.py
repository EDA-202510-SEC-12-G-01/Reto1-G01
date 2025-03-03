import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from DataStructures.List import array_list as al



"""Nueva cola"""
def new_queuea() -> dict:
    nueva_queue = al.new_list()
    return nueva_queue



"""Agrega elemento al final"""
def enqueuea(my_queue:dict, element) -> dict:
    al.add_last(my_queue, element)
    return my_queue



"""Elimina y retorna el primer elemento"""
def dequeuea(my_queue:dict):
    elemento = al.first_element(my_queue)
    al.remove_first(my_queue)
    return elemento



"""Primer elemento"""
def peeka(my_queue:dict):
    elemento = al.first_element(my_queue)
    return elemento



"""¿Está vacia?"""
def is_emptya(my_queue:dict) -> bool:
    vacia = al.is_empty(my_queue)
    return vacia



"""Tamaño"""
def sizea(my_queue: dict) -> int:
    tamano = al.size(my_queue)
    return tamano