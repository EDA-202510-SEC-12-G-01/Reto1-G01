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

def load_data(agro, estructura, archivo:str):
    
    """
    Carga los registros agrícolas desde un archivo CSV en la estructura de datos.
    """
    
    file = data_dir + '/'+ archivo
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
    item = agro_al['agricultural_records']
    
    for i in range(0,min(5, al.size(agro_al['agricultural_records']))):
        al.add_last(first_last_five, al.get_element(item, i))

    for j in range(max(0, al.size(agro_al["agricultural_records"]) - 5), al.size(agro_al["agricultural_records"])):
        al.add_last(first_last_five, al.get_element(item, j))

    return first_last_five

# Funciones de consulta sobre el catálogo


def buscar_entre_anios(agro, fecha_inicio:int, fecha_fin:int):
    """
    Retorna una single linked list con los registros que se encuentran entre los años dados.
    """
    registros = sl.new_list()
    
    node = agro['agricultural_records']['first']
    while node is not None:
        if int(node['info']['year_collection']) >= int(fecha_inicio) and int(node['info']['year_collection']) <= int(fecha_fin):
            sl.add_last(registros, node['info'])
        node = node['next']
    
    return registros

def buscar_entre_anios_al(agro_al, fecha_inicio:int, fecha_fin:int):
    """
    Retorna una array list con los registros que se encuentran entre los años dados.
    """  
    
    fecha_inicio = fecha_inicio
    fecha_fin = fecha_fin
    registros = al.new_list()
    for i in range(0, al.size(agro_al['agricultural_records'])):
        registro = al.get_element(agro_al["agricultural_records"], i) 
        if int(registro["year_collection"]) >= fecha_inicio and int(registro["year_collection"]) <= fecha_fin:
            al.add_last(registros, registro)
            
    return registros
    

from datetime import datetime

def buscar_anios(agro, anio: int):
    """
    Retorna una single linked list con los registros que se encuentran entre los años dados.
    """
    registros = sl.new_list()
    
    node = agro['agricultural_records']['first']
    while node is not None:
        if int(node['info']['year_collection']) == anio:
            sl.add_last(registros, node['info'])
        node = node['next']
    
    return registros

from datetime import datetime

def req_1(agro, year: str):
    """
    Retorna el resultado del requerimiento 1
    """
    try:   
        anio = int(year)
    except ValueError:
        return None
    
    lista = buscar_anios(agro, anio)
    retorno_final = {"numero_registros": 0, "registro": {}}

    if sl.size(lista) == 0: 
        return False  

    else:
        numero_registro = 0
        fecha_max = None
        node = lista['first']
        
        while node is not None:
            item = node["info"]
            fecha_2 = datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S")
            numero_registro += 1

            if fecha_max is None or fecha_2 > fecha_max:
                fecha_max = fecha_2

            node = node['next']

        if fecha_max is None:
            return retorno_final

        fecha_max_str = fecha_max.strftime("%Y-%m-%d %H:%M:%S")
        
        node = lista['first']
        while node is not None:
            item = node["info"]

            if item["load_time"] == fecha_max_str:
                retorno_final["numero_registros"] = numero_registro
                retorno_final["registro"] = item
                return retorno_final
            
            node = node['next']
   
    return retorno_final



def measure_req_1(agro, year:str):
    """
    Retorna el resultado del requerimiento 1
    """
    start = get_time()
    req_1(agro, year)
    end = get_time()
    return delta_time(start, end)

def measure_req_2(agro, departamento:str):
    """
    Retorna el resultado del requerimiento 2
    """
    start = get_time()
    req_2(agro, departamento)
    end = get_time()
    return delta_time(start, end)

def req_2(agro, departamento:str):
    """
    Retorna el resultado del requerimiento 2
    """
    
    fecha_1 = datetime.strptime("2011-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")
    retorno_final = {"numero_registros": 0, "registro": {}}
    node = agro["agricultural_records"]["first"]
    numero_registro = 0
    while node is not None:
        item = node["info"]
        if item["state_name"] == departamento:
            fecha_2 = datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S")
            if fecha_2 > fecha_1:
                fecha_1 = fecha_2
            numero_registro += 1
        node = node["next"]
    fecha_min = fecha_1.strftime("%Y-%m-%d %H:%M:%S")
    node = agro['agricultural_records']['first']
    while node is not None:
        item = node["info"]
        if item["load_time"] == fecha_min and item["state_name"] == departamento:
            retorno_final["numero_registros"] = numero_registro
            retorno_final["registro"] = item
            
            return retorno_final
        node = node['next']
    return(retorno_final)


