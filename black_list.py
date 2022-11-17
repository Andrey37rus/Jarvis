# from fuzzywuzzy import fuzz
# from comands import execute_name
# import time


# text = 'друг закрой прогу'
#
#

# import requests
#
# response = requests.get('https://www.youtube.com/')
# print(response)

# import win32gui
# import win32con
#
# win32gui.ShowWindow(328626, win32con.SW_MINIMIZE)
#
# from win32gui import GetWindowText, GetForegroundWindow
# count = 0
# while True:
#     if count == 10:
#         break
#     def windowEnumHandler(hwnd, top_windows):
#         top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#     def bringToFront(window_name):
#         top_windows = []
#
#         win32gui.EnumWindows(windowEnumHandler, top_windows)
#             # for num, elem in enumerate(top_windows):
#             #     print('elem:', num + 1, ':', elem)
#         for i in top_windows:
#             if i[1] == window_name:
#                 print('activ-win', i)
#                 # win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)
#     time.sleep(2)
#
#     activate = GetWindowText(GetForegroundWindow())
#
#     print('активное окно название', activate)
#
#     bringToFront(activate)




    # top_windows = []
    # win32gui.EnumWindows(windowEnumHandler, top_windows)
    # for num, elem in enumerate(top_windows):
    #     print('elem:', num + 1, ':', elem)


                    # if window_name.lower() in i[1].lower() and 'gdi+' not in i[1].lower():
                    #     win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
                    #     win32gui.SetForegroundWindow(i[0])
                    #     break


#
# def windowEnumHandler(hwnd, top_windows):
#     top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#
# def bringToFront(window_name):
#     top_windows = []
#
#     win32gui.EnumWindows(windowEnumHandler, top_windows)
#     for num, elem in enumerate(top_windows):
#         print('elem:', num + 1, ':', elem)
#     for i in top_windows:
#         if window_name.lower() in i[1].lower() and 'gdi+' not in i[1].lower():
#             win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
#             win32gui.SetForegroundWindow(i[0])
#             break

# new_name = 'AIMP.exe'
#
# bringToFront(new_name)
# from ctypes import *
# import ctypes
# for i in range(10):
#     hWnd = ctypes.windll.user32.GetForegroundWindow()
#     print('ключ:', hWnd)
#     time.sleep(3)


# from win32gui import GetWindowText, GetForegroundWindow
# print(GetWindowText(GetForegroundWindow()))
#
# def getWindow_W_H(hwnd):
#     # Получить размер целевого окна
#     left, top, right, bot = win32gui.GetWindowRect(hwnd)
#     print(left, top, right, bot)
#     width = right - left - 15
#     height = bot - top - 11
#     print(width, height)
#     return (left, top, width, height)
#
#
# hWnd = ctypes.windll.user32.GetForegroundWindow()
# getWindow_W_H(hWnd)

# def getWindow_Img(hwnd):
#     # Замените hwnd на WindowLong
#     s = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
#     win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, s|win32con.WS_EX_LAYERED)

# def activate_win(*args):
#
#     hwnd = int
#     activ_win_icon = list()
#     activ_win_icon.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#
# def windowEnumHandler(hwnd, top_windows):
#     top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#
# top_windows = []
# win32gui.EnumWindows(windowEnumHandler, top_windows)
#
# for num, elem in enumerate(top_windows):
#     print('elem:', num + 1, ':', elem)
#
# for i in top_windows:
#     print('id:', i[0])

# import psutil
# import ctypes
# from ctypes import wintypes

# pid = wintypes.DWORD()
# active = ctypes.windll.user32.GetForegroundWindow()
# active_window = ctypes.windll.user32.GetWindowThreadProcessId(active, ctypes.byref(pid))
#
# pid = pid.value
# for item in psutil.process_iter():
#     if pid == item.pid:
#         print(item.name())
#         win32gui.ShowWindow(328626, win32con.SW_MINIMIZE)

# import win32security
# import win32api
# import sys
# import time
# from ntsecuritycon import *

#
# def AdjustPrivilege(priv, enable=1):
#     # Get the process token
#     flags = TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY
#     htoken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
#     # Get the ID for the system shutdown privilege.
#     idd = win32security.LookupPrivilegeValue(None, priv)
#     # Now obtain the privilege for this process.
#     # Create a list of the privileges to be added.
#     if enable:
#         newPrivileges = [(idd, SE_PRIVILEGE_ENABLED)]
#     else:
#         newPrivileges = [(idd, 0)]
#     # and make the adjustment
#     win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges)

#
# def RebootServer(user=None,message='Rebooting', timeout=30, bForce=0, bReboot=1):
#     AdjustPrivilege(SE_SHUTDOWN_NAME)
#     try:
#         win32api.InitiateSystemShutdown(user, message, timeout, bForce, bReboot)
#     finally:
#         # Now we remove the privilege we just added.
#         AdjustPrivilege(SE_SHUTDOWN_NAME, 0)
#
# def AbortReboot():
#     AdjustPrivilege(SE_SHUTDOWN_NAME)
#     try:
#         win32api.AbortSystemShutdown(None)
#     finally:
#         AdjustPrivilege(SE_SHUTDOWN_NAME, 0)

