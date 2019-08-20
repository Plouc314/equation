from math import fabs
from math import isclose
from math import trunc
from time import process_time
from math import sqrt
from math import pow
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
inc = []
dif = []
string = []
equality = []
final_inc_values_work = []
min_provi = 0
total_tested_value = 0
multi_final_inc_value = 0
number_calc_depart_values = 0
input_start_values = input("valeurs de depart (9): ")
inc_starts_values = input_start_values.strip().split(" ")
if len(inc_starts_values) != 9:
    inc_starts_values = [-10,-5,-1,-0.5,0,0.5,1,5,10]
for i in range(len(inc_starts_values)):
    inc_starts_values[i] = float(inc_starts_values[i])
number_try_start = 0
index_zero_int = 0
index_zero_array = []
pas_touche_dif = []
failed_final_inc = []
number_equa = input("nombre d'equations: ")
for i in range(int(number_equa)):
    string.append(input("equation: "))
    string[i] = string[i].split(" ")

def analyse(string):
    global inc
    global equality
    global index_zero_array
    global dif
    global pas_touche_dif
    global failed_final_inc
    global multi_final_inc_value
    global final_inc_values_work
    for a in range(len(string)):
        part1 = ""
        part2 = ""
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
                        for u in range(len(inc)):
                            if inc[u][0] == string[a][i]:
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
                    for e in range(len(string[a]) - i - 1):
                        part2 = part2 + " " + string[a][e + i + 1]
                    part2 = part2.strip()
        equality.append(part1 + " = " + part2)
    for i in range(len(inc)):
        failed_final_inc.append([])
    input_multi = input("chercher le plus de valeurs possibles (oui/non): ")
    if input_multi == 'oui':
        multi_final_inc_value = 1
    else:
        multi_final_inc_value = 0
    #print(equality)
    for i in range(len(inc)):
        index_zero_array.append(0)
        dif.append(float(input("dif de " + inc[i][0] + " : ").strip()))
        final_inc_values_work.append([])
    for i in range(len(dif)):
        pas_touche_dif.append(dif[i])
    #inc = [['x',0.3],['y',3],['z',-3]]
    
def calc(part1):
    part1_array = part1.strip().split(" ")
    #print(part1_array)
    i = 0
    while i < len(part1_array):
        if part1_array[i] == "~":
            try:
                result = sqrt(float(part1_array[i - 1]))
            except:
                return "division error"
            part1_array.pop(i - 1)
            part1_array.pop(i - 1)
            part1_array[i - 1] = result
            i = i - 2
        i = i + 1
    i = 0
    while i < len(part1_array):
        if part1_array[i] == "**":
            result = pow(float(part1_array[i - 1]),float(part1_array[i + 1]))
            result = trunc_needed(result)
            part1_array.pop(i - 1)
            part1_array.pop(i - 1)
            part1_array[i - 1] = result
            i = i - 2
        i = i + 1
    i = 0
    while i < len(part1_array):
        if part1_array[i] == "/":
            try:
                result = float(part1_array[i - 1]) / float(part1_array[i + 1])
            except:
                return "division error"
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
    while i != -1:
        #print(str(part1_array[i]) + " part1_array[i]")
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
                    if result == "division error":
                        return "division error"
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
    #print(str(no_par_value) + " no_par_value")
    result = calc(no_par_value)
    #print(str(result) + " finish")
    return result

def set_int(inc,array_dif,part):
    #print(array_dif)
    #print(inc)
    returned = []
    for i in range(len(equality)):
        returned.append([])
    for e in range(7**(len(inc))):
        for a in range(len(equality)):
            calc_int = part[a]
            repartition = base_n(e,len(inc),7)
            for i in range(len(inc)):
                arg_dif = array_dif[i]
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
                #elif repartition[i:i + 1] == "7":
                #    new_value = float(inc[i][1]) + (float(arg_dif) *0.3)
                #elif repartition[i:i + 1] == "8":
                #    new_value = float(inc[i][1]) - (float(arg_dif) *0.3)               
                calc_int = calc_int.replace(inc[i][0],str(trunc_needed(new_value)))
            returned[a].append(calc_int)
    #print(returned)
    return returned



def base_n(num,len_inc,base):
    number = num
    num_b = 0
    while number != 0:
        a = 0
        while base**a <= number:
            a = a + 1
        a = a - 1
        n = 1
        while n*(base**a) <= number:
            n = n + 1
        n = n - 1
        number = number - (n*(base**a))
        num_b = num_b + n * (10**a)
    str_num_b = str(num_b)
    if len(str_num_b) < len_inc:
        for i in range(len_inc - (len(str_num_b))):
            str_num_b = "0" + str_num_b
    return str_num_b


