from DataStructures.List import nodos as no
from DataStructures.List import array_list as al



"""Nueva lista"""
def new_list() -> dict:
    nueva_lista = {"first": None, "last": None, "size": 0 }
    return nueva_lista



"""¿Está vacia?"""
def is_empty(my_list:dict) -> bool:
    vacia = False
    if my_list["size"] == 0:
        vacia = True
    return vacia



"""Tamaño"""
def size(my_list:dict) -> int:
    tamaño = my_list["size"]
    return tamaño



"""Agregar al inicio"""
def add_first(my_list:dict, element) -> dict:
    nodo = no.new_single_node(element)
    if is_empty(my_list) == True:
        my_list["last"] = nodo
        my_list["first"] = nodo
    else:
        nodo["next"] = my_list["first"]
        my_list["first"] = nodo
    my_list["size"] +=1
    return my_list



"""Agregar al final"""
def add_last(my_list:dict, element) -> dict:
    nodo = no.new_single_node(element)
    if is_empty(my_list):
        my_list["first"] = my_list["last"] = nodo
    else:
        my_list["last"]["next"] = nodo
        my_list["last"] = nodo
    my_list["size"] += 1
    return my_list



"""Primer elemento"""
def first_element(my_list:dict):
    error_vacia(my_list)
    elemento = no.get_element(my_list["first"])
    return elemento



"""Último elemento"""
def last_element(my_list:dict):
    error_vacia(my_list)
    elemento = no.get_element(my_list["last"])
    return elemento



"""Elemento dado index"""
def get_element(my_list:dict, pos:int):
    error_index(my_list, pos)
    nodo = avanzar(my_list, pos)
    return nodo["info"]



"""Elimina dado index"""
def delete_element(my_list:dict, pos:int) -> dict:
    error_index(my_list, pos)
    if size(my_list) == 1:
        my_list["first"] = None
        my_list["last"] = None
    elif pos == 0:
        remove_first(my_list)
    elif pos == (size(my_list) - 1):
        remove_last(my_list)
    else:
        nodo = avanzar(my_list, pos - 1)
        nodo["next"] = nodo["next"]["next"]
        my_list["size"] -= 1
    return my_list



"""Elimina el primero"""
def remove_first(my_list:dict) -> dict:
    error_vacia(my_list)
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= 1
    if my_list["first"] is None:
        my_list["last"] = None
    return my_list



"""Elimina el último"""
def remove_last(my_list: dict) -> dict:
    error_vacia(my_list)
    if size(my_list) == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        nodo = avanzar(my_list, size(my_list) - 2)
        nodo["next"] = None
        my_list["last"] = nodo
    my_list["size"] -= 1
    return my_list



"""Inserta elemento dado index"""
def insert_element(my_list:dict, element, pos:int) -> dict:
    error_index(my_list, pos)
    if pos == 0:
        add_first(my_list, element)
    elif pos == (size(my_list)-1):
        add_last(my_list, element)
    else:
        nodo = no.new_single_node(element)
        nodo_anterior = avanzar(my_list, pos-1)
        nodo["next"] = nodo_anterior["next"]
        nodo_anterior["next"] = nodo
        my_list["size"] += 1
    return my_list



"""Función de comparación"""
def default_function(element_1, element_2) -> int:
    valor = al.efault_function(element_1, element_2)
    return valor



"""¿Está presente?"""
def is_present(my_list:dict, element, cmp_function) -> int:
    nodo = my_list["first"]
    posicion = 0
    index = -1
    while nodo is not None and index == -1:
        if cmp_function(element, nodo["info"]) == 0:
            index = posicion
        nodo = nodo["next"]
        posicion += 1
    return index



""""""
def change_info(my_list:dict, pos:int, new_info) -> dict:
    error_index_con_negativos(my_list, pos)
    nodo = avanzar(my_list, pos)
    nodo["info"] = new_info
    return my_list



"""Intercambia dos nodos"""
def exchange(my_list: dict, pos_1: int, pos_2: int) -> dict:
    error_index_con_negativos(my_list, pos_1)
    error_index_con_negativos(my_list, pos_2)
    if pos_1 == pos_2:
        resultado = my_list
    else:
        if pos_1 > pos_2:
            pos_1, pos_2 = pos_2, pos_1
        nodo1 = avanzar(my_list, pos_1)
        nodo2 = avanzar(my_list, pos_2)
        nodo_anterior1 = avanzar(my_list, pos_1 - 1) if pos_1 > 0 else None
        nodo_anterior2 = avanzar(my_list, pos_2 - 1)
        if size(my_list) == 2:
            nodo1["next"] = None
            nodo2["next"] = nodo1
            my_list["first"], my_list["last"] = nodo2, nodo1
        else:
            if nodo1 == my_list["first"]:
                my_list["first"] = nodo2
            else:
                nodo_anterior1["next"] = nodo2
            if nodo2 == my_list["last"]:
                my_list["last"] = nodo1
            nodo_anterior2["next"] = nodo1
            nodo1["next"], nodo2["next"] = nodo2["next"], nodo1["next"]
        resultado = my_list
    return resultado



"""Sublista single linked list dado index y # de elementos"""
def sub_list(my_list:dict, pos:int, num_elements:int) -> dict:
    error_index_con_negativos(my_list, pos)
    sub_single_linked_list = new_list()
    nodo = avanzar(my_list, pos)
    contador = 0
    while nodo is not None and contador < num_elements:
        add_last(sub_single_linked_list, nodo["info"])
        nodo = nodo["next"]
        contador += 1
    return sub_single_linked_list



"""Funciones auxiliares"""



"""Si una lista esta vacia"""
def error_vacia(my_list:dict) -> None:
    vacia = is_empty(my_list)
    if vacia == True:
        raise IndexError("list index out of range")
    return None



"""Si el index dado no esta dentro de la lista"""
def error_index(my_list:dict, pos:int) -> None:
    if not isinstance(pos, int) or pos < 0 or pos >= my_list["size"]:
        raise IndexError("list index out of range")
    return None



"""Si el index dado no esta dentro de la lista... incluso con index negativos"""
def error_index_con_negativos(my_list:dict, pos:int) -> None:
    tamano = my_list["size"]
    if not isinstance(pos, int) or pos < -tamano or pos >= tamano:
        raise IndexError("list index out of range incluyendo negativos")
    return None



"""Avanzar en el nodo dado un index"""
def avanzar(my_list:dict, pos:int) -> dict:
    pos_act = 0
    nodo = my_list["first"]
    while pos_act < pos:
        nodo = nodo["next"]
        pos_act += 1
    return nodo



"""Eliminar cuando solo hay un elemento"""
def eliminar_el_unico(my_list:dict) -> dict:
    if size(my_list) == 1:
        my_list["first"] = None
        my_list["last"] = None
    return my_list