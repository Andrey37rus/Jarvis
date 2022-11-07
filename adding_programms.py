import os
import json
from gree import answer_jarvis
from gree import new_element
from colorama import Fore, Back, Style


def add_program_answer(*args):
    answer_jarvis()
    add_program()
    return


def add_program(*args):
    """Добавление названия программы и ее пути в словарь"""

    data = dict()

    print(Fore.LIGHTBLUE_EX + 'Введите название программы')
    name_prog = input().lower().split(', ')
    name = str(tuple(name_prog))
    print(Fore.LIGHTBLUE_EX + 'Введите путь')
    path = input()

    if os.path.exists(path):
        if os.path.isfile('name_path_program.json'):
            with open('name_path_program.json', 'r') as file:
                data = json.load(file)
            data[name] = path

            with open('name_path_program.json', 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                add_program_chunk(name_prog, path)
                print('Путь добавлен')
                new_element()
        else:
            data[name] = path
            with open('name_path_program.json', 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                add_program_chunk(name_prog, path)
                print('Путь добавлен')
                new_element()
    else:
        print(Fore.RED + 'Ошибка! Такого пути не существует')
        add_program()


def add_program_chunk(name_prog, path):

    data_game = dict()
    name_game = ' '.join(name_prog)
    name_game = name_game.split()
    for elem in name_game:
        if os.path.exists(path):
            if os.path.isfile('name_program.json'):
                with open('name_program.json', 'r') as file:
                    data_game = json.load(file)
                data_game[elem] = elem

                with open('name_program.json', 'w') as file:
                    json.dump(data_game, file, indent=4, ensure_ascii=False)
                    print(Fore.LIGHTGREEN_EX + 'Путь добавлен')
            else:
                data_game[elem] = elem
                with open('name_program.json', 'w') as file:
                    json.dump(data_game, file, indent=4, ensure_ascii=False)

                print(Fore.LIGHTGREEN_EX + 'Путь добавлен')
        else:
            print(Fore.RED + 'Ошибка! Такого пути не существует')
            add_program()
