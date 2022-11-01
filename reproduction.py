import pyautogui as pg


def up(*args):
    """делает звук громче в x2"""
    pg.press(['volumeup'], 7)
    return


def down(*args):
    """делает звук тише в x2"""
    pg.press(['volumedown'], 7)
    return


def soundless(*args):
    """Делает комп без звука, со звуком"""

    pg.press(['volumemute'])
    return


def next_trak(*args):
    """Включает следующий трек на компе"""
    pg.press(['nexttrack'])
    return


def previous_track(*args):
    """Включает предыдущий трек на компе"""
    pg.press(['prevtrack'])
    return


def play(*args):
    """Play or Pause"""
    pg.press(['playpause'])
    return


