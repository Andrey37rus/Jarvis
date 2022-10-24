import time
import webbrowser
from answer_jarvis import answer_jarvis
import pyautogui as pg
import ctypes
import py_win_keyboard_layout

list_links = {'яндекс': 'https://ya.ru/',
              'гугл': 'https://www.google.ru/',
              'ютуб': 'https://www.youtube.com/',
              'вконтакте': 'https://vk.com/feed',
              }


def open(text):

    """ Удаление 1 слова 0 индексом из строки"""
    s2 = " ".join(text.split()[1:])
    print('open', s2)

    url = ''

    for k, v in list_links.items():
        if s2 in k:
            url = v
            answer_jarvis()
            webbrowser.open_new_tab(url)
            return


def search_by_internet(text):
    answer_jarvis()
    search = ''.join(text)
    print('поиск в инете', search)
    url = "https://yandex.ru/search/?text=" + search
    webbrowser.get().open(url)
    return


def get_layout():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x4090409':
        return 'en'


def text_search(text: str):
    s2 = " ".join(text.split()[1:])
    s2 = s2.split()

    word_list = list()
    if len(s2) > 1:
        for word in s2:
            for i in word:
                word_list.append(i)
            word_list.append(' ')
    else:
        for elem in s2:
            for i in elem:
                word_list.append(i)

    print('finish', word_list)
    print('finished', ','.join(word_list))
    symbol = {'ё': '`', 'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o',
              'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j',
              'л': 'k', 'д': 'l', 'ж': ';', 'э': '''''', 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n',
              'ь': 'm', 'б': ',', 'ю': '.'}
    x = get_layout()
    if x == 'en':
        num = 0x4090409
    else:
       num = 0x4190419
    if x == 'en':
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x4190419)

    for elem in word_list:
        if elem == ' ':
            pg.press('space')
        for k, v in symbol.items():
            if elem == k:
                pg.typewrite(v)
    pg.press(['enter'])
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(num)





