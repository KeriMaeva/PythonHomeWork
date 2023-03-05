'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''
import random

my_list = []
index_list = []
n = int(input('Задайте длинну списка: '))
min_number = int(input('Задайте минимум: '))
max_number = int(input('Задайте максимум: '))
for i in range(n):
    my_list.append(random.randint(-10, 11))
    
print (f'Исходный список: {my_list}')
for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        index_list.append(i)
print (f'Индексы элементов списка, значения которых принадлежат диапазону {min_number} от до {max_number}: {index_list}')