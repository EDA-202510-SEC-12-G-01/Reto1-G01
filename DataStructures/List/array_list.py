"""Crear lista"""
def new_list() -> dict:
    nueva_lista = {"size":0, "elements":[]}
    return nueva_lista
    
    
    
"""¿La lista está vacia?"""
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
    error_element(element)
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list



"""Agregar al final"""
def add_last(my_list:dict, element) -> dict:
    error_element(element)
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list



"""Primer elemento"""
def first_element(my_list:dict):
    error_vacia(my_list)
    primer_elemento = my_list["elements"][0]
    return primer_elemento



"""Último elemento"""
def last_element(my_list:dict):
    error_vacia(my_list)
    ultimo_elemento = my_list["elements"][-1]
    return ultimo_elemento



"""Trae elemento"""
def get_element(my_list:dict, pos:int):
    error_index(my_list, pos)
    elemento = my_list["elements"][pos]
    return elemento



"""Elimina elemento por posición"""
def delete_element(my_list:dict, pos:int) -> dict:
    error_vacia(my_list)
    error_index(my_list, pos)
    del my_list["elements"][pos]
    my_list["size"] -=1
    return my_list



"""Elimina el primero"""
def remove_first(my_list:dict) -> dict:
    error_vacia(my_list)
    del my_list["elements"][0]
    my_list["size"] -=1
    return my_list



"""Elimina el último"""
def remove_last(my_list:dict) -> dict:
    error_vacia(my_list)
    del my_list["elements"][-1]
    my_list["size"] -=1
    return my_list



"""Insertar elemento en posición index"""
def insert_element(my_list: dict, element, pos:int) -> dict:
    error_element(element)
    error_index_con_negativos(my_list, pos)
    my_list["elements"].insert(pos,element)
    my_list["size"] +=1
    return my_list




"""Función de comparación"""
def default_function(element_1, element_2) -> int:
    comparaciones(element_1, element_2)
    valor = 0
    if element_1 > element_2:
        valor = 1
    elif element_1 < element_2:
       valor = -1
    return valor



"""¿Está presente?"""
def is_present(my_list: dict, element, cmp_function) -> int:
    error_element(element)
    tamano = my_list["size"]
    posicion = -1
    for index in range(tamano):
        elemento = my_list["elements"][index]
        if default_function(element, elemento) == 0:
            posicion = index
    return posicion



"""Cambiar información"""
def change_info(my_list:dict, pos:int, new_info) -> dict:
    error_index_con_negativos(my_list, pos)
    my_list["elements"][pos] = new_info
    return my_list



"""Intercambia información"""
def exchange(my_list:dict, pos_1:int, pos_2:int) -> dict:
    error_index_con_negativos(my_list, pos_1)
    error_index_con_negativos(my_list, pos_2)
    elemento_1 = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = elemento_1
    return my_list



"""Da una sublista"""
def sub_list(my_list: dict, pos_i: int, num_elements: int) -> dict:
    error_index_con_negativos(my_list, pos_i)
    pos_final = min(pos_i + num_elements, my_list["size"])
    sub_array_list = new_list()
    for elemento in range(pos_i, pos_final):
        add_last(sub_array_list, my_list["elements"][elemento])
    return sub_array_list



"""Funciones Auxiliares"""



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



"""Si el elemento a ingresar es un None"""
def error_element(element) -> None:
    if element is None:
        raise IndexError("El elemento es un None")
    return None



"""Si una lista esta vacia"""
def error_vacia(my_list:dict) -> None:
    vacia = is_empty(my_list)
    if vacia == True:
        raise IndexError("list index out of range")
    return None



"""¿Se puede comparar y si si, cambiar str?"""
def comparaciones(element_1, element_2) -> None:
    error_elementos_incomparables(element_1, element_2)
    if isinstance(element_1, str):
        element_1 = str_a_minusculas(element_1)
        element_2 = str_a_minusculas(element_2)
    if isinstance(element_1, (list, tuple)):
        comparar_listas(element_1, element_2)
    return None



""" Si se comparan 2 elementos que no se pueden comparar """
def error_elementos_incomparables(element_1, element_2) -> None:
    error_element(element_1)
    error_element(element_2)
    if not (isinstance(element_1, type(element_2)) or 
            (isinstance(element_1, (int, float)) and isinstance(element_2, (int, float)))):
        raise IndexError("Elementos incomparables")
    return None



""" Si se comparan 2 str.. deben estar en minúsculas """
def str_a_minusculas(element_1: str) -> str:
    return element_1.lower()




""" Si se comparan 2 listas """
def comparar_listas(element_1: list, element_2: list) -> None:
    if len(element_1) != len(element_2):
        raise ValueError("Las listas deben tener la misma longitud")
    for i in range(len(element_1)):
        cosa_1 = element_1[i]
        cosa_2 = element_2[i]
        if isinstance(cosa_1, list) and isinstance(cosa_2, list):
            comparar_listas(cosa_1, cosa_2)
            continue  
        error_elementos_incomparables(cosa_1, cosa_2)
        if isinstance(cosa_1, str) and isinstance(cosa_2, str):
            element_1[i] = str_a_minusculas(cosa_1)
            element_2[i] = str_a_minusculas(cosa_2)
    return None