#
# AdjustPrivilege(SE_SHUTDOWN_NAME)


# AdjustPrivilege(SE_SHUTDOWN_NAME)
# win32api.SetSystemPowerState(True, True) # спящий режим

# win32api.SetSystemPowerState(False, True) # кибернация
# AbortReboot()

# import ctypes
# from ctypes import wintypes
#
# pid = wintypes.DWORD()
# active = ctypes.windll.user32.GetForegroundWindow()
# active_window = ctypes.windll.user32.GetWindowThreadProcessId(active, ctypes.byref(pid))
# print('id activate window:', active_window)

# import pyautogui as pg

# while True:
#     post = pg.position()
#     print(post)
#     time.sleep(1)
#Point(x=601, y=132) рпоиска ютуб асположение
# xy = pg.moveTo(None, None,)
# print(xy)



# size = pg.size()
# print(size)


# import ctypes
# import py_win_keyboard_layout
#
# def get_layout():
#     u = ctypes.windll.LoadLibrary("user32.dll")
#     pf = getattr(u, "GetKeyboardLayout")
#     if hex(pf(0)) == '0x4190419':
#         return 'ru'
#     if hex(pf(0)) == '0x4090409':
#         return 'en'

# import pyautogui as pg

# print(pg.KEYBOARD_KEYS)
# import time
# text = "Привет ебанный мир!"
#
# for word in text:
#     time.sleep(0.2)
#     print(word, end='')
    # time.sleep(0.1)


# pg.press(['volumemute'])


# import win32api
#
# win32api.LoadKeyboardLayout("00000419", 1)

# from sound import Sound
# vol = int(input("Введите громкость звука в единицах (0..100): "))
# Sound.volume_set(vol)

# import keyboard
#
# btn_up = 'up'
# btn_down = 'down'
#
# enter = input('выберите громкость up or down: ')
#
# number = int(input('Выберите громкость от 0 100: '))
#
# if enter == 'up':
#     keyboard.press("ctrl")
#
#     for num in range(number):
#         keyboard.send(btn_up)
#     print(number)

# import webbrowser

# search_term = " ".join(args[0])

# search_term = 'стихи есенина'
#
# url = "https://yandex.ru/search/?text=" + search_term
# webbrowser.get().open(url)

# url = "https://www.youtube.com/results?search_query=" + search_term
# webbrowser.get().open(url)

# import time, sys
#
# def anything(str):
#
#     for letter in str:
#       sys.stdout.write(letter)
#       sys.stdout.flush()
#       time.sleep(0.2)
#
# anything("Blah Blah Blah...")



# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#
# volume = cast(interface, POINTER(IAudioEndpointVolume))
#
# volume.GetMute()


# volume = cast (interface, POINTER(IAudioEndpointVolume))
# volume.GetMute()
# volume.GetMasterVolumeLevel()
# volume.GetVolumeRange()
# volume.SetMasterVolumeLevel(-20.0, None)
#
# import queue
#
#
# q = queue.Queue()
# list_ind = ['собака', 'кошка', 'харек', 'улитка', 'педик']
#
# for i in list_ind:
#     q.put(i)
#
# while not q.empty():
#     print(q.get(), end=' ')
#
#



# name = ('джэйди', 'друг')
#
# x = {
#     "one": ('запусти', 'открыть',),
#     'two': ('я дома'),
#     'three': ('закрыть прогу'),
#     'for': ('выключи комп'),
# }
#
# y = ('запусти', 'закрой', 'выключи')
#
#
# enter = text
#
# for i in name:
#     enter = enter.replace(i, "").strip()
# print("VA_ALIAS", enter)
#
# for i in x.values():
#     enter = enter.replace(i, "").strip()
# print("VA_X", enter)
#
#
# for index in y:
#     enter = enter.replace(index, "").strip()
# print("VA_TBR:", enter)
#
#
#
# dict_list = {'key': '', 'percant': 30}
# count = 0
# for k, v in x.items():
#     print(v)

#
#     vrt = fuzz.ratio(enter, v)
#     count += 1
#     print(vrt)
#     if vrt > dict_list['percant']:
#         dict_list['key'] = k
#         dict_list['percant'] = vrt
#
# print(dict_list)
# print('всего:', count)
#
# cod = dict_list['key']
#
#
# dict_list = {'key': ''}
#
# for k, v in x.items():
#
#     if v == enter:
#         dict_list['key'] = k
# print(dict_list)
#
# cod = dict_list['key']
#
# if cod in x.keys():
#     if cod == 'one':
#         print('Приложение запущенно')
#
#     elif cod == 'two':
#         print('Хорошо что вы дома')
#
#     elif cod == 'three':
#         print('Закрываю приложение')
#
#     elif cod == 'for':
#         print('Выключаю')
#     elif cod == 'fife':
#         print('Приложение открыто')
#
#     else:
#         print('Ошибка')
#
# from fuzzywuzzy import fuzz
#
#
# values_values = 'утро доброе'
# dictt = {'доброе утро': ('все ок')}
#
# values = ''

