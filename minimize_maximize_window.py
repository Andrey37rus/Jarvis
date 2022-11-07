import win32gui
import win32con
from win32gui import GetWindowText, GetForegroundWindow
from gree import yes_ser
from colorama import Fore, Back, Style

activ_win_icon = []


def show_minimize(*args):
    """Свернуть программу"""

    def windowEnumHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    top_windows = []

    activate = GetWindowText(GetForegroundWindow())

    win32gui.EnumWindows(windowEnumHandler, top_windows)
    for i in top_windows:
        if i[1] == activate:
            if i[1] == '':
                print(Fore.RED + 'danger')
                return
            else:
                win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)
                yes_ser()
                activ_win_icon.append(i[0])


def show_window(*args):
    """Развернуть программу"""

    if len(activ_win_icon) == 0:
        print(Fore.LIGHTYELLOW_EX + 'нет всписке свернутых программ')
        return
    for elem in activ_win_icon[::-1]:
        win32gui.ShowWindow(elem, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(elem)
        yes_ser()
        activ_win_icon.remove(elem)
        return
