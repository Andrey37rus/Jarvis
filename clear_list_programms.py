import os
from gree import answer_jarvis
from playsound import playsound


def clear(*args):
    if os.path.isfile('name_path_program.json'):
        answer_jarvis()
        os.remove('name_path_program.json')
        if os.path.isfile('name_program.json'):
            os.remove('name_program.json')
    else:
        playsound(os.path.join('music_jar', 'mistake.wav'))



