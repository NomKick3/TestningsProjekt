import random
import sys

def random_number_generator(arg): 
    number = random.randint(1,1000)/random.randint(1,10000)
    return number

def random_string_generator(arg):
    string = ""
    for _ in range(random.randint(0,1000)):
            string.join(random.choice("1234567890!#¤%&/()=?`@£$€{[]}`^*¨'~qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,;.:-_><|§½\n\t\r'*+?"))
    return string

def random_list_generator(arg):
    global highest_depth
    if arg > highest_depth: highest_depth = arg
    if arg >= 10:
        lst = "END"
    else:
        lst = []
        for _ in range(random.randint(0,5)):
            lst.append(functions[random.randint(0,len(functions)-1)](arg+1))
    return lst

def random_structure_generator(arg):
    global highest_depth
    if arg > highest_depth: highest_depth = arg
    if arg >= 10:
        another_one = "END"
    else:
        for i in range(0,3):
            another_one = {str(arg+i): functions[random.randint(0,len(functions)-1)](arg+1)}
    return another_one

def cykled_lst(arg, lst=[],num=random.randint(0, 1000)):
    t1_list = lst
    t1_list.append(0)
    t1_list.append([])
    for i in range(1,num):
        t1_list = t1_list[1]
        t1_list.append(i)
        t1_list.append([])
    t1_list.pop()
    t1_list.append(lst)
    return lst
    
def cykled_dict(arg, dic={}, num=random.randint(1, 1000)):
    t1_dict = dic
    t1_dict[0] = {}
    for i in range(1,num):
        t1_dict = t1_dict[i-1]
        t1_dict[i] = {}
    t1_dict = t1_dict[num-1]
    t1_dict[num] = dic
    return dic

    
functions = [random_string_generator, random_structure_generator, random_number_generator, random_list_generator] 

def random_data_generator():
    global highest_depth
    highest_depth = 0
    sys.setrecursionlimit(1000000)
    index = 0
    y_dict = {}
    while True:
        j = random.randint(0,len(functions)-1)
        y_dict[str(index)] = functions[j](0)
        index += 1
        yield y_dict

def random_number():
    while True:
        lower_limit = 0
        upper_limit = 100
        multiplier = 1
        while True:
            
            if upper_limit < lower_limit:
                upper_limit,lower_limit = lower_limit,upper_limit
            n1 = random.randint(lower_limit, upper_limit)
            n2 = random.randint(lower_limit*multiplier, upper_limit*multiplier)
            lower_limit += 1000
            upper_limit += 1000
            multiplier += random.randint(lower_limit,upper_limit)
            yield n1/n2

def check_equal_list(list1,list2):
    if len(list1) != len(list2): return False
    if list1[0] != list2[0]: return False
    t1_list, t2_list = list1[1], list2[1]
    while t1_list[0] != 0:
        if t1_list[0] != t2_list[0]: return False
        t1_list, t2_list = t1_list[1], t2_list[1]
    return True

def check_equal_dict(dict1, dict2,depth = 0):
    # if depth > 100:
    #     return True

    if not (type(dict1) == dict) or not (type(dict2) == dict):
        return False

    if set(dict1.keys()) != set(dict2.keys()):
        return False
    
    # for k in dict1:  # Iterate through keys in dict1
    #     if (type(dict1[k]) ==  dict) and (type(dict2[k]) == dict):# If the value is another dictionary, recursively compare dictionaries 
    #         depth += 1
    #         if not check_equal_dict(dict1[k], dict2[k],depth):
    #             return False  # If the recursive check fails, return False
    #     elif type(dict1[k]) != type(dict2[k]) or dict1[k] != dict2[k]: # If the types of values are different or the values are not equal
    #         return False
        
    key = int(list(dict1.keys())[0])
    t1_dict, t2_dict = dict1[key], dict2[key]
    while int(list(t1_dict.keys())[0]) != 0:
        if set(t1_dict.keys()) != set(t2_dict.keys()): return False
        key = int(list(t1_dict.keys())[0])
        t1_dict, t2_dict = t1_dict[key], t2_dict[key]
    return True
    # return True


if __name__ == "__main__":
    global highest_depth
    highest_depth = 0
    cykle = cykled_dict(0)
    cykle2 = cykled_dict(0)
    print(check_equal_dict(cykle,cykle2))
