from math import fabs
from math import isclose
from math import trunc
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
inc = []
dif = 1
string = []
equality = []
number_equa = input("nombre d'equations: ")
for i in range(int(number_equa)):
    string.append(input("equ : "))
    string[i] = string[i].split(" ")

def analyse(string):
    global inc
    global equality
    part1 = ""
    part2 = ""
    for a in range(len(string)):
        for i in range(len(string[a])):
            close = 0
            e = 0
            #print(string[i])
            try:
                float(string[a][i])
            except:
                while close == 0 and e < 26:
                    test = 0
                    if string[a][i] == alph[e]:
                        for a in range(len(inc)):
                            if inc[a][0] == string[a][i]:
                                test = 1
                        if test == 0:
                            array = [alph[e],0]
                            inc.append(array)
                            close = 1
                    e = e + 1
                if string[a][i] == "=":
                    for e in range(i):
                        part1 = part1 + " " + string[a][e]
                    part1 = part1.strip()
                    for e in range(len(string) - i - 1):
                        part2 = part2 + " " + string[a][e + i + 1]
                    part2 = part2.strip()
        equality.append(part1 + " = " + part2)

def calc(part1):
    part1_array = part1.strip().split(" ")
    #print(part1_array)
    i = 0
    while i < len(part1_array):
        if part1_array[i] == "/":
            result = float(part1_array[i - 1]) / float(part1_array[i + 1])
            part1_array.pop(i - 1)
            part1_array.pop(i - 1)
            part1_array[i - 1] = result
            i = i - 2
        i = i + 1
    i = 0
    while i < len(part1_array):
        if part1_array[i] == "*":
            result = float(part1_array[i - 1]) * float(part1_array[i + 1])
            part1_array.pop(i - 1)
            part1_array.pop(i - 1)
            part1_array[i - 1] = result
            i = i - 2
        i = i + 1
    i = 0
    while i < len(part1_array):
        if part1_array[i] == "+":
            result = float(part1_array[i - 1]) + float(part1_array[i + 1])
            part1_array.pop(i - 1)
            part1_array.pop(i - 1)
            part1_array[i - 1] = result
            i = i - 2
        elif part1_array[i] == "-":
            result = float(part1_array[i - 1]) - float(part1_array[i + 1])
            part1_array.pop(i - 1)
            part1_array.pop(i - 1)
            part1_array[i - 1] = result
            i = i - 2
        i = i + 1
    return part1_array[0]

def calc_par(part1):
    part1_e = part1
    #print(part1_e + " PART1_E")
    part1_array = part1_e.strip().split(" ")
    i = len(part1_array) - 1
    while i != 0:
        if part1_array[i] == "(":
            test = 0
            f = i
            while test != 1:
                if part1_array[f] == ")":
                    test = 1
                    par_value = ""
                    for a in range(f - i + 1):
                        if a != f - i:
                            par_value = par_value + part1_array[a + i] + " "
                        else:
                            par_value = par_value + part1_array[a + i]
                    result = calc(par_value[2:len(par_value) - 1])
                    for a in range(f - i):
                        part1_array.pop(i)
                        part1_array[i] = str(result)
                f = f + 1           
        i = i - 1
    no_par_value = ""
    for a in range(len(part1_array)):
        if a != len(part1_array) - 1:
            no_par_value = no_par_value + part1_array[a] + " "
        else:
            no_par_value = no_par_value + part1_array[a]
    result = calc(no_par_value)
    #print(str(result) + " finish")
    return result

def set_int(inc,arg_dif,part):
    returned = []
    for e in range(7**(len(inc))):
        for a in range(len(equality)):
            returned.append([])
            calc_int = part[a]
            repartition = base7(e,len(inc))
            for i in range(len(inc)):
                if repartition[i:i + 1] == "0":
                    new_value = float(inc[i][1]) 
                elif repartition[i:i + 1] == "1":
                    new_value = float(inc[i][1]) + float(arg_dif)
                elif repartition[i:i + 1] == "2":
                    new_value = float(inc[i][1]) + (float(arg_dif) * 10)
                elif repartition[i:i + 1] == "3":
                    new_value = float(inc[i][1]) - float(arg_dif)
                elif repartition[i:i + 1] == "4":
                    new_value = float(inc[i][1]) - (float(arg_dif) * 10)
                elif repartition[i:i + 1] == "5":
                    new_value = float(inc[i][1]) - (float(arg_dif) * 0.1)
                elif repartition[i:i + 1] == "6":
                    new_value = float(inc[i][1]) + (float(arg_dif) *0.1)
                calc_int = calc_int.replace(inc[i][0],str(new_value))
            returned[a].append(calc_int)
    #print(returned)
    return returned



