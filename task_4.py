# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from importlib.resources import path
from pathlib import Path
import time
import os
os.system('cls' if os.name == 'nt' else 'clear')
min = 0
max = 100
def random_my(min, max):
    time.sleep(0.3)
    return (int(time.time() % 1 *(max-min)+min))
def koficent(n):
    resukt_k=[ ]
    for i in range(n):
        resukt_k.append(random_my(min, max))
    return resukt_k
def function (k):
    list_1=[]
    i = k
    str_result=""
    list_result=[]
    while i > 0:
        if i !=1:
            list_1.append("x^"+str(i))
            i-=1
        else:
            list_1.append("x")
            i-=1
    list_2 = koficent(k)
    for i in range(k):
        list_result.append(str(list_2[i])+"*"+list_1[i])
    z = koficent(1)
    list_result.append(str(z[0]))
    for i in range(k+1):
        if i ==0:
            str_result+=list_result[i]
        else:
            str_result+="+"+list_result[i]
    return str_result

data=open ("file.txt","w")
for i in range(3):
    data.write(function(4)+"\n")
data.close


path = "file.txt"
data = open(path,"r")
for line in data:
    print(line)
data.close