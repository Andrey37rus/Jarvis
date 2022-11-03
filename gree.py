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
    finally: return


def home(*args):
    """Я дома!"""
    try:
        playsound(os.path.join('music_jar', 'greetings.wav'))
        return
    except:
        Exception()
    finally: return


def good_days(*args):
    """Добрый день"""
    try:
        playsound(os.path.join('music_jar', 'good_morning.wav'))
        return
    except:
        Exception()


def thanks(*args):
    try:
        playsound(os.path.join('music_jar', 'thanks.wav'))
        return
    except:
        Exception()


def i_need(*args):
    try:
        playsound(os.path.join('music_jar', 'yes_ser.wav'))
        return
    except:
        Exception()


def mistake(*args):
    try:
        playsound(os.path.join('music_jar', 'mistake.wav'))
        return
    except:
        Exception()


def off_comp(*args):
    try:
        playsound(os.path.join('music_jar', 'restart.wav'))
        return
    except:
        Exception()


def yes_ser(*args):
    try:
        playsound(os.path.join('music_jar', 'eat.wav'))
        return
    except:
        Exception()