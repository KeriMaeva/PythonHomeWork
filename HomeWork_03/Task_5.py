'''Задача 5: Задайте число. 
Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.

Пример:
- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 
2, 3, 5, 8, 13, 21]'''

list_f = [1, 0, 1]
f1 = 0
fn1 = 0
f2 = 1
fn2 = 1
f3 = 1
fn3 = -1
i = 1
k = int(input('Введите число больше ноля: '))
while i < k:
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    fn3 = fn1 - fn2
    fn1 = fn2
    fn2 = fn3
    list_f.append(f3)
    list_f.insert(0, fn3)
    i += 1
print(list_f)
