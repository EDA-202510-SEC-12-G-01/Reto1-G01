import time
import csv
import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Stack import stack_single as ss
from DataStructures.Stack import stack_array as sa
from DataStructures.Queue import queue_array as qa
from DataStructures.Queue import queue_single as qs
data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Data")
csv.field_size_limit(2147483647)



"""Inicia las estructuras"""
def new_logic() -> dict:
    catalogo = {
        "single_linked_list": sl.new_list(), 
        "array_list": al.new_list(), 
    }
    return catalogo



"""Funciones para la carga de datos"""



"""Carga los datos"""
def load_data(catalog: dict, filename:str) -> dict:
    filepath = os.path.join(data_dir, filename)
    with open(filepath, encoding='utf-8') as file:
        input_file = csv.DictReader(file)
        for fila in input_file:
            agregar_fila_del_csv(catalog, fila)
    numero = cantidad_de_registros(catalog)
    menor_ano_registro = obtener_menor_año(catalog)
    mayor_ano_registro = obtener_mayor_año(catalog)
    recientes_viejos = cinco_recientes_cinco_viejos(catalog)
    requerimientos = al.new_list()
    al.add_last(requerimientos, numero)
    al.add_last(requerimientos, menor_ano_registro)
    al.add_last(requerimientos, mayor_ano_registro)
    al.add_last(requerimientos, recientes_viejos)
    return requerimientos



"""Consulta sobre el catálogo"""



"""Trae dato por su ID"""
def get_data(catalog:dict, id:int):
    al.error_index_con_negativos(catalog["array_list"], id)
    dato = al.get_element(catalog["array_list"], id)
    return dato



"""da el último registro recopilado según el año de interés"""
def Req_1_grupal_ultimo_registro_recopilado_segun_ano(catalog:dict, year:int) -> dict:
    tiempo_inicio = time.perf_counter()
    total_registros = 0
    if not catalog or "array_list" not in catalog or not catalog["array_list"] or not catalog["array_list"]["elements"]:
        registro = None
        resultado = crear_respuesta_arraylist(total_registros, tiempo_inicio, registro)
    else:
        ultimo_registro = None
        for registro in catalog["array_list"]["elements"]:
            if es_registro_del_año(registro, year):
                total_registros += 1
                if es_mas_reciente(registro, ultimo_registro):
                    ultimo_registro = registro
        registro = extraer_datos(ultimo_registro) if ultimo_registro else None
        resultado = crear_respuesta_arraylist(total_registros, tiempo_inicio, registro)
    return resultado



"""Ultimo registro cargado del departamento"""
def Req_2_grupal_ultimo_registro_departamento(catalog:dict, department:str) -> dict:
    tiempo_inicio = time.perf_counter()
    ultimo_registro = None
    total_registros = 0
    if not catalog or "array_list" not in catalog or not catalog["array_list"] or not catalog["array_list"]["elements"]:
        registro = None
        resultado = crear_respuesta_arraylist(total_registros, tiempo_inicio, registro)
    else:
        for registro in catalog["array_list"]["elements"]:
            if es_del_departamento(registro, department):
                total_registros += 1
                if es_mas_reciente(registro, ultimo_registro):
                    ultimo_registro = registro
    respuesta = crear_respuesta_arraylist(total_registros, tiempo_inicio, ultimo_registro)
    return respuesta



"""Registros recopilado por departamento para periodo de tiempo"""
def Req_3_individual_listar_registros_departamento_periodo(catalog:dict, department:str, anio_inicio:int, anio_fin:int) -> list:
    tiempo_inicio = time.perf_counter()
    if not catalog or "array_list" not in catalog or not catalog["array_list"] or not catalog["array_list"]["elements"]:
        registro_final = al.new_list()
        respuesta =crear_respuesta_arraylist34(0, 0, 0, tiempo_inicio, registro_final)
    else:
        registros_filtrados = filtrar_registros_departamento_periodo(catalog, department, anio_inicio, anio_fin)
        total_registros = al.size(registros_filtrados)
        total_survey, total_census = contar_SURVEY_CENSUS(registros_filtrados)
        registros_finales = supera_los_20(registros_filtrados)
        respuesta = crear_respuesta_arraylist34(total_registros, total_survey, total_census, tiempo_inicio, registros_finales)
    return respuesta



