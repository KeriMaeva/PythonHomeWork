"""1. Напишите программу, которая принимает 
на вход цифру, обозначающую день недели, 
и проверяет, является ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет
"""
day = int(input('Введите день недели: '))
if 1 <= day <= 5:
    print('Нет')
elif 6 <= day <= 7:
    print('Да')
else:
    print(f"Число {day} не является днём недели")