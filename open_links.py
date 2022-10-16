import webbrowser
from answer_jarvis import answer_jarvis


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


def search_by_internet(text):
    answer_jarvis()
    search = ''.join(text)
    print('поиск в инете', search)
    url = "https://yandex.ru/search/?text=" + search
    webbrowser.get().open(url)
    return


