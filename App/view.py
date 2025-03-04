import sys
import os
import App.logic as logic
sys.setrecursionlimit(10000)  # Ajustar límite de recursión si es necesario4
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DataStructures.Stack import stack as st
from DataStructures.Stack import stackal as stal


def new_logic(estructura:str):
    
    if estructura == "sl":
        control = logic.new_logic("sl")
        return control
    if estructura == "al":
        control = logic.new_logic("al")
        return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(archivo: str):
    """
    Carga los datos en ambas estructuras de datos
    """
    logic.load_data(control, "sl", archivo)  

    logic.load_data(control_lt, "al", archivo)  
    
def agric_records_size(control):
    """
    Retorna la cantidad de registros agrícolas
    """
    size = logic.agricultural_records_size(control)
    return size

def less_data_yr(control):
    less_recolection_yr = logic.less_recolection_yr(control)
    return less_recolection_yr

def most_data_yr(control):
    most_recolection_yr = logic.most_recolection_yr(control)
    return most_recolection_yr

def top_5_registers(control):
    top_registers = logic.registers_from_the_top(control)
    return top_registers


def print_test_req1(req1):
    """
    Imprime los resultados de las pruebas de rendimiento
    """
    print("Tiempo de ejecución para el requerimiento 1:",
          f"{req1:.3f}", "[ms]")
    

def print_req_1(control,year):
    
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    try:
        req_1 = logic.req_1(control,year)
        req1_result = logic.measure_req_1(control,year)
        
        if req_1 == None:
            print("Por favor ingrese un año valido.")
            return(req_1)
        
        if req_1["numero_registros"] == 0:
            print("No se encontraron registros.")
            
        else:     
            print("Numero total de registros: " + str(req_1["numero_registros"]))
            print("Último registro encontrado: ")
            print("Año de recolección: "+ req_1["registro"]["year_collection"])
            print("Año de carga: "+ req_1["registro"]["load_time"])
            print("Tipo de origen: "+ req_1["registro"]["source"])
            print("Frecuencia de recolección: "+ req_1["registro"]["freq_collection"])
            print("Nombre del departamento: "+ req_1["registro"]["state_name"])
            print("Tipo de producto: "+ req_1["registro"]["commodity"])
            print("Unidad de medidad: "+ req_1["registro"]["unit_measurement"])
            print("Valor unitario del registro: "+ req_1["registro"]["value"])
            
        print_test_req1(req1_result)  
    except TypeError:
        print("Error: Por favor cargue los datos.")
        
    return(req_1)
    
def print_test_req2(req2):
    """
    Imprime los resultados de las pruebas de rendimiento
    """
    print("Tiempo de ejecución para el requerimiento 2:",
          f"{req2:.3f}", "[ms]")

def print_req_2(control, departament):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    try:
        req_2 = logic.req_2(control,departament)
        req2_result = logic.measure_req_2(control,departament)
        if len(req_2["registro"]) == 0:
            print("No se encontraron registros.")
            print_test_req2(req2_result)  
        else:
            print("Numero total de registros: " + str(req_2["numero_registros"]))
            print("Último registro encontrado: ")        
            print("Año de recolección: "+ req_2["registro"]["year_collection"])
            print("Año de carga: "+ req_2["registro"]["load_time"])
            print("Tipo de origen: "+ req_2["registro"]["source"])
            print("Frecuencia de recolección: "+ req_2["registro"]["freq_collection"])
            print("Nombre del departamento: "+ req_2["registro"]["state_name"])
            print("Tipo de producto: "+ req_2["registro"]["commodity"])
            print("Unidad de medidad: "+ req_2["registro"]["unit_measurement"])
            print("Valor unitario del registro: "+ req_2["registro"]["value"])
            print_test_req2(req2_result)  
            

    except TypeError:
        print("Error: Por favor cargue los datos.")
    
    return(req_2)


def print_req_3(control_lt):
    department = input("Ingrese el nombre del departamento: ")
    año_inicio = input("Ingrese el año inicial del periodo: ")
    año_fin = input("Ingrese el año final del periodo: ")
    resultado, tiempo = logic.measure_req_3(control_lt, department, año_inicio, año_fin)
    if isinstance(resultado, str):
        print(resultado)
        return
    print(f"Tiempo de ejecución: {tiempo:.3f} ms")
    print(f"Número total de registros: {resultado['total_registros']}")
    print(f"Número de registros 'SURVEY': {resultado['survey_count']}")
    print(f"Número de registros 'CENSUS': {resultado['census_count']}")
    print("Listado de registros:")
    for registro in resultado["registros"]:
        print(registro)
        
        
