# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def find_text(text):
    my_list = [i for i in text.split() if 'абв' not in i]
    return my_list

def print_text(text):
    print(f'Результат: {" ".join(find_text(text))}')

text = input("Введите текст:")
print_text(text)