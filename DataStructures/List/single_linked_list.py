def new_list ():
    new_list = {
        "first": None,
        "last": None,
        "size": 0
    }
    
    return new_list

def get_element (my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present (my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"] == 0):
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(lst, val):
    NN = {"info": val, "next": lst["first"]}  
    lst["first"] = NN  
    if lst["size"] == 0:
        lst["last"] = NN  
    lst["size"] += 1  

    return lst

def add_last (lst, val):
    NN = {"info": val, "next": None}
    if (lst["size"] == 0):
        lst["first"] = NN
        lst["last"] = NN
    else:
        lst["last"]["next"] = NN
        lst["last"] = NN
    lst["size"] += 1
    return lst

def size (lst):
    a = lst["size"]
    return a

def first_element(lst):
    if (lst["size"] == 0):
        return None
    else:
        a = lst["first"]["info"]
        return a

def is_empty(lst):
    if lst['size']==0:
        return True
    else:
        return False
        
def last_element(lst):
    if (lst["size"] == 0):
        return None
    else:
        a = lst["last"]["info"]
        return a
    
def remove_first(lst):
    
    if (lst["size"] == 0):
        return None
    a = lst["first"]["info"]
    if lst["size"] == 1:
        lst["first"]=None
        lst["last"]=None
        lst["size"]-=1
        return a
    else:
        lst["first"]=lst["first"]["next"]
        lst["size"]-=1
    if lst["size"] == 1:
        lst["last"]=lst["first"]
        
    
    return a

def insert_element(lst,val,pos):
    NN = {"info": val, "next": None}
    if (lst["size"] == 0):
        lst["first"] = NN
        lst["last"] = NN
        return lst
    elif pos==0:
        NN["next"]=lst["first"]
        lst["first"] = NN
        lst["size"] += 1  
        return lst
    elif pos==lst["size"]-1:
        lst["last"]["next"] = NN
        lst["last"] = NN
        lst["size"] += 1
        return lst
    searchpos = 0
    node = lst["first"]
    while searchpos-1 < pos:
        node = node["next"]
        searchpos += 1
    NN["next"]=node["next"]
    node["next"]=NN
    return lst

def remove_last(lst):
    if lst["size"] == 0:
        return None
    if lst["size"] == 1:
        a = lst["first"]["info"]
        lst["first"] = None
        lst["last"] = None
        lst["size"] -= 1
        return a

    node = lst["first"]
    while node["next"] != lst["last"]:
        node = node["next"]

    a = lst["last"]["info"]
    node["next"] = None
    lst["last"] = node
    lst["size"] -= 1
    return a

def delete_element(lst, pos):
    if lst["size"] == 0 or pos < 0 or pos >= lst["size"]:
        return None  

    if pos == 0:  
        lst["first"] = lst["first"]["next"]
        if lst["size"] == 1:
            lst["last"] = None
        lst["size"] -= 1
        return lst

    prev_node = None
    current_node = lst["first"]
    for _ in range(pos):
        prev_node = current_node
        current_node = current_node["next"]

    prev_node["next"] = current_node["next"]  

    if current_node == lst["last"]: 
        lst["last"] = prev_node

    lst["size"] -= 1
    return lst

def change_info(lst, pos, new_info):
    node = lst["first"]
    for _ in range(pos):
        node = node["next"]
    node["info"] = new_info
    return lst

def exchange(lst, pos_1, pos_2):
    if pos_1 == pos_2:
        return lst
    
    node1 = lst["first"]
    node2 = lst["first"]
    for _ in range(pos_1):
        node1 = node1["next"]
    for _ in range(pos_2):
        node2 = node2["next"]

    node1["info"], node2["info"] = node2["info"], node1["info"]
    return lst


def sub_list(lst, pos, num_elements):
    node=lst["first"]
    searchpos=0
    while searchpos<pos:
        node = node["next"]
        searchpos += 1
    new_list = {
        "first": node,
        "last": None,
        "size": num_elements
    }
    node=new_list["first"]
    searchpos=0
    while searchpos<num_elements:
        node = node["next"]
        searchpos += 1
    new_list["last"]=node
    return new_list