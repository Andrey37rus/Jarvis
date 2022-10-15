from playsound import playsound
import os


def shutdown(*args):
    """Завершение работы"""

    playsound(os.path.join('music_jar', 'shutdown.wav'))
    os.system("shutdown /s /t 1")


def restart(*args):
    """Перезагрузка системы"""

    playsound(os.path.join('music_jar', 'restart.wav'))
    os.system("shutdown /r /t 1")


def sleep_mode(*args):
    """Спящий режим"""
    playsound(os.path.join('music_jar', 'eat.wav'))
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
