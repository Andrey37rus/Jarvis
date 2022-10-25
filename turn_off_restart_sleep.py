from gree import yes_ser, off_comp
import os


def shutdown(*args):
    """Завершение работы"""
    off_comp()
    os.system("shutdown /s /t 1")
    # subprocess.run(["shutdown", "-s"])


def restart(*args):
    """Перезагрузка системы"""
    off_comp()
    os.system("shutdown /r /t 1")


def sleep_mode(*args):
    """Спящий режим"""
    yes_ser()
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
