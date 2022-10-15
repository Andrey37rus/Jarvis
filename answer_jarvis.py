import random
from playsound import playsound
import os


def answer_jarvis(*args, **kwargs):
    gret_list = [
        os.path.join('music_jar', 'eat.wav'),
        os.path.join('music_jar', 'loading_sir.wav'),
        os.path.join('music_jar', 'request_completed_sir.wav')
    ]
    playsound(random.choice(gret_list))
    return

