'''2. Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''
import random
def input_(name):
    x = int(
        input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    return x


def print_move(name, k, counter, value):
    print(
        f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def first_move():
    flag = random.randint(0, 2)
    if flag:
        print(f"Первый ходит {player1}")
        return flag
    else:
        print(f"Первый ходит {player2}")
        return flag
player1 = "Игрок 1"
player2 = "Игрок 2"
value = 221
count_1 = 0
count_2 = 0
print(f'На столе лежит {value} конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.')
flag = first_move()

while value > 28:
    if flag:
        k = input_(player1)
        count_1 += k
        value -= k
        flag = False
        print_move(player1, k, count_1, value)
    else:
        k = input_(player2)
        count_2 += k
        value -= k
        flag = True
        print_move(player2, k, count_2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
