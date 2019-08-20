from math import trunc
from math import sqrt
from time import process_time
def prime_search(number):
    number_calc = number
    test = 0
    diviseur = []
    while test == 0:
        old_number_calc = number_calc
        i = 2
        while i <= trunc(sqrt(number_calc)) + 1:
            if search_point_zero(number_calc/i):
                old_i = i
                diviseur.append(i)
                i = trunc(sqrt(number_calc)) + 1
                number_calc = number_calc/old_i
            else:
                i = i + 1
        if number_calc == old_number_calc:
            test = 1
    print("Temps: " + str(process_time()))
    if len(diviseur) != 0:
        diviseur.append(number_calc)
        print(str(number) + " n'est pas premier -> " + str(number) + " = " + build_message(diviseur))
    else:
        print(str(number) + " est premier.")
        return number
    
def prime_search_in_prime(number):
    number_calc = number
    test = 0
    diviseur = []
    content = read_content_array("prime_data.txt","\n")
    while test == 0:
        old_number_calc = number_calc
        duration = search_nearest_prime(number_calc,content)
        i = 0
        while i != duration:
            if search_point_zero(number_calc / int(content[i])):
                old_i = i
                diviseur.append(int(content[i]))
                i = duration
                number_calc = number_calc/ int(content[old_i])
            else:
                i = i + 1
        if number_calc == old_number_calc:
            test = 1
    print("Temps: " + str(process_time()))
    if len(diviseur) != 0:
        diviseur.append(number_calc)
        print(str(number) + " n'est pas premier -> " + str(number) + " = " + build_message(diviseur))
    else:
        print(str(number) + " est premier.")
        return number

def read_content_array(file_name,split_car):
    file = open(file_name)
    content = file.read()
    file.close()
    content = content.split(split_car)
    return content

def search_point_zero(number_search):
    for i in range(len(str(number_search))):
        if str(number_search)[i:i + 1] == '.' and str(number_search)[i + 1:i + 2] == '0' and i + 2 == len(str(number_search)):
            return True
    return False

def search_nearest_prime(number_calc,content):
    number_target = trunc(sqrt(number_calc))
    i = 0
    while int(content[i]) < number_target:
        i = i + 1
    return i

def build_message(diviseur):
    message = str(diviseur[0])
    for i in range(len(diviseur) - 1):
        message = message + " * " + str(diviseur[i + 1])
    return message

def normal_run(number):
    if number > 1000000000000:
        prime_search(number)
    else:
        prime_search_in_prime(number)

def add_prime_data(lower_number,higher_number):
    file = open("prime_data.txt","a")
    for i in range(higher_number - lower_number + 1):
        pos_prime = prime_search_in_prime(i + lower_number)
        if pos_prime != None:
            file.write("\n" + str(pos_prime))
    file.close()
    print(process_time())

number = int(input(" Entrer un nombre (temps de calcul x50 apres 1000000000000): "))
normal_run(number)