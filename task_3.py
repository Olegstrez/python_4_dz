# Задайте последовательность чисел. Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

import os
os.system('cls' if os.name == 'nt' else 'clear')
numbers_list = [int (i) for i in input().split()]
print(numbers_list)
def find_eqvivalent(numbers_list):
    lidt_1=[]
    lidt_1_new = []
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list)):
            if  numbers_list[i] == numbers_list[j] and i != j:
                lidt_1.append(i)
    for i in range(len(numbers_list)):
        count=0
        for j in lidt_1:
            if i == j:
                count+=1
        if count ==0:
            lidt_1_new.append(numbers_list[i]) 
    return lidt_1_new
print(find_eqvivalent(numbers_list))