#
# for key in dictt:
#     a = fuzz.token_sort_ratio(values_values, key)
#     print(a)
#     if a == 100:
#         values = key
#         print("значение values:", values)
#     if values in key:
#         print('все ок')




# from datetime import datetime, date, time
# x = dict()
# data = datetime.today().replace(microsecond=0)
# x[str(data)] = 'now'
# print(x)



# a = fuzz.ratio('Привет мир', 'Првет мр')
# print(a)


# import config
# import gree
#
# voice = 'джарвис утречко'
#

# def func_x(voice: str):
#     text = voice
#     print(text)
#     text = voice.split()
#     if text[0] in config.VA_ALIAS:
#         config.red_list.append(text[0])
#         text.remove(text[0])
#         func_y(text)
#
#     else:
#         print('ошибка имени!')
#
#
# def func_y(text):
#     good_voice =list()
#     text = text
#     for k, v in config.chunk.items():
#         for sym in v:
#             for word in text:
#                 if word == sym:
#                     good_voice.append(word)
#                     text.remove(text[0])
#     func_a(good_voice)
#
#
# def func_a(text):
#     text = text
#     good_word = ' '.join(text)
#     for key in config.chunk.keys():
#         if key == good_word:
#             gree.good_days()
#
# func_x(voice)
#

import sys
import os


# from remember import *
#
#
# def func():
#     print('Запустился скрипт')
#     while True:
#         x = int(input(':'))
#         if x == 1:
#             xxx()
#         else:
#             print('Работаем дальше')
#
#
# if __name__ == "__main__":
#     func()

import subprocess


# elif x == 1:
#     # os.execl(sys.executable, sys.executable, *sys.argv)
#     # os.execv(sys.executable, ['python3'] + sys.argv)
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
#     print('перезагрузка')
# else:
#     print('good')

# import sys
# import os
#
# def restartApp():
#
#     python = sys.executable
#     os.execl(python, python, *sys.argv)
#
# restartApp()

# import subprocess
#
# path = r"D:\games\Mortal Kombat X\Binaries\Retail\MK10.exe"
# subprocess.Popen(str(path))

from colorama import Fore, Back, Style
from config import commands
import json

data = {
    'искать': "служит для поиска в интернете. Пример: {jarvis} + {искать} + Ваш запрос{ каком году родился Пушкин}",
    'поиск': "служит для в вода текста в поисковой строке. Пример: {jarvis} + {искать} + Ваш запрос{смотреть фильм Хоббит}",
    'ты здесь': "jarvis отвечает на ваш вопрос: -Да сэр",
    'спасибо': "jarvis отвечает на вашу благодарность: -Всегда к вашим услугам сэр",
    'громче': "Служит для увеличения громкости. Пример:  {jarvis} + {Громче} ",
    'тихо': "Служит для уменьшения громкости. Пример:  {jarvis} + {Тише} ",
    'без звука': "Сделать без звука весь компьютер. Пример:  {jarvis} + {без звука}",
    'звук': "Сделать звук к исходному значению на всем компьютер. Пример:  {jarvis} + {звук}",
    'следующий трек': "Служит для переключение трека в play-листе. Пример:  {jarvis} + {следующий трек}",
    'предыдущий трек': "Служит для переключение трека в play-листе. Пример:  {jarvis} + {предыдущий трек}",
    'открыть': "Служит для открытия браузерных ссылок таких как yandex, google, you-tube. Пример: {jarvis} + {открыть} + {you-tube}",
    'запустить': "",
    'добавить программа': "",
    'выключить компьютер': "",
    'доброе утро': "",
    'перезагрузить компьютер': "",
    'спящий режим': "",
    'мёртвый режим': "",
    'закрыть': "",
    'выключить': "",
    'список программа': "",
    'свернуть': "",
    'развернуть': "",
    'я дома': "",
    'play': "",
    'конец': "",
    'перезагрузить программа': "",
    'список команд': "",
}


def commands_list():
    """Показывает список команд применяемых голосом"""

    with open('commands list.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)




    # with open('name_path_program.json', 'r') as file:
    #     data = json.load(file)
    # data[name] = path
    #
    # with open('name_path_program.json', 'w') as file:
    #     json.dump(data, file, indent=4, ensure_ascii=False)
    #     add_program_chunk(name_prog, path)
    #     print('Путь добавлен')
    #     new_element()
    # else:
    #     data[name] = path
    #     with open('name_path_program.json', 'w') as file:
    #         json.dump(data, file, indent=4, ensure_ascii=False)
    #         add_program_chunk(name_prog, path)
    #         print('Путь добавлен')
    #         new_element()



    #
    # print(Fore.CYAN + '\n', '*' * 7, 'список команд', '*' * 7,  end='\n' * 2)
    #
    # for key in commands.keys():
    #     print('*' * 2, 'jarvis', key, '*' * 2)


commands_list()
