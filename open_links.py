import time
import webbrowser
from gree import answer_jarvis, i_need
import pyautogui as pg
import ctypes
import py_win_keyboard_layout
from http import cookies

list_links = {
            'https://yandex.ru/': ('search/?text=', 'яндекс',  'яндексе'),
            'https://www.google.ru/': ('search?q=', 'гугл', 'гугле'),
            'https://www.youtube.com/': ('results?search_query=', 'ютуб', 'ютубе')

}


def search_str_youtube():
    webbrowser.open_new_tab("https://www.youtube.com/")
    i_need()
    time.sleep(2)
    for i in range(4):
        pg.press(['tab'])


def open(text):

    """ Удаление 1 слова 0 индексом из строки"""
    name_url = " ".join(text.split()[1:])

    for k, v in list_links.items():
        if name_url in v:
            if name_url == 'ютуб' or name_url == 'ютубе':
                search_str_youtube()
                return
            elif name_url == 'яндекс' or name_url == 'яндексе':
                answer_jarvis()
                webbrowser.get().open('https://ya.ru/')
                return
            elif name_url == 'гугл' or name_url == 'гугле':
                answer_jarvis()
                webbrowser.open_new_tab(k)


def search_by_internet(text: str):
    text = text.split()
    text.remove(text[0])

    for sym in text:
        if sym == 'в' or sym == 'на':
            text.remove(sym)

    for elem in text:
        for k, v in list_links.items():
            if elem in v:
                text.remove(elem)
                answer_jarvis()
                webbrowser.get().open(k + v[0] + ' '.join(text))
                return
    answer_jarvis()
    url = "https://yandex.ru/search/?text=" + ' '.join(text)
    webbrowser.get().open(url)


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

    symbol = {'ё': '`', 'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o',
              'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j',
              'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n',
              'ь': 'm', 'б': ',', 'ю': '.'}

    x = get_layout()

    num = int
    if x == 'en':
        num = 0x4090409
    elif x == 'ru':
       num = 0x4190419

    if x == 'en':
        py_win_keyboard_layout.change_foreground_window_keyboard_layout(0x4190419)

    for elem in word_list:
        if elem == ' ':
            pg.press('space')
        for k, v in symbol.items():
            if elem == k:
                pg.typewrite(v)
                time.sleep(0.1)
    pg.press(['enter'])
    py_win_keyboard_layout.change_foreground_window_keyboard_layout(int(num))





