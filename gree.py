from playsound import playsound
import os


def home(*args):
    """Я дома!"""
    playsound(os.path.join('music_jar', 'greetings.wav'))
    return


def good_days(*args):
    """Добрый день"""
    playsound(os.path.join('music_jar', 'good_morning.wav'))
    return


def thanks():
    playsound(os.path.join('music_jar', 'thanks.wav'))
    return


def i_need():
    playsound(os.path.join('music_jar', 'yes_ser.wav'))
    return