def measure_req_3(agro_al, department: str, año_inicio: str, año_fin: str):
    start = get_time()
    resultado = req_3(agro_al, department, año_inicio, año_fin)
    end = get_time()
    return resultado, delta_time(start, end)


def req_3(agro_al, department: str, año_inicio: str, año_fin: str):
    try:
        año_inicio = int(año_inicio)
        año_fin = int(año_fin)
    except ValueError:
        return "Error: ingreso un tipo de dato no válido"
    lista = buscar_entre_anios_al(agro_al, año_inicio, año_fin)
    filtro = al.new_list()
    census, survey = 0, 0
    for i in range(al.size(lista)):
        item = al.get_element(lista, i)
        if item["state_name"] == department:
            al.add_last(filtro, item)
            if item["source"] == "SURVEY":
                survey += 1
            elif item["source"] == "CENSUS":
                census += 1
    size = al.size(filtro)
    if size == 0:
        return "No se encontraron registros"
    if size > 20:
        seleccionados = filtro["elements"][:5] + filtro["elements"][-5:]
    else:
        seleccionados = filtro["elements"]
    return {
        "total_registros": size,
        "survey_count": survey,
        "census_count": census,
        "registros": seleccionados
    }
    

def measure_req_4al(agro_al, commodity:str, año_inicio:str, año_fin:str):
    """
    Retorna el tiempo de ejecución  del requerimiento 4
    """
    start = get_time()
    req_4al(agro_al,commodity, año_inicio, año_fin)
    end = get_time()
    return delta_time(start, end)    


def req_4al(agro_al, commodity:str, año_inicio:str, año_final:str):
    
    try:
        año_inicio = int(año_inicio)  
        año_final = int(año_final)
    except ValueError:  
        return ("Error: ingreso un tipo de dato no válido")
    
    lista = buscar_entre_anios_al(agro_al, año_inicio, año_final)
    filtro = al.new_list()
    st_req = stal.new_stack()
    census = 0
    survey = 0

    for i in range(al.size(lista)): 
        item = al.get_element(lista, i)
        if item["commodity"] == commodity:
            al.add_last(filtro, item)
            if item["source"] == "SURVEY":
                survey += 1
            elif item["source"] == "CENSUS":
                census += 1

    size = al.size(filtro)
    
    if size == 0:
        return False

    if size <= 20:
        for k in range(0, size):
            item = al.get_element(filtro, k)  
            stal.push(st_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                item["freq_collection"], item["state_name"],item["unit_measurement"], item["commodity"]))
        return (st_req, False, size, census, survey)
    else:
        al_req = al.new_list()
        for i in range(0, 5):
            item = al.get_element(filtro, i)  
            al.add_last(al_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                item["freq_collection"], item["state_name"],item["unit_measurement"], item["commodity"]))
        for j in range(size - 5, size):
            item = al.get_element(filtro, j)
            al.add_last(al_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                item["freq_collection"], item["state_name"],item["unit_measurement"], item["commodity"]))
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
#     """
#     Retorna el resultado del requerimiento 4
#     """
#     lista = buscar_entre_anios(agro, año_inicio, año_fin)
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
    # TODO: Modificar el requerimiento 5
    pass

