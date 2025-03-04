def new_list ():
    new_list = {
        "elements": [],
        "size": 0
    }
    
    return new_list

def get_element(my_list, index):
    
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range (0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(list, val):
    
    list["elements"].insert(0, val)
    list["size"] += 1
    return list

def add_last (list, val):
    list["elements"].append(val)
    list["size"] += 1
    return list

def size (list):
    
    a = list["size"]
    return a

def first_element(list):
    
    if (list["size"] == 0):
        return None
    else:
        
        a = list["elements"][0]
        return a

def last_element(lst):
    
    if (lst["size"] == 0):
        return None
    
    else:
        
        s = lst["size"] - 1
        a = lst["elements"][s]
        return a

def is_empty(list):
    if list["size"] == 0:
        return True
    else:
        return False

def remove_first(lst):
    if (lst["size"] == 0):
        return None
    else:
        a = lst["elements"].pop(0)
        lst["size"] -= 1
        return a

def remove_last(lst):
    if (lst["size"] == 0):
        return None
    else:
        s = lst["size"] - 1
        a = lst["elements"].pop(s)
        lst["size"] -= 1
        return a
    
def insert_element(lst, element, pos):
 
    if pos < 0 or pos > lst["size"]:  
        return None  

    lst["elements"].insert(pos, element)  
    lst["size"] += 1  
    return lst

def delete_element(lst, pos):
    if lst["size"] == 0 or pos < 0 or pos >= lst["size"]:
        return None  
    
    lst["elements"].pop(pos)
    lst["size"] -= 1
    return lst

def change_info(lst, pos, valor):
    
    if (pos >= lst["size"] or pos < 0):
        return None
    elif (lst["size"] == 0):
        return None
    else:
        lst["elements"][pos] = valor
        return lst

def exchange(lst, pos1, pos2):
    if pos1 < 0 or pos2 < 0 or pos1 >= lst["size"] or pos2 >= lst["size"]:
        return None  
    if pos1 == pos2:
        return lst  

    lst["elements"][pos1], lst["elements"][pos2] = lst["elements"][pos2], lst["elements"][pos1]  # Swap con tupla
    return lst

def sub_list(lst, pos1, pos2):
    
    if(pos2 < pos1):
        return None
    elif (pos1 >= lst["size"] or pos1 < 0):
        return None
    elif (pos2 >= lst["size"] or pos2 < 0):
        return None
    elif (lst["size"] == 0):
        return None
    else:
        nueva_lista = []
        for i in range (pos1, pos2+1):
            
            nueva_lista.append(lst["elements"][i])
        s = 0
        for i in range (0, len(nueva_lista)):
            s += 1
            
        nueva_lista = {"size": s, "elements": nueva_lista} 
        return nueva_lista