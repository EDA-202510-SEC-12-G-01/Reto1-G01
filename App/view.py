import sys
import App.logic as logic
sys.setrecursionlimit(10000)  # Ajustar límite de recursión si es necesario



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

def print_req_1(control,year):
    # TODO: Imprimir el resultado del requerimiento 1
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    req_1 = logic.req_1(control,year)
    return req_1

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


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
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
            for i in tbr:
                print(i,tbr[i]["year_collection"], tbr[i]["load_time"], tbr[i]["location"],tbr[i]["source"],tbr[i]["unit_measurement"],tbr[i]["value"])
            
            
        elif int(inputs) == 2:
            year = input('Ingrese un año\n')
            print(print_req_1(control,year))

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

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