def buscar_entre_fechas_al(agro_al, fecha_inicial:str, fecha_final:str):
    
    try:
        fecha_inicio = datetime.strptime(fecha_inicial, "%Y-%m-%d %H:%M:%S")
        fecha_fin = datetime.strptime(fecha_final, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return("Error: tipo de dato no válido")

    registros = al.new_list()

    for i in range(0, al.size(agro_al["agricultural_records"])):
        registro = al.get_element(agro_al["agricultural_records"], i)
        fecha_load = datetime.strptime(registro["load_time"], "%Y-%m-%d %H:%M:%S")
        if fecha_inicio <= fecha_load <= fecha_fin:
            
            al.add_last(registros, registro)

    return registros

def measure_req_6(agro_al, departamento:str, año_inicio:str, año_fin:str):
    """
    Retorna el tiempo de ejecución  del requerimiento 6
    """
    start = get_time()
    req_6(agro_al,departamento, año_inicio, año_fin)
    end = get_time()
    return delta_time(start, end)    

def req_6(agro_al, departamento:str, fecha_inicial:str, fecha_final:str):
    
    """
    Retorna el resultado del requerimiento 6
    """

    filtro = al.new_list()
    st_req = stal.new_stack()
    census = 0
    survey = 0
    lista = buscar_entre_fechas_al(agro_al, fecha_inicial, fecha_final)
    
    try:
        for i in range(0, al.size(lista)):
            item = al.get_element(lista, i)
            if item["state_name"] == departamento:
                al.add_last(filtro, item)
                if item["source"] == "CENSUS":
                    census += 1
                if item["source"] == "SURVEY":
                    survey += 1
    except TypeError:
        return("Error: Fecha ingresada no válida") 
    
    size = sl.size(filtro)
    
    if size == 0:
        return None
    
    if size <= 20:
        for k in range(0, size):
            item = al.get_element(filtro, k)  
            stal.push(st_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"), 
                               item["freq_collection"], item["state_name"],item["unit_measurement"], item["commodity"]))
            
        return (st_req, False, size, census, survey)

    else:
        al_req = al.new_list()
        for i in range(0, 5):
            item = al.get_element(filtro, i)  
            al.add_last(al_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                item["freq_collection"], item["state_name"],item["unit_measurement"], item["commodity"]))
        for j in range(size - 5, size):
            item = al.get_element(filtro, j)
            al.add_last(al_req, (item["source"], item["year_collection"], datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d"),
                item["freq_collection"], item["state_name"],item["unit_measurement"], item["commodity"]))
            
        return (al_req, True, size, census, survey)
        
        
def measure_req_7(agro_al, department: str, año_inicio: str, año_fin: str):
    """
    Retorna el tiempo de ejecución del requerimiento 7.
    """
    start = get_time()
    req_7(agro_al, department, año_inicio, año_fin)
    end = get_time()
    return delta_time(start, end)

def remover_value_lista(filtro, departamento):
    
    lista = sl.new_list()
    node = filtro["first"]
    while node is not None:
        item = node["info"]
        if item["state_name"] == departamento and "$" in item["unit_measurement"] and item["value"] != "(D)":
            sl.add_last(lista, item)
        node = node["next"]

    return(lista)

        
def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
            return False  

def req_7(agro, departmento: str, año_inicio: str, año_fin: str):
    
    """
    Retorna el análisis del periodo con mayores y menores ingresos para un departamento.
    """

    año_inicio = int(año_inicio)
    año_fin = int(año_fin)

    lista = buscar_entre_anios(agro, año_inicio, año_fin)
    lista_filtrada = remover_value_lista(lista, departmento)
    total_registros = sl.size(lista_filtrada)

    ingresos_por_año = {}

    node = lista_filtrada["first"]

    while node is not None:
        item = node["info"]
        anio = int(item["year_collection"]) 

        if anio not in ingresos_por_año:
            ingresos_por_año[anio] = {
                "lista": sl.new_list(),
                "total_ingresos": 0,
                "census": 0,
                "survey": 0,
                "validos": 0,
                "no_validos": 0
            }

        sl.add_last(ingresos_por_año[anio]["lista"], item)

        node = node["next"]

    anio_mayor = None
    anio_menor = None
    ingresos_mayor = 0
    ingresos_menor = pow(10,10)

    for anio in ingresos_por_año:
        
        data = ingresos_por_año[anio]
   
        #Acceso a la llave donde estan los single linked list para hacer las comparaciones
        lista = data["lista"]

        node = lista["first"]
        
        while node is not None:
            item = node["info"]

            if item["source"] == "CENSUS":
                data["census"] += 1
            elif item["source"] == "SURVEY":
                data["survey"] += 1

            # Validar si el valor es un número y sumarlo a los ingresos del año
            tipo = es_numero(item["value"])
            if tipo == True:
                data["total_ingresos"] += float(item["value"])
                data["validos"] += 1
            else:
                data["no_validos"] += 1

            node = node["next"]

        if data["total_ingresos"] > ingresos_mayor:
            ingresos_mayor = data["total_ingresos"]
            anio_mayor = anio
            dicr = data

        if data["total_ingresos"] < ingresos_menor:
            ingresos_menor = data["total_ingresos"]
            anio_menor = anio
            dicm = data

    return ((anio_mayor,"MAYOR",ingresos_mayor, dicr["validos"], dicr["no_validos"], dicr["survey"], dicr["census"]), (anio_menor, "MENOR", ingresos_menor, dicm["validos"], dicm["no_validos"], dicm["survey"], dicm["census"]), total_registros)


