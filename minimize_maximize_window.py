import win32gui
import win32con
from win32gui import GetWindowText, GetForegroundWindow
from gree import yes_ser
activ_win_icon = []

# def show_minimize(*args):
#     """Свернуть программу"""
#     activate = GetWindowText(GetForegroundWindow())
#
#     def windowEnumHandler(hwnd, top_windows):
#         top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#     def bringToFront(window_name):
#         top_windows = []
#
#         win32gui.EnumWindows(windowEnumHandler, top_windows)
#
#         for i in top_windows:
#             if i[1] == window_name:
#                 win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)
#
#     bringToFront(activate)


# def activate_win(hwnd, activ_win_icon):
#
#     activ_win_icon.append((hwnd, win32gui.GetWindowText(hwnd)))

# def activate_windows():
#     activ_win_icon.append((hwnd, win32gui.GetWindowText(hwnd)))


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
                print('danger')
                return
            else:
                win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)
                yes_ser()
                activ_win_icon.append(i[0])


def show_window(*args):
    """Развернуть программу"""

    if len(activ_win_icon) == 0:
        print('нет всписке свернутых программ')
        return

    print(activ_win_icon)
    for elem in activ_win_icon[::-1]:
        win32gui.ShowWindow(elem, win32con.SHOW_FULLSCREEN)
        win32gui.SetForegroundWindow(elem)
        yes_ser()
        activ_win_icon.remove(elem)
        return


    # for i in top_windows:
    #     if i[1] == activate:
    #         if i[1] == '':
    #             print('danger')
    #             return
    #         else:
    #             win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
    #             win32gui.SetForegroundWindow(i[0])



# def show_window(text: str):
#     """Развернуть программу"""
#
#     def windowEnumHandler(hwnd, top_windows):
#         top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#     def bringToFront(window_name):
#         top_windows = []
#
#         win32gui.EnumWindows(windowEnumHandler, top_windows)
#         for num, elem in enumerate(top_windows):
#             print('elem:', num + 1, ':', elem)
#         for i in top_windows:
#             if window_name.lower() in i[1].lower() and 'gdi+' not in i[1].lower():
#                 win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
#                 win32gui.SetForegroundWindow(i[0])
#                 break
#     print(text)
#     text = text.split()
#     text = text[1:]
#     print(text)
#     name = ' '.join(text).lower()
#     with open('name_path_program.json', 'r') as file:
#         name_path_program = json.load(file)
#     for key in name_path_program.keys():
#         if name in key:
#             path = name_path_program[key]
#             b = path[::-1]
#             slash = b.index('\\')
#             new_name = b[:slash]
#             new_name = new_name[::-1]
#             bringToFront(new_name)
#             break
#
#
# def show_minimize(*args):
#     """Свернуть программу"""
#
#     def windowEnumHandler(hwnd, top_windows):
#         top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
#
#     def bringToFront(window_name):
#         top_windows = []
#         win32gui.EnumWindows(windowEnumHandler, top_windows)
#         for i in top_windows:
#             if window_name.lower() in i[1].lower() and 'gdi+' not in i[1].lower():
#                 win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)
#                 break
#
#     name = ' '.join(args[0]).lower()
#     name_path_program = shelve.open("name_path_program")
#     for key in name_path_program.keys():
#         if name in key:
#             path = name_path_program[key]
#             b = path[::-1]
#             slash = b.index('\\')
#             new_name = b[:slash]
#             new_name = new_name[::-1]
#             bringToFront(new_name)
#             break
