# from fuzzywuzzy import fuzz
# from comands import execute_name

# text = 'друг закрой прогу'
#
#

# from sound import Sound
# vol = int(input("Введите громкость звука в единицах (0..100): "))
# Sound.volume_set(vol)

import keyboard

btn_up = 'up'
btn_down = 'down'

enter = input('выберите громкость up or down: ')

number = int(input('Выберите громкость от 0 100: '))

if enter == 'up':
    keyboard.press("ctrl")

    for num in range(number):
        keyboard.send(btn_up)
    print(number)








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