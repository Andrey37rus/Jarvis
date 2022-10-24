#  Jarvis 2.0
# auto-py-to-exe для компиляции online

import json
from datetime import datetime

import config
import stt
import os
from gree import i_need, mistake
from fuzzywuzzy import fuzz


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

head = {'head': 'off'}


def header(voice: str):
    text = str(voice).split()
    name = config.VA_ALIAS

    for elem in text:
        if elem in name:
            if len(text) == 1:
                i_need()
                head['head'] = 'on'
                del text
                return
            elif len(text) > 1:
                off_line(voice.replace(elem, ''))
                return

    if head['head'] == 'on':
        if len(voice) == 0:
            del voice
            return
        else:
            off_line(voice)


def off_line(voice):
    log_voice(voice)
    good_text = list()
    commands_dict = dict()
    head['head'] = 'off'

    for elem in voice.split():
        for k, v in config.chunk.items():
            if elem in v:
                good_text.append(k)
                break
    if len(good_text) == 0:
        mistake()
        return
    commands_dict[' '.join(good_text)] = voice
    func_y(commands_dict)


    # for elem in text:
    #     for k, v in config.chunk.items():
    #         if elem in v:
    #             good_text.append(k)
    #             for word in good_text:
    #                 if word in config.words_arguments or word in config.words_arguments_web:
    #                     print(elem)
    #                     good_text = ''.join(good_text)
    #                     text = ' '.join(text)
    #                     text = text.replace(elem, '')
    #                     commands_dict[good_text] = text
    #                     argument(commands_dict)
    #
    # if len(good_text) == 0:
    #     playsound(os.path.join('music_jar', 'mistake.wav'))
    #     print("Command not found")
    #     return
    # good_text = ' '.join(good_text)
    # commands_dict['good_text'] = good_text
    # func_y(commands_dict)


# def off_line(voice: str):
#     log_voice(voice)
#     text = voice.split()
#     good_text = list()
#     commands_dict = dict()
#     head['head'] = 'off'
#
#     for elem in text:
#         for k, v in config.chunk.items():
#             if elem in v:
#                 good_text.append(k)
#     if len(good_text) == 0:
#         playsound(os.path.join('music_jar', 'mistake.wav'))
#         print("Command not found")
#         return
#     for elem in good_text:
#         if elem in config.words_arguments or elem in config.words_arguments_web:
#             print(elem)
#             good_text = ''.join(good_text)
#             text = ' '.join(text)
#             commands_dict[good_text] = text
#             argument(commands_dict)
#     else:
#         good_text = ' '.join(good_text)
#         commands_dict['good_text'] = good_text
#         func_y(commands_dict)

#
# def argument(text: dict):
#     text = text
#     commands_list = list()
#
#     values = text.values()
#     values = ' '.join(values)
#     values = values.split()
#     try:
#         if 'запустить' in text:
#             argument_list = show_list_programms.list_chunk()
#
#             for elem in values:
#                 for k, v in argument_list.items():
#                     if elem in v:
#                         commands_list.append(k)
#             commands_list = ' '.join(commands_list)
#             text['запустить'] = commands_list
#             func_y(text)
#
#         # elif 'выключить' in text:
#         #         values = text.values()
#         #         values = ' '.join(values)
#         #         values = values.split()
#         #
#         #         for elem in values:
#         #             for k, v in argument_list.items():
#         #                 if elem in v:
#         #                     commands_list.append(k)
#         #         commands_list = ' '.join(commands_list)
#         #         text['выключить'] = commands_list
#         #         func_y(text)
#
#         elif 'искать' in text:
#             values_search = values[2:]
#             values_search = ' '.join(values_search)
#             text['искать'] = values_search
#             print('text', text)
#             func_y(text)
#
#         elif 'поиск' in text:
#             # values_search = values[2:]
#             # values_search = ' '.join(values_search)
#             values = ' '.join(values)
#             text['поиск'] = values
#             print('text', text)
#             func_y(text)
#
#         elif 'открыть' in text:
#             argument_list_links = open_links.list_links
#             for elem in values:
#                 for k, v in argument_list_links.items():
#                     if elem in k:
#                         commands_list.append(k)
#                         commands_list = ' '.join(commands_list)
#                         text['открыть'] = commands_list
#                         func_y(text)
#                         return
#             else:
#                 playsound(os.path.join('music_jar', 'mistake.wav'))
#                 print('нет ссылки')
#
#         elif 'закрыть' in text:
#             argument_list = show_list_programms.list_chunk()
#             for elem in values:
#                 for k, v in argument_list.items():
#                     if elem in v:
#                         commands_list.append(k)
#             commands_list = ' '.join(commands_list)
#             text['закрыть'] = commands_list
#             func_y(text)
#     except AttributeError:
#         AttributeError()


def func_y(text: dict):
    text = text
    keys_keys = ' '.join(text.keys())
    values_values = ' '.join(text.values())

    for k, v in config.commands.items():
        if k == keys_keys:
            config.commands[k](values_values)
            return
    else:
        mistake()
        return



    # if keys_keys in config.words_arguments or keys_keys in config.words_arguments_web:
    #     for key in config.commands.keys():
    #         fuzzz = fuzz.token_sort_ratio(keys_keys, key)
    #         if fuzzz == 100:
    #             keys = key
    #             if keys in key:
    #                 config.commands[key](text.values())
    #                 break
    #             else:
    #                 playsound(os.path.join('music_jar', 'mistake.wav'))
    #                 print("Command not found")
    #                 return

    # elif keys_keys == 'good_text':
    #     for key in config.commands.keys():
    #         fuzzz = fuzz.token_sort_ratio(values_values, key)
    #         if fuzzz == 100:
    #             values = key
    #             if values in key:
    #                 config.commands[key]()
    #                 break
    #             else:
    #                 playsound(os.path.join('music_jar', 'mistake.wav'))
    #                 print("Command not found")
    #                 return
    #


def log_voice(text: str):
    text = text
    print(text)
    for elem in text.split():
        if elem in config.VA_ALIAS:
            date = str(datetime.today().replace(microsecond=0))
            data = dict()

            if os.path.isfile('configs.json'):
                with open('configs.json', 'r') as file:
                    data = json.load(file)
                data[date] = text

                with open('configs.json', 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)
            else:
                data[date] = text
                with open('configs.json', 'w') as file:
                    json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    stt.va_listen(header)


if __name__ == "__main__":
    main()
