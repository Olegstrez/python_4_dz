# # Даны два файла, в каждом из которых находится запись многочлена.
# # Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_1.txt', 'w') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_2.txt', 'w') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()


with open('poly_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

print(f'{list_of_poly_1} + {list_of_poly_2}')
sum_poly = list_of_poly_1 + list_of_poly_2

with open('sum_poly.txt', 'w') as file:
    file.write(f'{list_of_poly_1} + {list_of_poly_2}')
# with open('data.txt', 'w') as f:
#     data = 'some data to be written to the file'
#     f.write(data)

# with open('data.txt', 'r') as f:
#     data = f.read()
