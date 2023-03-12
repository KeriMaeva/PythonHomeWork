'''
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
'''

def menu(data):
    print('''\nКоманды для работы со справочником:
        Просмотр всех записей справочника:  - 1
        Поиск по справочнику для работы с записью - 2
        Добавление новой записи - 3
        Сохранить справочник в файл - 4''')
    
    command = input('Команда: > ')
    if command == '1':
        screen(data)
        menu(data)
    elif command == '2':
        index_data = search_data(data)
        menu_for_change(data, index_data)
    elif command == '3':
        data = add_user(data)
        menu(data)
    elif command == '4':
        write_data(data)
        menu(data)


def menu_for_change(data, index_data):
    print('''\nЧто делаем с текущей записью:
        Удаление записи из справочника - 1
        Изменение записи справочника - 2 
        Вернуться в меню - 0 ''')
    command = input('Команда: > ')
    if command == '1':
        del_data(data, index_data)
        menu(data)
    elif command == '2':
        change_data(data, index_data)
        menu(data)
    elif command == '0':
        menu(data)

def del_data(data, index_data):
    data.pop(index_data)

def change_data(data, index_data):
    new_name = input("Измените пользователя ФИО и номер телефона: ")
    for elem in range(len(data)):
        if index_data == elem:
            data[elem] = new_name

def search_data(data):
    text = input('Введите текст для поиска: ')
    for elem in range(len(data)):
        if text in data[elem]:
            print(data[elem])
            return elem

def write_data(data):
    with open('HomeWork/HomeWork_08/fio.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)

def add_user(data):
    data.append('\n' + input("Добавьте пользователя ФИО и номер телефона: "))
    return data

def read_data():
    with open('HomeWork/HomeWork_08/fio.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
        return data

def screen(data):
    for elem in data:
        print(elem.strip())

def main():
    data = read_data()
    menu(data)

if __name__ == '__main__':
    main()