def min(array):
    global number_try_start
    min_value = 0
    add_array = []
    #print(str(array) + " array")
    for i in range(len(array[0])):
        inter_value = 0
        test = 0
        for a in range(len(array)):
            if array[a][i] != "division error":
                test = test + 1
        if test == len(array):
            #print(test)
            for a in range(len(array)):
                inter_value = inter_value + array[a][i]
            add_array.append(inter_value)
        else:
            add_array.append(100)
    #print(add_array)
    for i in range(len(add_array) - 1):
        if add_array[i + 1] < add_array[min_value]:
            min_value = i + 1
    #print(str(add_array[min_value]) + " min")
    #print(str(min_value) + " min_value")
    return min_value


def compare(equality):
    global dif
    global inc_starts_values
    global inc
    global number_try_start
    global index_zero_int
    global index_zero_array
    global failed_final_inc
    global total_tested_value
    global number_calc_depart_values
    possible_v = set_int(inc,dif,equality)
    result = []
    dif_result = []
    returned = []
    #print(str(possible_v) + " Possible_v")
    #print(str(possible_v[1][34]) + " Possible_v1")
    #print(str(possible_v[2][34]) + " Possible_v2")
    for a in range(len(equality)):
        result.append([])
        dif_result.append([])
        for i in range(len(possible_v[a])):
            possible_v[a][i] = possible_v[a][i].split(" = ")
            result[a].append([0,0])
            try:
                result[a][i][0] = float(calc_par(possible_v[a][i][0]))
                result[a][i][1] = float(calc_par(possible_v[a][i][1]))
            except:
                result[a][i][0] = "division error"
                result[a][i][1] = "division error"
        #print(str(result) + " RESULT")
    for i in range(len(possible_v[0])):
        test = 0
        error = 0
        for a in range(len(equality)):
            if result[a][i][0] != "division error" and result[a][i][1] != "division error":
                #print(str(result[a][i][0]) + " RESULT1")
                #print(str(result[a][i][1]) + " RESULT2")
                if isclose(result[a][i][0],result[a][i][1],rel_tol=1e-05):
                    test = test + 1
            else:
                error = 1
        if test == len(equality): 
            #print("EQUAL") 
            for a in range(len(equality)):
                returned.append(possible_v[a][i])
            returned.append("equal")
            #print("coucou")
            #print(returned)
            return returned
        else:
            for a in range(len(equality)):
                if error == 0:
                    dif_result[a].append(fabs(result[a][i][0] - result[a][i][1]))
                else:
                    dif_result[a].append("division error")
    #print(str(len(dif_result)) + " LENGHT")
    index = min(dif_result)
    #for i in range (len(inc)):
    #    if base_n(index,len(inc),9)[i:i + 1] == '0':
    #        dif[i] = dif[i] / 2
    #print(str(index) + " INDEX")
    
    if index == 0:
        #print("ZERO")
        #print(inc)
        #print(index_zero_int)
        new_values_needed = 0
        test = 0
        for i in range(len(inc)):
            test_inc = 0
            for e in range(len(failed_final_inc[i])):
                if isclose(inc[i][1],failed_final_inc[i][e],rel_tol=1e-3):
                    test_inc = 1
            test = test + test_inc
        if test == len(inc):
            #print("same_final_value")
            new_values_needed = 1
        test = 0
        for i in range(len(inc)):
            if index_zero_array[i] == len(str(inc[i][1])):
                test = test + 1
        if test == len(inc):
            index_zero_int = index_zero_int + 1
        else:
            index_zero_int = 0
        if index_zero_int == 7:
            index_zero_int = 0
            new_values_needed = 1
        index_zero_array = []
        for i in range(len(inc)):
            index_zero_array.append(len(str(inc[i][1])))
        for i in range(len(inc)):
            test0 = 0
            test9 = 0
            for e in range(len(str(inc[i][1]))):
                if str(inc[i][1])[e:e + 1] == '.':
                    point_place = e
                    for e in range(len(str(inc[i][1]))):
                        if str(inc[i][1])[e:e + 1] == '0':
                            test0 = test0 + 1
                        else:
                            test0 = 0
                        if str(inc[i][1])[e:e + 1] == '9':
                            test9 = test9 + 1
                        else:
                            test9 = 0
                        if test0 == 3 or test9 == 3:
                            new_values_needed = 1
        if new_values_needed == 1:
            #print(str(inc) + " OLD INC")
            test = 0
            for e in range(len(failed_final_inc[i])):
                if inc[i][1] == failed_final_inc[i][e]:
                    test = 1
            if test == 0:
                for i in range(len(inc)):
                    failed_final_inc[i].append(inc[i][1])
            #print(str(failed_final_inc)+ " failed_final_inc")
            if number_try_start < 9**len(inc):
                return set_when_new_value_needed(inc,inc_starts_values,equality)
            else:
                calc_start_values()
                number_calc_depart_values = number_calc_depart_values + 1
                print("Nouvelles valeurs de départs...")
                total_tested_value = total_tested_value + number_try_start
                number_try_start = 0
                return set_when_new_value_needed(inc,inc_starts_values,equality)
        else:
            for i in range(len(inc)):
                dif[i] = dif[i] / 2
        
    #print(str(dif_result) + " DIF")
    string_min_value = []
    for a in range(len(equality)):
        string_min_value.append(possible_v[a][index])
    #print(string_min_value)
    #print(dif)
    #print(result)
    return string_min_value

