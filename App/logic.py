import time
import csv
import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Stack import stack as st
from DataStructures.Stack import stackal as stal

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

# Aumentar el límite de lectura del CSV para evitar errores con datos grandes
csv.field_size_limit(2147483647)


def new_logic(estructura):
    
    """
    Inicializa la estructura de datos para almacenar los registros agrícolas.
    """
    
    if estructura == "sl":
        #Inicializar una single_linked_list de registros agrícolas
        agro = {'agricultural_records': sl.new_list()}  
        return agro
    
    if estructura == "al":
        #Inicializar una array_list de registros agrícolas
        agro = {'agricultural_records': al.new_list()}  
        return agro
    
    else:
        return None
        
# Funciones para la carga de datos

agro = new_logic("sl")
agro_al = new_logic("al")

def load_data(agro, estructura):
    
    """
    Carga los registros agrícolas desde un archivo CSV en la estructura de datos.
    """
    
    file = data_dir + '/agricultural-mini.csv'
    input_file = csv.DictReader(open(file, encoding='utf-8'))
    for row in input_file:
        add_row(agro, row, estructura)
    return agricultural_records_size(agro)

def add_row(agro, row, estructura):
    """ 
    Añade un registro agrícola a la estructura de datos.
    """
    if estructura == "sl":
        sl.add_last(agro['agricultural_records'], row)
    if estructura == "al":
        al.add_last(agro['agricultural_records'], row)
    return agro

def agricultural_records_size(agro):
    """
    Retorna la cantidad de registros agrícolas. 
    """
    return sl.size(agro['agricultural_records'])


def less_recolection_yr(agro):
    """
    Retorna el menor año de recolección de datos.
    """
    if sl.size(agro['agricultural_records']) == 0:
        return None  
    
    menor_año = pow(10,10)  
    nodo = agro['agricultural_records']['first'] 

    while nodo is not None:  
        año = int(nodo['info']['year_collection']) 
        if año < menor_año:
            menor_año = año
        nodo = nodo['next']  

    return menor_año


def most_recolection_yr(agro):
    """
    Retorna el último año de recolección de datos.
    """
    if sl.size(agro['agricultural_records']) == 0:
        return None  

    mayor_año = 0  
    nodo = agro['agricultural_records']['first'] 

    while nodo is not None:  
        año = int(nodo['info']['year_collection']) 
        if año > mayor_año:
            mayor_año = año
        nodo = nodo['next']  

    return mayor_año

    
def registers_from_the_top(agro_al):
    """
    Retorna un diccionario con los primeros 5 y los últimos 5 registros.
    """
    if agro_al is None or agro_al['agricultural_records'] is None:
        return None
    
    first_last_five = al.new_list()
    
    for i in range(0,min(5, al.size(agro_al['agricultural_records']))):
        al.add_last(first_last_five, al.get_element(agro_al['agricultural_records'], i))

    for j in range(max(0, al.size(agro_al["agricultural_records"]) - 5), al.size(agro_al["agricultural_records"])):
        al.add_last(first_last_five, al.get_element(agro_al['agricultural_records'], j))

    return first_last_five

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def buscar_entre_fechas(agro, fecha_inicio:str, fecha_fin:str):
    """
    Retorna una single linked list con los registros que se encuentran entre las fechas dadas.
    """
    registros = sl.new_list()
    
    node = agro['agricultural_records']['first']
    while node is not None:
        if node['info']['year_collection'] >= fecha_inicio and node['info']['year_collection'] <= fecha_fin:
            sl.add_last(registros, node['info'])
        node = node['next']
    
    return registros

def buscar_entre_fechas_al(agro_al, fecha_inicio:str, fecha_fin:str):
    """
    Retorna una array list con los registros que se encuentran entre las fechas dadas.
    """
    registros = al.new_list()
    for i in range(0, al.size(agro_al['agricultural_records'])):
        registro = al.get_element(agro_al["agricultural_records"], i) 
        if registro["year_collection"] >= fecha_inicio and registro["year_collection"] <= fecha_fin:
            al.add_last(registros, registro)
     
    return registros

