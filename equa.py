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
precision_accru = 0
nombre_entier = 0
inc_starts_values = [-10,-5,-1,-0.5,0,0.5,1,5,10]
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
    global precision_accru
    for a in range(len(string)):
        part1 = ""
        part2 = ""
        for i in range(len(string[a])):
            close = 0
            e = 0
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
        final_inc_values_work.append([])
        index_zero_array.append(0)
    input_options = input("option (oui/non): ")
    if input_options == 'oui':
        optional_input()
    else:
        for i in range(len(inc)):
            dif.append(1)
            pas_touche_dif.append(1)
    print("...")
   
def optional_input():
    global multi_final_inc_value
    global precision_accru
    global nombre_entier
    global inc_starts_values
    global dif
    global pas_touche_dif
    input_start_values = input("valeurs de depart (9): ")
    inc_starts_values = input_start_values.strip().split(" ")
    if len(inc_starts_values) != 9:
        inc_starts_values = [-10,-5,-1,-0.5,0,0.5,1,5,10]
    for i in range(len(inc_starts_values)):
        inc_starts_values[i] = float(inc_starts_values[i])
    input_multi = input("chercher le plus de valeurs possibles (oui/non): ")
    if input_multi == 'oui':
        multi_final_inc_value = 1
    else:
        multi_final_inc_value = 0
    input_precision = input("précision accrue (oui/non): ")
    if input_precision == 'oui':
        precision_accru = 1
    else:
        precision_accru = 0
    input_nbr_entier = input("donner une réponse que pour les entiers (oui/non):")
    if input_nbr_entier == 'oui':
        nombre_entier = 1
    else:
        nombre_entier = 0
    for i in range(len(inc)):
        dif.append(float(input("dif de " + inc[i][0] + " : ").strip()))
    for i in range(len(dif)):
        pas_touche_dif.append(dif[i])

def calc(part1):
    part1_array = part1.strip().split(" ")
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
    part1_array = part1_e.strip().split(" ")
    i = len(part1_array) - 1
    while i != -1:
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
    result = calc(no_par_value)
    return result

def set_int(inc,array_dif,part):
    #change les valeurs des inc en fonctions des dif
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
                calc_int = calc_int.replace(inc[i][0],str(trunc_needed(new_value)))
            returned[a].append(calc_int)
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
    for i in range(len(array[0])):
        inter_value = 0
        test = 0
        for a in range(len(array)):
            if array[a][i] != "division error":
                test = test + 1
        if test == len(array):
            for a in range(len(array)):
                inter_value = inter_value + array[a][i]
            add_array.append(inter_value)
        else:
            add_array.append(100)
    for i in range(len(add_array) - 1):
        if add_array[i + 1] < add_array[min_value]:
            min_value = i + 1
    return min_value


def compare(equality):
    global dif
    global inc_starts_values
    global inc
    global number_try_start
    global index_zero_int
    #index_zero_int est le nombre de fois ou len(str(inc[i][1])) n'a pas evolué
    global index_zero_array
    #index_zero_array contient par inc -> len(str(inc[i][1])) pour voir si un nombre evolue ou pas
    global failed_final_inc
    #failed_final_inc contient les valeurs raté des inc
    global total_tested_value
    global number_calc_depart_values
    global precision_accru
    global nombre_entier
    possible_v = set_int(inc,dif,equality)
    result = []
    dif_result = []
    returned = []
    # possivle_v contient par equation -> une array par possibilité de changement de valeur de inc dans set_int -> array= l'egalité (string) avec les inc([0][0]) remplacer par les valeurs des inc([0][1])
    # result contient par equation -> une array par possibilité de changement de valeur de inc dans set_int -> array= les deux valeurs des deux parties de l'egalité
    # dif_result contient par equation -> n valeurs (n=len(result[0]) -> chaque valeur egal la dif entre les deux parties de l'egalité
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
    for i in range(len(possible_v[0])):
        test = 0
        error = 0
        for a in range(len(equality)):
            if result[a][i][0] != "division error" and result[a][i][1] != "division error":
                if precision_accru == 0:
                    if isclose(result[a][i][0],result[a][i][1],rel_tol=1e-05):
                        test = test + 1
                else:
                    if isclose(result[a][i][0],result[a][i][1],abs_tol=1e-05):
                        test = test + 1
            else:
                error = 1
        if test == len(equality): 
            for a in range(len(equality)):
                returned.append(possible_v[a][i])
            returned.append("equal")
            return returned
        else:
            for a in range(len(equality)):
                if error == 0:
                    dif_result[a].append(fabs(result[a][i][0] - result[a][i][1]))
                else:
                    dif_result[a].append("division error")
    #min cherche la plus petite valeur de dif_result
    index = min(dif_result)
    
    if index == 0:
        # aucun changement marche -> differents test pour voir s'il faut changer de valeurs de depart
        new_values_needed = 0
        if nombre_entier == 1 and control_inc(inc) == False:
            new_values_needed = 1
        test = 0
        for i in range(len(inc)):
            test_inc = 0
            for e in range(len(failed_final_inc[i])):
                if precision_accru == 0:
                    if isclose(inc[i][1],failed_final_inc[i][e],rel_tol=1e-3):
                        test_inc = 1
                else:
                    if isclose(inc[i][1],failed_final_inc[i][e],rel_tol=1e-10):
                        test_inc = 1
            test = test + test_inc
        if test == len(inc):
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
                        if precision_accru == 0:
                            if test0 == 3 or test9 == 3:
                                new_values_needed = 1
                        else:
                            if test0 == 7 or test9 == 7:
                                new_values_needed = 1 
        if new_values_needed == 1:
            #change les valeurs des inc
            test = 0
            for e in range(len(failed_final_inc[i])):
                if inc[i][1] == failed_final_inc[i][e]:
                    test = 1
            if test == 0:
                for i in range(len(inc)):
                    failed_final_inc[i].append(inc[i][1])
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
    string_min_value = []
    for a in range(len(equality)):
        string_min_value.append(possible_v[a][index])
    #string_min_value contient par egalité -> une array -> partie 1 de l'egalité et partie 2 de l'egalité
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
    #array_part contient l'egalité (array)
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
    for i in range(len(inc)):
        for e in range(len(part1_a)):
            if inc[i][0] == part1_a[e]:
                inc[i][1] = float(string_min_value_a1[e])
        for e in range(len(part2_a)):
            if inc[i][0] == part2_a[e]:
                inc[i][1] = float(string_min_value_a2[e])   
    return inc

