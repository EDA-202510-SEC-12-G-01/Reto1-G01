"""Crea el nodo"""
def new_single_node(element)->dict:
    node = {"info": element, "next": None}
    return node



"""Da la información del nodo"""
def get_element(node:dict):
    elemento = node["info"]
    return elemento



"""Dice quien es el siguiente nodo"""
def get_next(node:dict)->dict:
    siguiente_nodo = node.get("next", None)
    return siguiente_nodo