def measure_req_8(agro):
    """
    Retorna el tiempo de ejecución  del requerimiento 8
    """
    start = get_time()
    req_8(agro)
    end = get_time()
    return delta_time(start, end)   

def filtrar_registros_valor(agro):
    #Ignorar registros con $ y value D
    lista = sl.new_list()
    node = agro["agricultural_records"]["first"]
    while node is not None:
        item = node["info"]     
        if not ("$" in item["unit_measurement"] and item["value"] == "(D)"):

            sl.add_last(lista, item)

        node = node["next"]
        
    return(lista)

def req_8(agro):
    
    """
        REQ. 8: Identificar el departamento con mayor diferencia promedio de 
        tiempo de recolección y publicación de registros (B)
    """

    #Filtrar la lista para no tener en cuenta los valores $ con ("D")
    lista = filtrar_registros_valor(agro)
    node = lista['first']
    dic_estados = {}
    mayor = 0
    total_estados = 0  
    suma_registros = 0
    numero_registros = 0
    mayor_anio = 0
    menor_anio = pow(10,10)
    

    while node is not None:
        item = node['info']
        estado = item["state_name"]
        c = False
        s = False
        
        if estado not in dic_estados:
            dic_estados[estado] = sl.new_list()  
            total_estados += 1

        # Extraer el año de la carga de datos y de recolección
        fecha_dt = datetime.strptime(item["load_time"], "%Y-%m-%d %H:%M:%S")
        registro = fecha_dt.year
        año = int(item["year_collection"])
        
        # Calcular menor y mayor año general
        if año < menor_anio:
            menor_anio = año
        if año > mayor_anio:
            mayor_anio = año

        # Sumar registros para el promedio
        numero_registros += 1
        suma_registros += registro
        
        # Calcular diferencia
        diferencia = abs(registro - año)
        if item["source"] == "CENSUS":
            c = True
        if item["source"] == "SURVEY":
            s = True
        
        # Crear nodo para la lista enlazada de cada estado
        nodo_info = {
            "diferencia": diferencia,
            "census": c,
            "survey": s,
            "año": año
        }

        sl.add_last(dic_estados[estado], nodo_info)
        node = node["next"]

    # Calcular promedio de cargas
    if numero_registros == 0:
        promedio_cargas = 0
    else:   
        promedio_cargas = suma_registros / numero_registros 

    ret = ()
    for estado in dic_estados:  
        lista = dic_estados[estado]
        total = 0
        census = 0
        survey = 0
        año_max = 0
        diferencia_max = 0
        año_min = pow(10,10)
        diferencia_min = pow(10,10)

        registros = lista["size"]
        node = lista["first"]

        while node is not None:
            item = node["info"]
            total += item["diferencia"]
                  
            if item["census"]:
                census += 1
            if item["survey"]:
                survey += 1
            
            if item["año"] > año_max:
                año_max = item["año"]
            if item["año"] < año_min:
                año_min = item["año"]
                
            if item["diferencia"] > diferencia_max:
                diferencia_max = item["diferencia"]
            if item["diferencia"] < diferencia_min:
                diferencia_min = item["diferencia"]
                 
            node = node["next"]

        # Calculo del promedio de diferencia
        if registros > 0:
            promedio = total/registros
        else:
            promedio = 0
            
        if promedio > mayor:
            mayor = promedio
            ret = (estado, promedio, año_max, año_min, diferencia_max, diferencia_min, census, survey, registros)

    return (ret, total_estados, mayor_anio, menor_anio, promedio_cargas)


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