def set_when_new_value_needed(inc,inc_starts_values,equality):
    global number_try_start
    global dif
    global pas_touche_dif
    #pas_touche_dif contient les dif de base (entré au debut)
    #equality contient les egalité (string)
    repartition = base_n(number_try_start,len(inc),9)
    for i in range(len(inc)):
        inc[i][1] = inc_starts_values[int(repartition[i:i + 1])]
    number_try_start = number_try_start + 1
    for i in range(len(dif)):
        dif[i] = pas_touche_dif[i]
    string_equality = []
    for a in range(len(equality)):
        string_equality.append(equality[a].split(" = "))
        string_equality[a][0] = string_equality[a][0].split(" ")
        string_equality[a][1] = string_equality[a][1].split(" ")
    #string_equality contient par equation -> 2 array part 1 et 2 d'une egalité (array) (pas de =) -> chaque part est une array 
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
    #string_min_value contient par equation -> une array -> de deux array -> part 1 et 2 egalité (array)
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
    for i in range(len(inc_starts_values)):
        inc_starts_values[i] = new_inc_starts_values[i]

def when_wrong_final_result():
    global number_try_start
    global inc
    global inc_starts_values
    global equality
    global total_tested_value
    global number_calc_depart_values
    if number_try_start < 9**len(inc):
        set_when_new_value_needed(inc,inc_starts_values,equality)
    else:
        calc_start_values()
        number_calc_depart_values = number_calc_depart_values + 1
        if number_calc_depart_values != 3:
            print("Nouvelles valeurs de départs...")
        total_tested_value = total_tested_value + number_try_start
        number_try_start = 0
        set_when_new_value_needed(inc,inc_starts_values,equality)

def look_for_same_result():
    global inc
    global final_inc_values_work
    test_same_final_value = 0
    for i in range(len(inc)):
        trunc_needed(inc[i][1])
        for e in range(len(final_inc_values_work[i])):
            if inc[i][1] == final_inc_values_work[i][e]:
                test_same_final_value = 1
    return test_same_final_value

def when_a_result_found(string_min_value):
    global inc
    global equality
    global total_tested_value
    global number_try_start
    global multi_final_inc_value
    # multi_final_inc_value = 1 si cherche plusieurs valeurs des inc
    global final_inc_values_work
    #final_inc_values_work contient les valeurs des inc qui sont correct
    global failed_final_inc
    test = 0
    if multi_final_inc_value == 0:
        test = 1
    test_same_final_value = look_for_same_result()
    add_same_final_value(test_same_final_value)
    if test_same_final_value == 0:
        for i in range(len(inc)):
            prep_inc = inc[i][1]
            if precision_accru == 0:
                prep_inc = trunc(100000000*prep_inc)/100000000
            print(inc[i][0] + " = " + str(prep_inc))
        if total_tested_value != 0:
            print("Nombre de valeurs de départs testées: " + str(total_tested_value + number_try_start + 1))
        else:
            print("Nombre de valeurs de départs testées: " + str(number_try_start + 1))
        print("Temps: " + str(process_time()) + "\n")
    else:
        when_wrong_final_result()
    return test

def add_same_final_value(test_same_final_value):
    global final_inc_values_work
    global failed_final_inc
    if test_same_final_value == 0:
        for i in range(len(inc)):
            final_inc_values_work[i].append(inc[i][1])
            failed_final_inc[i].append(final_inc_values_work[i][len(final_inc_values_work[i]) - 1])

def control_inc(inc):
    test = 0
    for i in range(len(inc)):
        controled_part = str(inc[i][1])
        if controled_part[len(controled_part) - 2:len(controled_part)] == '.0':
            test = test + 1
    if test == len(inc):
        return True
    else:
        return False

def run(string):
    global inc
    global number_calc_depart_values
    global equality
    global nombre_entier
    global multi_final_inc_value
    analyse(string)
    test = 0
    while test == 0:
        string_min_value = compare(equality)
        if len(string_min_value) == len(equality) + 1:
            for a in range(len(equality)):
                inc = new_inc(string_min_value[a],inc,equality[a])
            if nombre_entier == 1:
                if control_inc(inc):
                    test = when_a_result_found(string_min_value)
                else:
                    test_same_final_value = look_for_same_result()
                    add_same_final_value(test_same_final_value)
                    when_wrong_final_result()
            else:
                test = when_a_result_found(string_min_value)
        else:
            for a in range(len(equality)):
                inc = new_inc(string_min_value[a],inc,equality[a]) 
        if number_calc_depart_values == 3:
            test = 1
    if multi_final_inc_value == 1:
        print('Temps: ' + str(process_time()))

run(string)