def base7(num,len_inc):
    number = num
    num_b7 = 0
    while number != 0:
        a = 0
        while 7**a <= number:
            a = a + 1
        a = a - 1
        n = 1
        while n*(7**a) <= number:
            n = n + 1
        n = n - 1
        number = number - (n*(7**a))
        num_b7 = num_b7 + n * (10**a)
    str_num_b7 = str(num_b7)
    if len(str_num_b7) < len_inc:
        for i in range(len_inc - (len(str_num_b7))):
            str_num_b7 = "0" + str_num_b7
    return str_num_b7


def min(array):
    min_value = 0
    add_array = []
    for i in range(array[0]):
        add_array.append(array[0][i] + array[1][i])
    for i in range(len(array) - 1):
        if add_array[i + 1] < add_array[min_value]:
            min_value = i + 1
    return min_value


def compare(inc,equality):
    global dif
    possible_v = set_int(inc,dif,equality)
    result = []
    dif_result = []
    returned = []
    #print(str(possible_v) + " Possible_v")
    for a in range(len(equality)):
        result.append([])
        dif_result.append([])
        for i in range(len(possible_v[a])):
            possible_v[a][i] = possible_v[a][i].split(" = ")
            result[a].append([0,0])
            result[a][i][0] = float(calc_par(possible_v[a][i][0]))
            result[a][i][1] = float(calc_par(possible_v[a][i][1]))
            #print(result)
    for i in range(len(possible_v[0])):
        test = 0
        for a in range(len(equality)):
            if isclose(result[a][i][0],result[a][i][1]):
                test = 1
            else:
                test = 0
        if test == 1:  
            for a in range(len(equality)):
                returned.append(possible_v[a][i])
            returned.append("equal")
            #print("coucou")
            #print(returned)
            return returned
        else:
            for a in range(len(equality)):
                dif_result[a].append(fabs(result[a][i][0] - result[a][i][1]))
    index = min(dif_result)
    if index == 0:
        dif = dif / 2
    #print(str(dif) + " DIF")
    string_min_value = []
    for a in range(len(equality)):
        string_min_value.append(possible_v[a][index])
    #print(string_min_value)
    #print(dif)
    #print(result)
    return string_min_value

def new_inc(string_min_value,inc,part):
    array_part = part.split(" ")
    for i in range(len(array_part)):
        if array_part[i] == "=":
            part1_a = ""
            for e in range(i):
                part1_a = part1_a + " " + array_part[e]
            part1_a = part1_a.strip()
            part2_a = ""
            for e in range(len(array_part) - i):
                part2_a = part2_a + " " + array_part[e]
            part2_a = part2_a.strip()
    string_min_value_a1 = string_min_value[0].split(" ")
    string_min_value_a2 = string_min_value[1].split(" ")
    #print("TEST")
    #print(part1_a)
    #print(string_min_value)
    for i in range(len(inc)):
        for e in range(len(part1_a)):
            if inc[i][0] == part1_a[e]:
                inc[i][1] = float(string_min_value_a1[e])
        for e in range(len(part2_a)):
            if inc[i][0] == part2_a[e]:
                inc[i][1] = float(string_min_value_a2[e])   
    #print(inc)
    return inc

analyse(string)
test = 0
while test == 0:
    string_min_value = compare(inc,equality)
    #print("BELLOW")
    #print(string_min_value)
    if len(string_min_value) == len(equality) + 1:
        test = 1
        for a in range(len(equality)):
            inc = new_inc(string_min_value[a],inc,equality[a])
        for i in range(len(inc)):
            prep_inc = inc[i][1]
            prep_inc = trunc(100000000*prep_inc)/100000000
            print(inc[i][0] + " = " + str(prep_inc))
    else:
        for a in range(len(equality)):
            inc = new_inc(string_min_value[a],inc,equality[a]) 