#fuerzas

def req_1(agro, year:str):
    # TODO: Modificar el requerimiento 1
    """
    Retorna el resultado del requerimiento 1
    """
    
    fecha_1 = datetime.strptime(year + "-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    registros = []
    retorno_final = {"numero_registros": 0, "registro": {}}
    if sl.size(agro['agricultural_records']) == 0: 
        return None  
    else:
        node = agro['agricultural_records']['first']
        while node is not None:
            if node['info']['year_collection'] == year:
                registros.append(node['info']["load_time"])
            node = node['next']

        numero_registros = len(registros)
        for j in registros:

            fecha_2 = datetime.strptime(j, "%Y-%m-%d %H:%M:%S")
            if fecha_2 > fecha_1:
                fecha_1 = fecha_2
        
        fecha_min = fecha_1.strftime("%Y-%m-%d %H:%M:%S")

        node = agro['agricultural_records']['first']
        while node is not None:
            if node["info"]["load_time"] == fecha_min:
                retorno_final["numero_registros"] = numero_registros
                retorno_final["registro"] = node["info"]
                
                return retorno_final
            
            node = node['next']
   

def measure_req_1(agro, year:str):
    """
    Retorna el resultado del requerimiento 1
    """
    start = get_time()
    req_1(agro, year)
    end = get_time()
    return delta_time(start, end)

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


def measure_req_4al(agro_al, commodity:str, año_inicio:str, año_fin:str):
    """
    Retorna el tiempo de ejecución  del requerimiento 1
    """
    start = get_time()
    req_4al(agro_al,commodity, año_inicio, año_fin)
    end = get_time()
    return delta_time(start, end)    


def req_4al(agro_al, commodity, año_inicio, año_fin):
    lista = buscar_entre_fechas_al(agro_al, año_inicio, año_fin)
    filtro = al.new_list()
    st_req = stal.new_stack()
    census, survey = 0, 0

    for i in range(al.size(lista)): 
        item = al.get_element(lista, i)
        if item["commodity"] == commodity:
            al.add_last(filtro, item)
            if item["source"] == "SURVEY":
                survey += 1
            elif item["source"] == "CENSUS":
                census += 1

    size = al.size(filtro)

    if size <= 20:
        for k in range(size):
            item = al.get_element(filtro, k)  
            stal.push(st_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                item["freq_collection"], item["state_name"], item["unit_measurement"]))
        return (st_req, False, size, census, survey)
    else:
        al_req = al.new_list()
        for i in range(0, min(5, size)):
            al.add_last(al_req, al.get_element(filtro, i))
        for j in range(max(0, size - 5), size):
            al.add_last(al_req, al.get_element(filtro, j))
        return (al_req, True, size, census, survey)

    


# def measure_req_4(agro, commodity:str, año_inicio:str, año_fin:str):
#     """
#     Retorna el tiempo de ejecución  del requerimiento 1
#     """
#     start = get_time()
#     req_4(agro,commodity, año_inicio, año_fin)
#     end = get_time()
#     return delta_time(start, end)    

# def req_4(agro, commodity, año_inicio, año_fin):
#     # TODO: Modificar el requerimiento 4
#     """
#     Retorna el resultado del requerimiento 4
#     """
#     lista = buscar_entre_fechas(agro, año_inicio, año_fin)
#     st_req = st.new_stack()
#     node = lista["first"]
#     while node is not None:
#         if node["info"]["commodity"] == commodity:
            
#             st.push(st_req, (node["info"]["source"], 
#                              node["info"]["year_collection"], 
#                              datetime.strptime(node["info"]["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"), 
#                              node["info"]["freq_collection"],
#                              node["info"]["state_name"], 
#                              node["info"]["unit_measurement"]))
                   
#         node = node["next"]
     
#     return st_req

    

def req_5(agro, categoria, año_inicio, año_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    
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
