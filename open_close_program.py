import json
import os
from answer_jarvis import answer_jarvis
from playsound import playsound
import subprocess
# from gree import thanks


def run_programs(*args):
    """Запуск программ"""
    try:
        name = ' '.join(args[0]).lower()
        if len(name) != 0:
            if os.path.isfile('name_path_program.json'):
                with open('name_path_program.json', 'r') as file:
                    name_path_program = json.load(file)
                for key in name_path_program.keys():
                    if name in key:
                        path = name_path_program[key]
                        print(path)
                        answer_jarvis()
                        # subprocess.run(str(path))
                        os.startfile(str(path))
                        break
            else:
                playsound(os.path.join('music_jar', 'mistake.wav'))
                print('Нет файла!\n'
                      'добавьте программу')
        else:
            playsound(os.path.join('music_jar', 'mistake.wav'))
            print('Программы не существует!')

    except IndexError:
        IndexError()


def close_program(*args):
    print(args)
    """Закрытие программ"""
    try:
        name = ' '.join(args[0]).lower()
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
                    break
            else:
                playsound(os.path.join('music_jar', 'mistake.wav'))
                print('Программа не нашлась')
        else:
            playsound(os.path.join('music_jar', 'mistake.wav'))
            print('Нет файла!\n'
                  'добавьте программу')
    except IndexError:
        IndexError()
