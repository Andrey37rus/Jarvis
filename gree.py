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


def thanks(*args):
    playsound(os.path.join('music_jar', 'thanks.wav'))
    return


def i_need(*args):
    playsound(os.path.join('music_jar', 'yes_ser.wav'))
    return


def mistake(*args):
    playsound(os.path.join('music_jar', 'mistake.wav'))
    return


