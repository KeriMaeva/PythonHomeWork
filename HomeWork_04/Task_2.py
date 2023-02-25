'''Задача 2: Задайте натуральное число N. 
Напишите программу, которая составит 
список простых множителей числа N.
'''

number = int(input("Введите число: "))
i = 2  
my_list = []
my_number = number
while i <= number:
    if number % i == 0:
        my_list.append(i)
        number //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {my_number} равны: {my_list}")