import json
import os
from gree import answer_jarvis, mistake
import subprocess
from colorama import Fore, Back, Style


def run_programs(name: str):
    """Запуск программ"""
    name = name.split()

    if len(name) != 0:
        if os.path.isfile("name_path_program.json"):
            with open('name_path_program.json', 'r') as file:
                name_path_program = json.load(file)
                for elem in name:
                    for key in name_path_program.keys():
                        if elem in key:
                            path = name_path_program[key]
                            answer_jarvis()
                            subprocess.Popen(str(path))
                            return
                print(Fore.RED + 'нет файла или пути больше не существует')
                mistake()
        else:
            mistake()
            print(Fore.RED + 'Нет файла!\n'
                  'добавьте программу')
    else:
        mistake()
        print(Fore.RED + 'Программы не существует!')


def close_program(name: str):
    """Закрытие программ"""

    name = name.split()[1:]
    name = ' '.join(name)
    try:
        if os.path.isfile('name_path_program.json'):
            with open('name_path_program.json', 'r') as file:
                name_path_program = json.load(file)

            for key in name_path_program.keys():
                if name in key:
                    path = name_path_program[key]
                    b = path[::-1]
                    slash = b.index('\\')
                    new_name = b[:slash]
                    new_name = new_name[::-1]
                    subprocess.call("taskkill /f /im {app}".format(app=new_name))
                    answer_jarvis()
                    return
            else:
                mistake()
                print(Fore.LIGHTYELLOW_EX + 'Программа не нашлась')
        else:
            mistake()
            print(Fore.RED + 'Нет файла!\n'
                  'добавьте программу')
    except IndexError:
        IndexError()
