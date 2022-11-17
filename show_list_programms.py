import os
import json
from gree import answer_jarvis
from playsound import playsound
from colorama import Fore, Back, Style


def list_programs(*args):
    """Показывает список программ добавленных в каталог"""
    if os.path.isfile('name_path_program.json'):
        answer_jarvis()
        with open('name_path_program.json', 'r') as file:
            data = json.load(file)
        print('***СПИСОК ПРОГРАММ***')
        for name in data:
            print(Fore.LIGHTGREEN_EX + name)
        print('___________________')
    else:
        playsound(os.path.join('music_jar', 'mistake.wav'))
        print(Fore.RED + 'Файл не существует')


def list_chunk():
    """Показывает список программ добавленных в каталог"""

    if os.path.isfile('name_program.json'):
        with open('name_program.json', 'r') as file:
            data = json.load(file)
            return data

    else:
        playsound(os.path.join('music_jar', 'mistake.wav'))
        print(Fore.RED + 'Файл не существует')

#
# def commands_list(*args):
#     """Показывает список команд применяемых голосом"""
#
#     print(Fore.)