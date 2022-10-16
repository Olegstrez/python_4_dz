# Вычислить число c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141
import math

def pi_number(numbers):
    k = 1
    pi = 0
    for i in range ( 1000000 ):
        if i % 2 == 0 :
             pi +=4 / k
        else :
            pi -= 4 / k
        k += 2
    numbers_list = str(pi).split(".")

    pi=3+int(numbers_list[1][0:numbers])/(math.pow(10,numbers))
    return pi 
print(pi_number(10))
