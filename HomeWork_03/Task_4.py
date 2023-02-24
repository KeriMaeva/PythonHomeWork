'''Задача 4: Напишите программу, которая будет 
преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
import copy
input_number = int(input('Введите число: '))
number = copy.copy(input_number)
result = ''
while number > 0:
    result = str(number % 2) + result
    number = number // 2
print(f'{input_number} -> {result}')