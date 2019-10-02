import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import subprocess
from math import gcd
from math import ceil
from math import modf

r = input('Suite: ')
r = r.split(',')
for i in range(len(r)):
    r[i] = int(r[i])
shape = len(r)
a = []
for i in range(shape):
    array = []
    num = i+1
    for e in range(shape):
        add = num**(shape-e-1)
        array.append(add)
    a.append(array)
#create np.array
R = np.array(r)
A = np.array(a)
df = pd.DataFrame(A)  

#solve
Inc = np.linalg.solve(A,R)


#create func
def search_p(number):
    count = 0
    for i in range(len(str(number))):
        if str(number)[i:i+1] == '.':
            same = 0
            same_num = [str(number)[i+1:i+2],i + 1]
            for e in range(len(str(number))-i):
                if str(number)[e+i:e+i+1] == same_num[0]:
                    same += 1
                    if same == 5:
                        return str(number)[0:same_num[1]] +'$'
                else:
                    same_num = [str(number)[e+i:e+i+1],e+i+1]
    return str(number)

def search_point(string):
    for e in range(len(str(string))):
        if str(string)[e:e+1] == '.':
            return e

def display_func(inc):
    func='f(n)= '
    for i in range(len(inc)):
        if str(inc[i][0]).find('-') != -1:
            func += inc[i][0]
        else:
            func += '+' + inc[i][0]
        if inc[i][1] != 0:
            func += ' n^' + str(inc[i][1])+' '
    print(func)

def analyse_1(Inc):
    Inc_1 = []
    for i in range(len(Inc)):
        Inc_1.append([search_p(Inc[i]),len(Inc)-i-1])
    return Inc_1

def analyse_2(Inc_1):
    i = -1
    Inc_2 = []
    while i < len(Inc_1) -1:
        i += 1
        try:
            if abs(float(Inc_1[i][0])) < 10**-8:
                Inc_1.pop(i)
                i -= 1
            else:
                Inc_2.append([str(Inc_1[i][0]),Inc_1[i][1]])
        except:
            if Inc_1[i][0].find('$') != -1:
                length = len(Inc_1[i][0])
                calc_num = float(Inc_1[i][0][0:length-1])
                point_place = search_point(calc_num)
                if Inc_1[i][0][length-2:length-1] == '0':
                    period = 0
                else:
                    period = int(str(calc_num)[length-2:length-1])*10**(-length+point_place+2)
                #print(str(period)+' period')
                int_num = (9*calc_num + period)*10**(length-point_place-3)
                point_place2 = search_point(int_num)
                if str(int_num)[point_place2+1:point_place2+2] == '9':
                    int_num = ceil(int_num)
                #print(str(int_num)+' int_num')
                deno = int(9*10**(length-point_place-3))
                div = gcd(int(int_num),deno)
                final_num = str(int(int_num/div))+"/"+str(int(deno/div)) 
                #print(final_num)
                Inc_2.append([final_num,Inc_1[i][1]])
    return Inc_2

#print(Inc)
Inc_1 = analyse_1(Inc)
#print(Inc_1)
Inc_2 = analyse_2(Inc_1)
#print(Inc_2)

display_func(Inc_2)


#calc suite
for e in range(len(Inc)+5):
    a = e+1
    num = 0
    for i in range(shape):
        num+= Inc[i]*(a**(shape-1-i))
    if num <0:
        arrondi = ceil(num+1)
    else: arrondi = ceil(num)
    if modf(num)[0] < 0.5 and modf(num)[0] != 0:
            print(arrondi-1)
    else:
        print(ceil(num))

def figure(Inc,shape,pre):
    suite = [[],[]]
    suite2 = []
    for a in range(int(pre*(shape + 1)+2)):
        num = 0
        suite2.append(0)
        for i in range(shape):
            num+= Inc[i]*(((a-1)/pre)**(shape-1-i))
        suite[0].append(num) 
        suite[1].append((a-1)/pre)   
    fig = plt.figure()
    plt.plot(suite[1],suite[0])
    plt.plot(suite[1],suite2)
    plt.xticks([suite[1][pre*e+1] for e in range(ceil(len(suite[1])/pre-1))])
    fig.savefig('plot.png')

def display_image():
    subprocess.call(['xdg-open','/home/alexandre/Documents/python/math/plot.png'])

figure(Inc,shape,20)
display_image()