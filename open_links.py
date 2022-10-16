import webbrowser
from answer_jarvis import answer_jarvis
from playsound import playsound
import os

list_links = {'яндекс': 'https://ya.ru/',
              'гугл': 'https://www.google.ru/',
              'ютуб': 'https://www.youtube.com/',
              'вконтакте': 'https://vk.com/feed',
              }


def open(text):
    link = ''.join(text)
    print('open', link)
    url = ''

    for k, v in list_links.items():
        if link in k:
            url = v
            answer_jarvis()
            webbrowser.open_new_tab(url)
            return