def trunc_needed(number):
    trunc_needed0 = 0
    trunc_needed9 = 0
    test0 = 0
    test9 = 0
    for i in range(len(str(number))):
        if str(number)[i:i + 1] == '.':
            for e in range(len(str(number))):
                point_place = 1
                if str(number)[e:e + 1] == '0':
                    test0 = test0 + 1
                else:
                    test0 = 0
                if str(number)[e:e + 1] == '9':
                    test9 = test9 + 1
                else:
                    test9 = 0
                if test0 == 5:
                    trunc_needed0 = 1
                    start_trunc = e
                elif test9 == 5:
                    trunc_needed9 = 1
                    start_trunc = e
    if trunc_needed0 == 1:
        number = trunc(number * 10**(start_trunc - point_place - 5)) / 10**(start_trunc - point_place - 5)
    elif trunc_needed9 == 1:
        if number < 0:
            number = trunc((number * 10**(start_trunc - point_place - 5)) - 1) / 10**(start_trunc - point_place - 5)
        else:
            number = trunc((number * 10**(start_trunc - point_place - 5)) + 1) / 10**(start_trunc - point_place - 5)
    return number
                
def new_inc(string_min_value,inc,part):
    array_part = part.split(" ")
    #print(str(string_min_value) + " string_min_value")
    #print(str(array_part) + " array_part")
    for i in range(len(array_part)):
        if array_part[i] == "=":
            part1_a = []
            for e in range(i):
                part1_a.append(array_part[e])
            part2_a = []
            for e in range(len(array_part) - i - 1):
                part2_a.append(array_part[e + i + 1])
    string_min_value_a1 = string_min_value[0].split(" ")
    string_min_value_a2 = string_min_value[1].split(" ")
    #print("TEST")
    #print(str(part1_a) + " part1_a")
    #print(str(part2_a) + " part2_a")
    #print(str(string_min_value_a1) + " string_min_value_a1")
    #print(str(string_min_value_a2) + " string_min_value_a2")
    for i in range(len(inc)):
        for e in range(len(part1_a)):
            if inc[i][0] == part1_a[e]:
                inc[i][1] = float(string_min_value_a1[e])
        for e in range(len(part2_a)):
            if inc[i][0] == part2_a[e]:
                inc[i][1] = float(string_min_value_a2[e])   
    #print(str(inc) + " NEW INC")
    return inc

def set_when_new_value_needed(inc,inc_starts_values,equality):
    global number_try_start
    global dif
    global pas_touche_dif
    repartition = base_n(number_try_start,len(inc),9)
    for i in range(len(inc)):
        inc[i][1] = inc_starts_values[int(repartition[i:i + 1])]
    number_try_start = number_try_start + 1
    #print(str(dif) + " dif")
    #print(str(pas_touche_dif) + " pas_touche_dif")
    for i in range(len(dif)):
        dif[i] = pas_touche_dif[i]
    #print(str(inc) + " NEW START VALUES")
    #print(str(number_try_start))
    string_equality = []
    for a in range(len(equality)):
        string_equality.append(equality[a].split(" = "))
        string_equality[a][0] = string_equality[a][0].split(" ")
        string_equality[a][1] = string_equality[a][1].split(" ")
    for a in range(len(equality)):
        for i in range(2):
            for e in range(len(string_equality[a][i])):
                for u in range(len(inc)):
                    if string_equality[a][i][e] == inc[u][0]:
                        string_equality[a][i][e] = inc[u][1]
    string_min_value = []
    for a in range(len(equality)):
        string_part = ["",""]
        for i in range(2):
            for e in range(len(string_equality[a][i])):
                string_part[i] = string_part[i] + str(string_equality[a][i][e]) + " "
                string_part[i].strip()
        string_min_value.append(string_part)
    #print(str(string_min_value) + " STRING_MIN_VALUE")
    return string_min_value



