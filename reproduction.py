import pyautogui


def up():
    # x = 7
    # a = (x//2)
    pyautogui.press('volumeup', 7)


def down():
    # x = 7
    # a = (x//2)
    pyautogui.press('volumedown', 7)


def soundless():
    pyautogui.press('volumedown', 55)


def sound():
    pyautogui.press('volumeup', 15)
