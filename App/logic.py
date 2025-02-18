import time
import csv
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as sl

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

# Aumentar el límite de lectura del CSV para evitar errores con datos grandes
csv.field_size_limit(2147483647)


def new_logic():
    
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    """
    Inicializa la estructura de datos para almacenar los registros agrícolas.
    """
    agro = {'agricultural_records': None}
    
    #Inicializar la lista de registros agriculturales

    agro['agricultural_records'] = sl.new_list()
    return agro


# Funciones para la carga de datos

def load_data(agro):
    
    """
    Carga los registros agrícolas desde un archivo CSV en la estructura de datos.
    """
    
    file = data_dir + '/agricultural-20.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for row in input_file:
        add_row(agro, row)
    return agricultural_records_size(agro)

def add_row(agro, row):
    sl.add_last(agro["agricultural_records"],row)
    return agro

def agricultural_records_size(agro):
    return sl.size(agro['agricultural_records'])


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
