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
    if (lst["size"] == 0):
        return None
    a = lst["first"]["info"]
    if lst["size"] == 1:
        lst["first"]=None
        lst["last"]=None
        lst["size"]-=1
        return a
    else:
        node=lst["first"]
        searchpos=0
        while searchpos-1<lst["size"]:
            node = node["next"]
            searchpos += 1
        node["next"]=None
        lst["last"]=None
        return a
def delete_element(lst, pos):

    if (lst["size"] == 0):
        lst["first"]=None
        lst["last"]=None
    
    
    if lst["size"] == 1:
        a = lst["first"]["info"]
        lst["first"]=None
        lst["last"]=None
        lst["size"]-=1
    
    
    elif pos==0:
        lst["first"]=lst["first"]["next"]
        lst["size"]-=1
        
    elif pos==lst["size"]:
        node=lst["first"]
        searchpos=0
        while searchpos-1<lst["size"]:
            node = node["next"]
            searchpos += 1
        node["next"]=None
        lst["last"]=None
        
    else:
        node=lst["first"]
        searchpos=0
        
        while searchpos-1<pos:
            node = node["next"]
            searchpos += 1
        node["next"]=node["next"]["next"]
        
    if lst["size"] == 1:
        lst["last"]=lst["first"]
    return lst

def change_info(lst, pos, new_info):
    node=lst["first"]
    searchpos=0
    while searchpos<pos:
        node = node["next"]
        searchpos += 1
    NN = {"info": new_info, "next":node["next"] }
    return lst




def exchange(lst, pos_1, pos_2):
    node1=lst["first"]
    searchpos=0
    while searchpos<pos_1:
        node1 = node1["next"]
        searchpos += 1
    node2=lst["first"]
    searchpos=0
    while searchpos<pos_2:
        node2 = node2["next"]
        searchpos += 1
    a=node2
    node2=node1
    node1=a
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