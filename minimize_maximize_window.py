import shelve
import win32gui
import win32con


def show_window(*args):
    """Развернуть программу"""

    def windowEnumHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    def bringToFront(window_name):
        top_windows = []
        win32gui.EnumWindows(windowEnumHandler, top_windows)
        for i in top_windows:
            if window_name.lower() in i[1].lower() and 'gdi+' not in i[1].lower():
                win32gui.ShowWindow(i[0], win32con.SW_SHOWNORMAL)
                win32gui.SetForegroundWindow(i[0])
                break

    name = ' '.join(args[0]).lower()
    name_path_program = shelve.open("name_path_program")
    for key in name_path_program.keys():
        if name in key:
            path = name_path_program[key]
            b = path[::-1]
            slash = b.index('\\')
            new_name = b[:slash]
            new_name = new_name[::-1]
            bringToFront(new_name)
            break


def show_minimize(*args):
    """Свернуть программу"""

    def windowEnumHandler(hwnd, top_windows):
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    def bringToFront(window_name):
        top_windows = []
        win32gui.EnumWindows(windowEnumHandler, top_windows)
        for i in top_windows:
            if window_name.lower() in i[1].lower() and 'gdi+' not in i[1].lower():
                win32gui.ShowWindow(i[0], win32con.SW_MINIMIZE)
                break

    name = ' '.join(args[0]).lower()
    name_path_program = shelve.open("name_path_program")
    for key in name_path_program.keys():
        if name in key:
            path = name_path_program[key]
            b = path[::-1]
            slash = b.index('\\')
            new_name = b[:slash]
            new_name = new_name[::-1]
            bringToFront(new_name)
            break
