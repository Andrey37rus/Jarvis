from playsound import playsound
import os
import random


def answer_jarvis(*args):
    try:
        greet_list = [
            os.path.join('music_jar', 'eat.wav'),
            os.path.join('music_jar', 'loading_sir.wav'),
            os.path.join('music_jar', 'request_completed_sir.wav')
        ]
        playsound(random.choice(greet_list))
        return
    except:
        Exception()


def home(*args):
    """Я дома!"""
    playsound(os.path.join('music_jar', 'greetings.wav'))
    return


def good_days(*args):
    """Добрый день"""
    playsound(os.path.join('music_jar', 'good_morning.wav'))
    return


def thanks(*args):

    playsound(os.path.join('music_jar', 'thanks.wav'))
    return


def i_need(*args):

    playsound(os.path.join('music_jar', 'yes_ser.wav'))
    return


def mistake(*args):

    playsound(os.path.join('music_jar', 'mistake.wav'))
    return


def off_comp(*args):
    playsound(os.path.join('music_jar', 'restart.wav'))
    return


def yes_ser(*args):
    playsound(os.path.join('music_jar', 'eat.wav'))
    return


def new_element(*args):
    playsound(os.path.join('music_jar', 'make new element.wav'))
    return


def restart(*args):
    playsound(os.path.join('music_jar', 'restart_prog.wav'))
    return


def as_you_wish(*args):
    """закрывает приложение Jarvis"""
    playsound(os.path.join('music_jar', 'As-you-wish.wav'))
    return


def I_rebooted(*args):
    """Перезагрузка программы"""
    playsound(os.path.join('music_jar', 'I_rebooted.wav'))
    return
