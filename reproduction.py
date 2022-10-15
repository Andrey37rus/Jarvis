import keyboard
import time


def play_music():
    btn = 'space'
    keyboard.send(btn)
    return


def up():
    nums = 0
    btn_up = 'up'
    keyboard.press("ctrl")
    for num in range(10):
        keyboard.send(btn_up)
        nums += 1
    print(nums)
    keyboard.release("ctrl")
    return


def down():
    nums = 0
    btn_down = 'down'
    keyboard.press("ctrl")
    for num in range(10):
        keyboard.send(btn_down)
        nums += 1
    print('-', nums)
    keyboard.release("ctrl")
    return


def next_trak():
    btn_down = 'down'
    btn_enter = 'enter'
    keyboard.send(btn_down)
    keyboard.send(btn_enter)
    return


def previous_track():
    btn_up = 'up'
    btn_enter = 'enter'
    keyboard.send(btn_up)
    keyboard.send(btn_enter)
    return



    # # name = ' '.join(args[0]).lower()
    # for key in wars_dict.keys():
    #     if name in key:
    #         for btn in wars_dict[key]:
    #             keyboard.send(btn)
    #             time.sleep(0.1)
    #
    #         break

