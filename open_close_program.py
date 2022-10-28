import json
import os
from gree import answer_jarvis, mistake
from playsound import playsound
import subprocess
from gree import thanks


def run_programs(name: str):
    """Запуск программ"""

    print('open app:', name)
    print(type(name))

    name = name.split()[1:]
    print(name)
    name = ' '.join(name).lower()

    if len(name) != 0:
        if os.path.isfile("name_path_program.json"):
            with open('name_path_program.json', 'r') as file:
                name_path_program = json.load(file)
            for key in name_path_program.keys():
                if name in key:
                    path = name_path_program[key]
                    answer_jarvis()
                    subprocess.Popen(str(path))
                    # os.startfile(str(path))
                    return
            print('нет файла или пути больше не существует')
        else:
            mistake()
            print('Нет файла!\n'
                  'добавьте программу')
    else:
        mistake()
        print('Программы не существует!')


def close_program(name: str):
    """Закрытие программ"""

    print('close app:', name)
    print(type(name))

    name = name.split()[1:]
    print(name)
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
                    print(new_name)
                    subprocess.call("taskkill /f /im {app}".format(app=new_name))
                    # os.system("TASK-KILL /F /IM {app}".format(app=new_name))
                    answer_jarvis()
                    return
            else:
                mistake()
                print('Программа не нашлась')
        else:
            mistake()
            print('Нет файла!\n'
                  'добавьте программу')
    except IndexError:
        IndexError()
