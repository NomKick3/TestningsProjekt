import random
import sys

def random_number_generator(arg): 
    number = random.randint(10**arg,10**arg+1)/random.randint(arg+1**26,arg+1**27)
    return number
def random_string_generator(arg):
    string = ""
    for _ in range(random.randint(0,1000)):
            string.join(random.choice("1234567890!#¤%&/()=?`@£$€{[]}`^*¨'~qwertyuiopåasdfghjklöäzxcvbnmQWERTYUIOPÅASDFGHJKLÖÄZXCVBNM,;.:-_><|§½\n\t\r'*+?"))
    return string
def random_structure_generator(arg):
    global highest_depth
    if arg > highest_depth: highest_depth = arg
    if arg >= 10:
        another_one = "END"
    else:
        for i in range(0,3):
            another_one = {str(arg+i): functions[random.randint(0,len(functions)-1)](arg+1)}
    return another_one

def cykled_lst(arg, lst=[],num=10,first = []): #random.randint(0, 1000)
    # if arg == num:
    #     lst.append(arg)
    # else:
    #     lst.append(arg)
    #     lst.append([])
    #     cykled_lst(arg+1, lst[1], num, first)
    #     return lst

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
    

def cykled_dict(arg, dic={}, num=random.randint(0, 10)):
    if arg == num:
        dic[arg] = 0
        return dic
    else:
        dic[arg] = {}
        cykled_dict(arg+1, dic[arg], num)
        return dic
    
functions = [cykled_lst] # random_string_generator, random_structure_generator,

def random_data_generator():
    global highest_depth
    highest_depth = 0
    sys.setrecursionlimit(1000000)
    index = 0
    y_dict = {}
    while True:
        j = random.randint(0,len(functions)-1)
        # print(j)
        y_dict[str(index)] = functions[j](0)
        # print("hora")
        index += 1
        # print(highest_depth)
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

def check_equal(list1,list2):
    if len(list1) != len(list2): return False
    if list1[0] != list2[0]: return False
    t1_list, t2_list = list1[1], list2[1]
    while t1_list[0] != 0:
        print(t1_list[0])
        if t1_list[0] != t2_list[0]: return False
        t1_list, t2_list = t1_list[1], t2_list[1]

    return True

list = cykled_lst(0)

if check_equal(list,list):
    print("Amanda är kass")
else:
    print("Amanda är fortfarande kass")