"""Registros recopilado por tipo de producto por periodo de tiempo"""
def Req_4_listar_registros_por_producto_periodo(catalog:dict, producto:str, anio_inicio:int, anio_fin:int) -> dict:
    tiempo_inicio = time.perf_counter()
    if not catalog or "array_list" not in catalog or not catalog["array_list"] or not catalog["array_list"]["elements"]:
        registro_final = al.new_list()
        respuesta = crear_respuesta_arraylist34(0, 0, 0, tiempo_inicio, registro_final)
    else:
        registros_filtrados = filtrar_registros_producto_periodo(catalog, producto, anio_inicio, anio_fin)
        total_registros = al.size(registros_filtrados)
        total_survey, total_census = contar_SURVEY_CENSUS(registros_filtrados)
        registros_finales = supera_los_20(registros_filtrados)
        respuesta = crear_respuesta_arraylist(total_registros, total_survey, total_census, tiempo_inicio, registros_finales)
    return respuesta



"""Registros cargado por categoria estadistica por periodo de tiempo"""
def Req_5_listar_registros_por_categoria_periodo(catalog:dict, categoria:str, anio_inicio:int, anio_fin:int) -> dict:
    tiempo_inicio = time.perf_counter()
    if not catalog or "array_list" not in catalog or not catalog["array_list"] or not catalog["array_list"]["elements"]:
        registro_final = al.new_list()
        respuesta = crear_respuesta_arraylist34(0, 0, 0, tiempo_inicio, registro_final)
    else:
        registros_filtrados = filtrar_registros_categoria_periodo(catalog, categoria, anio_inicio, anio_fin)
        total_registros = al.size(registros_filtrados)
        total_survey, total_census = contar_SURVEY_CENSUS(registros_filtrados)
        registros_finales = supera_los_20(registros_filtrados)
        respuesta = crear_respuesta_arraylist34(total_registros, total_survey, total_census, tiempo_inicio, registros_finales)
    return respuesta



"""Departamento y fecha de carga"""
def Req_6_analizar_registros_por_departamento(catalog: dict, departamento: str, fecha_inicio: str, fecha_fin: str) -> dict:
    tiempo_inicio = time.perf_counter()
    if not catalog or "array_list" not in catalog or not catalog["array_list"] or not catalog["array_list"]["elements"]:
        registro_final = al.new_list()
        respuesta = crear_respuesta_arraylist34(0, 0, 0, tiempo_inicio, registro_final)
    else:
        registros_filtrados = filtrar_registros_cargados_departamento_periodo(catalog, departamento, fecha_inicio, fecha_fin)
        total_registros = al.size(registros_filtrados)
        total_survey, total_census = contar_SURVEY_CENSUS(registros_filtrados)
        registros_finales = supera_los_20(registros_filtrados)
        respuesta = crear_respuesta_arraylist34(total_registros, total_survey, total_census, tiempo_inicio, registros_finales)
    return respuesta




"""Funciones auxiliares"""



"""Agrega la información de una fila del scv a la array list"""
def agregar_fila_del_csv(catalog:dict, elemento):
    al.add_last(catalog['array_list'], elemento)
    return elemento



"""Contar elemento de la lista"""
def cantidad_de_registros(catalog:dict):
    return al.size(catalog['array_list'])



"""Retorna en menor año en el registro"""
def obtener_menor_año(catalog:dict):
    anos = al.new_list()
    for registro in catalog['array_list']["elements"]:
        ano = int(registro["year_collection"])
        al.add_last(anos, ano)
    ano_menor = min(anos["elements"])
    return ano_menor



"""Retorna en mayor año en el registro"""
def obtener_mayor_año(catalog:dict):
    anos = al.new_list()
    for registro in catalog['array_list']["elements"]:
        ano = int(registro["year_collection"])
        al.add_last(anos, ano)
    ano_mayor = max(anos["elements"])
    return ano_mayor