# def print_test_req4(req4):
#     """
#     Imprime los resultados de las prueba de tiempo del requerimiento 4
#     """
#     print("Tiempo de ejecución para el requerimiento 4:",
#           f"{req4:.3f}", "[ms]")
    
# def print_req_4(control, commodity, low_yr, high_yr):
# 
#     """
#         Función que imprime la solución del requerimiento 4 en consola
#     """
#     req4 = logic.req_4(control, commodity, low_yr, high_yr)
    
#     while not st.is_empty(req4):
#         print(st.pop(req4))  
        
#     req4_result = logic.measure_req_4(control, commodity, low_yr, high_yr)
#     print_test_req4(req4_result)
        
#     return req4

def print_test_req4al(req4):
    """
    Imprime los resultados de las prueba de tiempo del requerimiento 4
    """
    print("Tiempo de ejecución para el requerimiento 4:",
          f"{req4:.3f}", "[ms]")
    

def print_req_4al(control, commodity, low_yr, high_yr):
   
    try:
        req4 = logic.req_4al(control, commodity, low_yr, high_yr)
        req4_result = logic.measure_req_4al(control,commodity, low_yr, high_yr)
        if req4 == False:
            print("No se encontraron registros asociados.")
            print_test_req4al(req4_result)
        else:
            print("Tipo de origen | Año de recolección | Fecha de carga | Frecuencia de recolección | Departamento | Unidad de medida | Producto")
            if req4[1] == False:   
                while not stal.is_empty(req4[0]):    
                    print(stal.pop(req4[0])) 
            else:         
                for i in req4[0]["elements"]:              
                    print(i)                                  
            print("Total de registros: " + str(req4[2])) 
            print("Total de registros con tipo de fuente/origen “CENSUS”: " + str(req4[3]))  
            print("Total de registros con tipo de fuente/origen “SURVEY”: " + str(req4[4]))             
            print_test_req4al(req4_result)
            
    except TypeError:
        print("Error: Ingrese una fecha válida.")
    
    return(req4)
  
def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass

def print_test_req6(req6):
    """
    Imprime los resultados de las prueba de tiempo del requerimiento 6
    """
    print("Tiempo de ejecución para el requerimiento 6:",
          f"{req6:.3f}", "[ms]")
    
def print_req_6(control, departament, initial_date, last_date):

    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    try:
        req6 = logic.req_6(control, departament, initial_date, last_date)
        req6_result = logic.measure_req_6(control,departament, initial_date, last_date)
        if req6 == None:
            print("No se encontraron registros asociados.")
            print_test_req6(req6_result)
            return(req6)
        else: 
            print("Tipo de origen | Año de recolección | Fecha de carga | Frecuencia de recolección | Departamento | Unidad de medida | Producto")      
            if req6[1] == False:
                while not stal.is_empty(req6[0]):
                
                    print(stal.pop(req6[0])) 
            else:
                for i in req6[0]["elements"]:              
                    print(i)     
                       
            print("Total de registros: " + str(req6[2])) 
            print("Total de registros con tipo de fuente/origen “CENSUS”: " + str(req6[3]))  
            print("Total de registros con tipo de fuente/origen “SURVEY”: " + str(req6[4]))      
            print_test_req6(req6_result)
            return(req6)
    except:
        print("Error: Por favor ingrese una fecha válida.")

def print_test_req7(req7):
    """
    Imprime los resultados de las prueba de tiempo del requerimiento 7
    """
    print("Tiempo de ejecución para el requerimiento 7:",
          f"{req7:.3f}", "[ms]")
        
