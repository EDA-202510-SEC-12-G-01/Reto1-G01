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

def load_data():
    """
    Carga los datos en ambas estructuras de datos
    """
    logic.load_data(control, "sl")  

    logic.load_data(control_lt, "al")  
    
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


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

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
    req_1 = logic.req_1(control,year)

    print("Numero total de registros: " + str(req_1["numero_registros"]))
    print("Último registro encontrado: ")
    print(req_1["registro"]["year_collection"], req_1["registro"]["load_time"], req_1["registro"]["source"], 
          req_1["registro"]["freq_collection"], req_1["registro"]["state_name"], req_1["registro"]["commodity"],
          req_1["registro"]["unit_measurement"], req_1["registro"]["value"])

    req1_result = logic.measure_req_1(control,year)
    print_test_req1(req1_result)
    
    return (req_1)

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


# def print_test_req4(req4):
#     """
#     Imprime los resultados de las prueba de tiempo del requerimiento 4
#     """
#     print("Tiempo de ejecución para el requerimiento 4:",
#           f"{req4:.3f}", "[ms]")
    
# def print_req_4(control, commodity, low_yr, high_yr):
#     # TODO: Imprimir el resultado del requerimiento 4
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
    req4 = logic.req_4al(control, commodity, low_yr, high_yr)

    if req4[1] == False:
        while not stal.is_empty(req4[0]):
            print(stal.pop(req4[0])) 
    else:
        for i in req4[0]["elements"]:              
            print(i)      
               
    req4_result = logic.measure_req_4al(control,commodity, low_yr, high_yr)
    print("Total de registros: " + str(req4[2])) 
    print("Total de registros con tipo de fuente/origen “CENSUS”: " + str(req4[3]))  
    print("Total de registros con tipo de fuente/origen “SURVEY”: " + str(req4[4])) 
       
    print_test_req4al(req4_result)
    pass

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


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
            load_data()
            data_size = agric_records_size(control)
            lry = less_data_yr(control)
            mry = most_data_yr(control)
        
            print('Registros cargados: ' + str(data_size))
            print("Año de menor recolección: ", str(lry))
            print("Año de mayor recolección: ", str(mry))
            
            tbr = top_5_registers(control_lt)
            for i in tbr["elements"]:               
                print(i["year_collection"], i["load_time"], i["state_name"], i["source"], i["unit_measurement"], i["value"])
           
                      
        elif int(inputs) == 2:
            year = input('Ingrese un año: \n')
            print_req_1(control,year)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:

            print_req_3(control)

        elif int(inputs) == 5:
            commodity = input("Ingrese el tipo de producto: ")
            low_yr = input("Ingrese el año mínimo: ")
            high_yr = input("Ingrese el año máximo: ")
            print(print_req_4al(control_lt, commodity, low_yr, high_yr))
     
        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