def calc_start_values():
    global inc_starts_values
    new_inc_starts_values = []
    total_value = [0,0]
    for i in range(len(inc_starts_values)):
        total_value[0] = total_value[0] + inc_starts_values[i]
    for i in range(len(inc_starts_values) - 1):
        moyenne = (inc_starts_values[i] + inc_starts_values[i + 1]) / 2
        new_inc_starts_values.append(moyenne)
        total_value[1] = total_value[1] + new_inc_starts_values[i]
    last_value = total_value[0] - total_value[1]
    i = 0
    while last_value > new_inc_starts_values[i]:
        i = i + 1
    provisoire = [new_inc_starts_values[i]]
    new_inc_starts_values[i] = last_value
    i = i + 1
    while i != len(new_inc_starts_values):
        provisoire.append(new_inc_starts_values[i])
        new_inc_starts_values[i] = provisoire[0]
        provisoire.pop(0)
        i = i + 1
    new_inc_starts_values.append(provisoire[0])
    #print(new_inc_starts_values)
    for i in range(len(inc_starts_values)):
        inc_starts_values[i] = new_inc_starts_values[i]

    

def run(string):
    global inc
    global total_tested_value
    global number_try_start
    global multi_final_inc_value
    global final_inc_values_work
    global failed_final_inc
    global inc_starts_values
    global number_calc_depart_values
    analyse(string)
    #print(" INC STAARST " + str(inc_starts_values))
    test = 0
    while test == 0:
        #print(" compare -> START")
        string_min_value = compare(equality)
        #print(" compare -> DONE")
        #print(str(inc) + " INC AFTER COMPARE")
        #print("BELLOW")
        #print(string_min_value)
        if number_calc_depart_values == 3:
            test = 1
        if len(string_min_value) == len(equality) + 1:
            if multi_final_inc_value == 0:
                test = 1
            #print("EQUAL")
            #print(str(string_min_value) + "string_min_value")
            for a in range(len(equality)):
                #print(str(inc) + " inc b")
                inc = new_inc(string_min_value[a],inc,equality[a])
                #print(str(inc) + " inc after")
            test_same_final_value = 0
            for i in range(len(inc)):
                trunc_needed(inc[i][1])
                for e in range(len(final_inc_values_work[i])):
                    if inc[i][1] == final_inc_values_work[i][e]:
                        test_same_final_value = 1
            #print(str(final_inc_values_work) + " final_inc_values_work")
            if test_same_final_value == 0:
                for i in range(len(inc)):
                    final_inc_values_work[i].append(inc[i][1])
                    failed_final_inc[i].append(final_inc_values_work[i][len(final_inc_values_work[i]) - 1])
                    prep_inc = inc[i][1]
                    prep_inc = trunc(100000000*prep_inc)/100000000
                    print(inc[i][0] + " = " + str(prep_inc))
                if total_tested_value != 0:
                    print("Nombre de valeurs de départs testées: " + str(total_tested_value + number_try_start + 1))
                else:
                    print("Nombre de valeurs de départs testées: " + str(number_try_start + 1))
                print("Temps: " + str(process_time()))
            else:
                if number_try_start < 9**len(inc):
                    set_when_new_value_needed(inc,inc_starts_values,equality)
                else:
                    calc_start_values()
                    number_calc_depart_values = number_calc_depart_values + 1
                    print("Nouvelles valeurs de départs...")
                    total_tested_value = total_tested_value + number_try_start
                    number_try_start = 0
                    set_when_new_value_needed(inc,inc_starts_values,equality)
        else:
            for a in range(len(equality)):
                inc = new_inc(string_min_value[a],inc,equality[a]) 

run(string)
#min([[1,2,"division error",4,5],[10,9,7,4,2],[2,2,2,0,14]])
#print(base_n(8428,4,10))
#print(trunc_needed(1.23475063))
#calc_start_values()