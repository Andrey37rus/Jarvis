#  Jarvis 2.0
# auto-py-to-exe для компиляции online

import json
from datetime import datetime

import config
import stt
import os
from gree import i_need, mistake
from fuzzywuzzy import fuzz
import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.GREEN + f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")

head = {'head': 'off', 'foot': 'off', 'activ': 'on'}


def header(voice: str):
    voice = voice.split()
    name = config.VA_ALIAS
    try:
        for elem in voice:
            if elem in name:
                if len(voice) == 1:
                    i_need()
                    head['head'] = 'on'
                    return
                elif len(voice) > 1:
                    num = voice.index(elem)
                    voice.pop(num)
                    off_line(' '.join(voice))
                    return

        if head['head'] == 'on':
            if len(voice) == 0:
                del voice
                return
            else:
                off_line(' '.join(voice))
                return
    except:
        Exception()


def off_line(voice):
    # log_voice(voice)
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
    return


def func_y(text: dict):
    keys_keys = ' '.join(text.keys())
    values_values = ' '.join(text.values())
    func_b(keys_keys, values_values)


def func_b(keys_keys, values_values):

    for k, v in config.commands.items():
        fuzzz = fuzz.token_sort_ratio(keys_keys, k)
        if fuzzz == 100:
            keys = k
            if keys == k:
                head['foot'] = 'off'
                config.commands[keys](values_values)
                return
    if head['foot'] == 'on':
        head['foot'] = 'off'
        mistake()
        return
    slise(keys_keys, values_values)


def slise(keys_keys, values_values):
    head['foot'] = 'on'
    keys_keys = keys_keys.split()
    keys_keys = keys_keys[:1]
    keys_keys = ' '.join(keys_keys)
    func_b(keys_keys, values_values)


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
