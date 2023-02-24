'''Задача 3: Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.

Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
list = [1.1, 1.2, 3.1, 5, 10.01]
mini = 1000000
maxi = 0
for i in range(len(list)):
    ostatok = round(list[i] % 1, 2)
    if ostatok > 0:
        if ostatok < mini:
            mini = ostatok
        if ostatok > maxi:
            maxi = ostatok
print(f'{list} => {round(maxi - mini, 2)}')
