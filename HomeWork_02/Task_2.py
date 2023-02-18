'''
Задача 2: Напишите программу, 
которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.
Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''

number = int(input('Введите целое число N: '))
index = 1
result = 1
print(f"Произведений чисел от 1 до {number} = [ ", end='')
while index <= number:
    result = index * result
    if index < number:
        print(f"{result}", end=', ')
    else:
        print(f"{result}", end=' ]')
    index += 1