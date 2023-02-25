'''Задача 4: Задана натуральная степень k. 
Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 
или x² + 5 = 0 или 10*x² = 0
'''

import random
k = int(input("Введите натуральную степень k = "))
koef = [random.randint(0, 101) for i in range(k+1)]
k_list = koef[::-1]
result = ''
if len(k_list) < 1:
    result = 'x = 0'
else:
    for i in range(len(k_list)):
        if i != len(k_list) - 1 and k_list[i] != 0 and i != len(k_list) - 2:
            result += f'{k_list[i]}x^{len(k_list)-i-1}'
            if k_list[i+1] != 0:
                result += ' + '
        elif i == len(k_list) - 2 and k_list[i] != 0:
            result += f'{k_list[i]}x'
            if k_list[i+1] != 0:
                result += ' + '
        elif i == len(k_list) - 1 and k_list[i] != 0:
            result += f'{k_list[i]} = 0'
        elif i == len(k_list) - 1 and k_list[i] == 0:
            result += ' = 0'
print(result)