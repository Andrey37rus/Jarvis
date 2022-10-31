# from fuzzywuzzy import fuzz
# from comands import execute_name
import time


# text = 'друг закрой прогу'
#
#

# import requests
#
# response = requests.get('https://www.youtube.com/')
# print(response)

import win32gui
import win32con
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
from ctypes import *
import ctypes
# for i in range(10):
#     hWnd = ctypes.windll.user32.GetForegroundWindow()
#     print('ключ:', hWnd)
#     time.sleep(3)


# from win32gui import GetWindowText, GetForegroundWindow
# print(GetWindowText(GetForegroundWindow()))

def getWindow_W_H(hwnd):
    # Получить размер целевого окна
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    print(left, top, right, bot)
    width = right - left - 15
    height = bot - top - 11
    print(width, height)
    return (left, top, width, height)


hWnd = ctypes.windll.user32.GetForegroundWindow()
getWindow_W_H(hWnd)

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

import psutil
import ctypes
from ctypes import wintypes

# pid = wintypes.DWORD()
# active = ctypes.windll.user32.GetForegroundWindow()
# active_window = ctypes.windll.user32.GetWindowThreadProcessId(active, ctypes.byref(pid))
#
# pid = pid.value
# for item in psutil.process_iter():
#     if pid == item.pid:
#         print(item.name())
#         win32gui.ShowWindow(328626, win32con.SW_MINIMIZE)


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

import pyautogui as pg

# print(pg.KEYBOARD_KEYS)



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

# for i in x.values():
#     enter = enter.replace(i, "").strip()
# print("VA_X", enter)


# for index in y:
#     enter = enter.replace(index, "").strip()
# print("VA_TBR:", enter)


#
# dict_list = {'key': '', 'percant': 30}
# count = 0
# for k, v in x.items():
#     print(v)
#
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

# from fuzzywuzzy import fuzz
#
#
# values_values = 'утро доброе'
# dictt = {'доброе утро': ('все ок')}
#
# values = ''
#
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