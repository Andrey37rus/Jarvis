import sys
from win32ctypes.core import ctypes
from gree import yes_ser, off_comp, as_you_wish
import ctypes
import win32security
import win32api
from ntsecuritycon import *
import os


def AdjustPrivilege(priv, enable=1):
    # Get the process token
    flags = TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY
    htoken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
    # Get the ID for the system shutdown privilege.
    idd = win32security.LookupPrivilegeValue(None, priv)
    # Now obtain the privilege for this process.
    # Create a list of the privileges to be added.
    if enable:
        newPrivileges = [(idd, SE_PRIVILEGE_ENABLED)]
    else:
        newPrivileges = [(idd, 0)]
    # and make the adjustment
    win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges)


def shutdown(*args):
    """Завершение работы"""
    try:
        off_comp()
        AdjustPrivilege(SE_SHUTDOWN_NAME)
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000008, 0x00000000)
        return
    except:
        Exception()


def restart(*args):
    """Перезагрузка системы"""
    try:
        off_comp()
        AdjustPrivilege(SE_SHUTDOWN_NAME)
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000002, 0x00000000)
        return
    except:
        Exception()


def sleep_mode(*args):
    """Спящий режим"""
    try:
        yes_ser()
        AdjustPrivilege(SE_SHUTDOWN_NAME)
        win32api.SetSystemPowerState(True, True)
        return
    except:
        Exception()


def hibernation(*args):
    """Режим гибернации
    Нужен чтоб полностью обесточить комп но в оперативной памяти оставить все запущенные процессы
    """
    try:
        yes_ser()
        AdjustPrivilege(SE_SHUTDOWN_NAME)
        win32api.SetSystemPowerState(False, True)
    except:
        Exception()


def exxit(*args):
    """Завершение приложения!"""
    as_you_wish()
    sys.exit()


def reboot_program(*args):
    """Перезагрузка программы"""
    yes_ser()
    path = os.path.abspath(os.path.join('reboot.py'))
    os.startfile(path)
    sys.exit()
