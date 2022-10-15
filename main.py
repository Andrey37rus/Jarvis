#  Jarvis 2.0

import json
from datetime import datetime

import config
import show_list_programms
import stt
from playsound import playsound
import os
from fuzzywuzzy import fuzz


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

# head = {1: 'off'}


# def on_line():
#     while True:
#         voice = stt.record_and_recognize_audio()
#         voice = str(voice)
#
#         log_voice(voice)
#         text = voice.split()
#         good_text = list()
#         commands_dict = dict()
#
#         if head == 'on':
#             head['head'] = 'off'
#             text.append('джарвис')
#
#         for name in config.VA_ALIAS:
#             for name_text in text:
#                 if name_text == name:
#                     if len(text) == 1:
#                         playsound(os.path.join('music_jar', 'yes_ser.wav'))
#                         head['head'] = 'on'
#                         break
#                     print('Пошел дальше')
#                     name_index = text.index(name_text)
#                     text.pop(name_index)
#                     for elem in text:
#                         for k, v in config.chunk.items():
#                             if elem in v:
#                                 good_text.append(k)
#                     if len(good_text) == 0:
#                         playsound(os.path.join('music_jar', 'mistake.wav'))
#                         print("Command not found")
#
#                     elif 'запустить' in good_text or 'закрыть' in good_text or 'выключить' in good_text:
#                         good_text = ' '.join(good_text)
#                         text = ' '.join(text)
#                         commands_dict[good_text] = text
#                         argument(commands_dict)
#                     else:
#                         good_text = ' '.join(good_text)
#                         commands_dict['good_text'] = good_text
#                         func_y(commands_dict)

# head = {'head': 'off'}

# def yea_ser():
#     head[1] = 'on'
#     playsound(os.path.join('music_jar', 'yes_ser.wav'))
#     return
#
#
# def off_line(voice: str):
#     log_voice(voice)
#     text = voice.split()
#     good_text = list()
#     commands_dict = dict()
#     print(len(text))
#     if head[1] == 'on':
#         if len(text) == 0:
#             return
#         elif len(text) == 1 and text == 'джарвис':
#             yea_ser()
#             return
#         head[1] = 'off'
#         for elem in text:
#             for k, v in config.chunk.items():
#                 if elem in v:
#                     good_text.append(k)
#         if len(good_text) == 0:
#             print('я в on')
#             playsound(os.path.join('music_jar', 'mistake.wav'))
#             print("Command not found")
#             return
#         elif 'запустить' in good_text or 'закрыть' in good_text or 'выключить' in good_text:
#             good_text = ''.join(good_text)
#             print('1', good_text)
#             text = ' '.join(text)
#             print('2', text)
#             commands_dict[good_text] = text
#             argument(commands_dict)
#         else:
#             good_text = ' '.join(good_text)
#             commands_dict['good_text'] = good_text
#             func_y(commands_dict)
#
#     else:
#         for name_text in text:
#             for name in config.VA_ALIAS:
#                 if name_text == name:
#                     if len(text) == 1:
#                         yea_ser()
#                         return
#                     name_index = text.index(name_text)
#                     text.pop(name_index)
#                     for elem in text:
#                         for k, v in config.chunk.items():
#                             if elem in v:
#                                 good_text.append(k)
#                     if len(good_text) == 0:
#                         playsound(os.path.join('music_jar', 'mistake.wav'))
#                         print("Command not found")
#                         return
#                     elif 'запустить' in good_text or 'закрыть' in good_text or 'выключить' in good_text:
#                         good_text = ''.join(good_text)
#                         print('1', good_text)
#                         text = ' '.join(text)
#                         print('2', text)
#                         commands_dict[good_text] = text
#                         argument(commands_dict)
#                     else:
#                         good_text = ' '.join(good_text)
#                         commands_dict['good_text'] = good_text
#                         func_y(commands_dict)
#                 else:
#                     return


head = {'head': 'off'}


def header(voice: str):
    text = str(voice).split()

    for name in text:
        if name in config.VA_ALIAS:
            if len(text) == 1:
                playsound(os.path.join('music_jar', 'yes_ser.wav'))
                head['head'] = 'on'
                return
            elif len(text) > 1:
                # name_index = text.index(name)
                # text.pop(name_index)
                off_line(voice)
                return
    if head['head'] == 'on':
        if len(voice) == 0:
            return
        else:
            off_line(voice)


def off_line(voice: str):
    log_voice(voice)
    text = voice.split()
    good_text = list()
    commands_dict = dict()
    head['head'] = 'off'

    for elem in text:
        for k, v in config.chunk.items():
            if elem in v:
                good_text.append(k)
    if len(good_text) == 0:
        playsound(os.path.join('music_jar', 'mistake.wav'))
        print("Command not found")
        return
    for elem in good_text:
        if elem in config.words_arguments:
            good_text = ''.join(good_text)
            text = ' '.join(text)
            commands_dict[good_text] = text
            argument(commands_dict)
    else:
        good_text = ' '.join(good_text)
        commands_dict['good_text'] = good_text
        func_y(commands_dict)


def argument(text: dict):
    text = text
    commands_list = list()
    argument_list = show_list_programms.list_chunk()
    try:
        if 'запустить' in text:
            values = text.values()
            values = ' '.join(values)
            values = values.split()

            for elem in values:
                for k, v in argument_list.items():
                    if elem in v:
                        commands_list.append(k)
            commands_list = ' '.join(commands_list)
            text['запустить'] = commands_list
            # print('args', text)
            func_y(text)

        # elif 'выключить' in text:
        #         values = text.values()
        #         values = ' '.join(values)
        #         values = values.split()
        #
        #         for elem in values:
        #             for k, v in argument_list.items():
        #                 if elem in v:
        #                     commands_list.append(k)
        #         commands_list = ' '.join(commands_list)
        #         text['выключить'] = commands_list
        #         func_y(text)

        elif 'закрыть' in text:
            values = text.values()
            values = ' '.join(values)
            values = values.split()

            for elem in values:
                for k, v in argument_list.items():
                    if elem in v:
                        commands_list.append(k)
            commands_list = ' '.join(commands_list)
            text['закрыть'] = commands_list
            func_y(text)
    except AttributeError:
        AttributeError()


def func_y(text: dict):
    text = text
    keys_keys = text.keys()
    values_values = text.values()
    keys_keys = ' '.join(keys_keys)
    values_values = ' '.join(values_values)

    if keys_keys in config.words_arguments:
        for key in config.commands.keys():
            fuzzz = fuzz.token_sort_ratio(keys_keys, key)
            if fuzzz == 100:
                keys = key
                if keys in key:
                    config.commands[key](text.values())
                    break
                else:
                    playsound(os.path.join('music_jar', 'mistake.wav'))
                    print("Command not found")
                    return

    elif keys_keys == 'good_text':
        for key in config.commands.keys():
            fuzzz = fuzz.token_sort_ratio(values_values, key)
            if fuzzz == 100:
                values = key
                if values in key:
                    config.commands[key]()
                    break
                else:
                    playsound(os.path.join('music_jar', 'mistake.wav'))
                    print("Command not found")
                    return


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

    # for v in config.listen.values():
    #     if v == 'online':
    #         print('работает online')
    #         on_line()
        # elif v == 'offline':
        #     print('работает offline')
        #     stt.va_listen(off_line)


if __name__ == "__main__":
    main()
