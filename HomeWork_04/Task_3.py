'''Задача 3: Задайте последовательность чисел. 
Напишите программу, которая выведет список 
неповторяющихся элементов исходной последовательности.
'''

my_list = list(input("Введите числа через пробел: ").split())
print(f"Исходный список: {my_list}")
my_set = set(my_list)
print(f"Список из неповторяющихся элементов: {my_set}")