"""trae la información de los 5 más recientes y los 5 más viejos"""
def cinco_recientes_cinco_viejos(catalog:dict) -> dict:
    registros = catalog['array_list']["elements"]
    registros_ordenados = sorted(registros, key=lambda x: int(x["year_collection"]))
    primeros_5 = al.new_list()
    ultimos_5 = al.new_list()
    for registro in registros_ordenados[:5]:
        al.add_last(primeros_5, {
            "Año de recolección del registro": registro["year_collection"],
            "Fecha de carga del registro": registro["load_time"],
            "Nombre del departamento del registro": registro["state_name"],
            "Tipo de fuente/origen del registro": registro["source"],
            "Unidad de medición del registro": registro["unit_measurement"],
            "Valor de la medición del registro": registro["value"]
        })
    for registro in registros_ordenados[-5:]:
        al.add_last(ultimos_5, {
            "Año de recolección del registro": registro["year_collection"],
            "Fecha de carga del registro": registro["load_time"],
            "Nombre del departamento del registro": registro["state_name"],
            "Tipo de fuente/origen del registro": registro["source"],
            "Unidad de medición del registro": registro["unit_measurement"],
            "Valor de la medición del registro": registro["value"]
        })
    resultado = al.new_list()
    al.add_last(resultado, {"primeros 5": primeros_5, "últimos 5": ultimos_5})
    return resultado



"""Extrae los datos por la fecha"""
def extraer_datos(registro:dict) -> dict:
    datos = {
        "Año de recopilación del registro": registro["year_collection"],
        "Fecha de carga del registro a la plataforma": registro["load_time"],
        "Tipo de fuente/origen del registro": registro["source"],
        "Frecuencia de la recopilación del registro": registro["freq_collection"],
        "Nombre del departamento del registro": registro["state_name"],
        "Tipo del producto del registro": registro["commodity"],
        "Unidad de medición del registro": registro["unit_measurement"],
        "Valor de la medición del registro": registro["value"],
    }
    return datos



"""¿El registro es del año?"""
def es_registro_del_año(registro: dict, year: int) -> bool:
    year_str = registro["year_collection"].strip()  # Eliminar espacios extra
    print(f"Comparando año del registro: '{year_str}' con el año ingresado: '{year}'")
    return int(year_str) == year



"""Compara y dice cual tiene la fecha más reciente"""
def es_mas_reciente(registro_actual:dict, registro_ultimo:dict) -> bool:
    fecha_actual = datetime.strptime(registro_actual["load_time"], "%Y-%m-%d %H:%M:%S") 
    fecha_ultimo = datetime.strptime(registro_ultimo["load_time"], "%Y-%m-%d %H:%M:%S") if registro_ultimo else datetime.min 
    mas_reciente = False
    if fecha_actual > fecha_ultimo:
        mas_reciente = True
    return mas_reciente




"""Estructuración de respuestas"""
def crear_respuesta_arraylist(total_registros:int, tiempo_inicio:float, registro:dict) -> list:
    respuesta = al.new_list()
    tiempo_total = (time.perf_counter() - tiempo_inicio) * 1000
    datos_registro = extraer_datos(registro) if registro else None  
    al.add_last(respuesta, {"Tiempo de la ejecución": tiempo_total})
    al.add_last(respuesta, {"Número total de registros": total_registros})
    al.add_last(respuesta, {"Registro encontrado": datos_registro})
    return respuesta



"""¿El registro es del departamento?"""
def es_del_departamento(registro: dict, department: str) -> bool:
    es_del_departamento = False
    if registro["state_name"] == department:
        es_del_departamento = True
    return es_del_departamento