def print_req_7(control, department, año_inicio, año_fin):

    req7 = logic.req_7(control, department, año_inicio, año_fin)
    req7_result = logic.measure_req_7(control, department, año_inicio, año_fin)

    print("Año de recopilación: "+ str(req7[0][0]))
    print("Indicación del periodo: "+ str(req7[0][1]))
    print("Valor de ingresos del periodo: "+ str(req7[0][2]))
    print("Número de registros validos: "+ str(req7[0][3]))
    print("Número de registros no validos: "+ str(req7[0][4]))
    print("Número de registros tipo SURVEY: "+ str(req7[0][5]))
    print("Número de registros tipo CENSUS: "+ str(req7[0][6]))
    
    print("\nAño de recopilación: "+ str(req7[1][0]))
    print("Indicación del periodo: "+ str(req7[1][1]))
    print("Valor de ingresos del periodo: "+ str(req7[1][2]))
    print("Número de registros validos: "+ str(req7[1][3]))
    print("Número de registros no validos: "+ str(req7[1][4]))
    print("Número de registros tipo SURVEY: "+ str(req7[1][5]))
    print("Número de registros tipo CENSUS: "+ str(req7[1][6]))
    print_test_req7(req7_result)
  
    return(req7)
    
    
    
def print_test_req8(req8):
    """
    Imprime los resultados de las prueba de tiempo del requerimiento 8
    """
    print("Tiempo de ejecución para el requerimiento 8:",
          f"{req8:.3f}", "[ms]")
    
def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """

    req8 = logic.req_8(control)
    try:
        print("Numero total de departamentos: " + str(req8[1]))
        print("Mayor año de carga: " + str(req8[2]))
        print("Menor año de carga: " + str(req8[3]))
        print("Años promedio de tiempos de carga: " + str(round(req8[4],2)) + " \n")
        
        print("Departamento con mayor diferencia promedio: ")
        print("Estado: "+ str(req8[0][0]))
        print("Promedio: "+ str(round(req8[0][1],2)))
        print("Año máximo de recolección: "+ str(req8[0][2]))
        print("Año mínimo de recolección: "+ str(req8[0][3]))
        print("Diferencia máxima calculada: "+ str(req8[0][4]))
        print("Diferencia mínima calculada: "+ str(req8[0][5]))
        print("Registros tipo Census: "+ str(req8[0][6]))
        print("Registros tipo Survey: "+ str(req8[0][7]))
        print("Registros del departamento: "+ str(req8[0][8]))
        
        req8_result = logic.measure_req_8(control)
        print_test_req8(req8_result)
    except IndexError:
        print("Error: Por favor cargue los datos.")
 
    return(req8)


# Se crea la lógica asociado a la vista
control = new_logic("sl")
control_lt = new_logic("al")

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()

        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            archivo = input("Ingrese el nombre del archivo que quiere cargar: ")
            load_data(archivo)
            data_size = agric_records_size(control)
            lry = less_data_yr(control)
            mry = most_data_yr(control)
        
            print('Registros cargados: ' + str(data_size))
            print("Año de menor recolección: ", str(lry))
            print("Año de mayor recolección: ", str(mry))
            
            tbr = top_5_registers(control_lt)
            print("Año de recolección | Fecha de carga | Departamento | Tipo de origen | | Unidad de medida | Valor unitario del registro")
            for i in tbr["elements"]:               
                print(i["year_collection"], i["load_time"], i["state_name"], i["source"], i["unit_measurement"], i["value"])
        
                    
        elif int(inputs) == 2:
            year = input('Ingrese un año: \n')
            print_req_1(control,year)

        elif int(inputs) == 3:
            departament = input('Ingrese un departamento: \n')
            print_req_2(control,departament)

        elif int(inputs) == 4:
            print_req_3(control_lt)

        elif int(inputs) == 5:
            commodity = input("Ingrese el tipo de producto: ")
            low_yr = input("Ingrese el año mínimo: ")
            high_yr = input("Ingrese el año máximo: ")
            print_req_4al(control_lt, commodity, low_yr, high_yr)
    
        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            departament = input("Ingrese el departamento: ")
            initial_date = input("Ingrese la fecha mínima: ")
            last_date = input("Ingrese la fecha máxima: ")
            print_req_6(control_lt, departament, initial_date, last_date)



        elif int(inputs) == 8:
            department = input("Ingrese el nombre del departamento: ")
            año_inicio = input("Ingrese el año inicial del periodo: ")
            año_fin = input("Ingrese el año final del periodo: ")
            print_req_7(control, department, año_inicio, año_fin)
            
            

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")

    sys.exit(0)