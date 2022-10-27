import pyautogui
import pyautogui as pg


def up(*args):
    """делает звук громче в x2"""

    pg.press(['volumeup'], 7)


def down(*args):
    """делает звук тише в x2"""

    pg.press(['volumedown'], 7)


def soundless(*args):
    """Делает комп без звука, со звуком"""

    pg.press(['volumemute'])
    return


def next_trak(*args):
    """Включает следующий трек на компе"""

    pg.press(['nexttrack'])


def previous_track(*args):
    """Включает предыдущий трек на компе"""
    pg.press(['prevtrack'])
    pass


def play(*args):
    """Play or Pause"""
    pg.press(['playpause'])
    pass

def stop(*args):
    pass