"""Estructuracion respuest para el 3"""
def crear_respuesta_arraylist34(total_registros, total_survey, total_census, tiempo_inicio, registros_finales) -> dict:
    respuesta = al.new_list()
    tiempo_total = (time.perf_counter() - tiempo_inicio) * 1000
    al.add_last(respuesta, {"Tiempo de la ejecución": tiempo_total})
    al.add_last(respuesta, {"Número total de registros": total_registros})
    al.add_last(respuesta, {"Número total de registros con tipo de fuente/origen SURVEY": total_survey})
    al.add_last(respuesta, {"Número total de registros con tipo de fuente/origen CENSUS": total_census})
    al.add_last(respuesta, {"Registro encontrado": registros_finales})
    return respuesta



"""Filtrar por departamento y periodo de tiempo"""
def filtrar_registros_departamento_periodo(catalog, department, anio_inicio, anio_fin):
    registros_filtrados = al.new_list()
    for registro in catalog["array_list"]["elements"]:
        anio_recoleccion = int(registro["year_collection"])
        if es_del_departamento(registro, department) and anio_inicio <= anio_recoleccion <= anio_fin:
            al.add_last(registros_filtrados, registro)
    return registros_filtrados



"""Contar tipos de SURVEY y tipos de CENSUS"""
def contar_SURVEY_CENSUS(registros):
    total_survey = 0
    total_census = 0
    for registro in registros:
        if registro["source"] == "SURVEY":
            total_survey += 1
        elif registro["source"] == "CENSUS":
            total_census += 1
    return total_survey, total_census



"""Si se superan los 20 registros"""
def supera_los_20(registros):
    if registros["size"] > 20:
        mostrar = registros["elements"][:5] + registros["elements"][-5:]
    else:
        mostrar = registros["elements"]
    return mostrar



"""Filtra por periodo y producto"""
def filtrar_registros_producto_periodo(catalog, producto, anio_inicio, anio_fin):
    resultado = al.new_list()
    for i in range(al.size(catalog["array_list"])):
        registro = al.get_element(catalog["array_list"], i)
        if registro["commodity"] == producto and anio_inicio <= int(registro["year_collection"]) <= anio_fin:
            nuevo_registro = {
                "source": registro["source"],
                "Año de recopilación": registro["year_collection"],
                "Fecha de carga": registro["date_loaded"],
                "Frecuencia": registro["freq"],
                "Departamento": registro["state"],
                "Unidad de medición": registro["unit"]
            }
            al.add_last(resultado, nuevo_registro)
    return resultado



"""filtrar por categoria y perdiodo de tiempo"""
def filtrar_registros_categoria_periodo(catalog, categoria, anio_inicio, anio_fin):
    resultado = al.new_list()
    for i in range(al.size(catalog["array_list"])):
        registro = al.get_element(catalog["array_list"], i)
        if "load_time" in registro and len(registro["load_time"]) >= 4:
            anio_carga = int(registro["load_time"][:4])
            if registro["stat_category"] == categoria and anio_inicio <= anio_carga <= anio_fin:
                nuevo_registro = {
                    "source": registro["source"],
                    "Año de recopilación": registro["year_collection"],
                    "Fecha de carga": registro["load_time"],
                    "Frecuencia": registro["freq"],
                    "Departamento": registro["state"],
                    "Unidad de medición": registro["unit"],
                    "Tipo de producto": registro["commodity"]
                }
                al.add_last(resultado, nuevo_registro)
    return resultado



"""Filtrar departamento, periodo, año de carga"""
def filtrar_registros_cargados_departamento_periodo(catalog, departamento, fecha_inicio, fecha_fin):
    resultado = al.new_list()
    for i in range(al.size(catalog["array_list"])):
        registro = al.get_element(catalog["array_list"], i)
        fecha_carga = registro["load_time"][:10]  # Extraer la fecha de carga en formato YYYY-MM-DD
        if registro["state"] == departamento and fecha_inicio <= fecha_carga <= fecha_fin:
            nuevo_registro = {
                "source": registro["source"],
                "Año de recopilación": registro["year_collection"],
                "Fecha de carga": registro["load_time"],
                "Frecuencia": registro["freq"],
                "Departamento": registro["state"],
                "Unidad de medición": registro["unit"],
                "Tipo de producto": registro["commodity"]
            }
            al.add_last(resultado, nuevo_registro)
    return resultado