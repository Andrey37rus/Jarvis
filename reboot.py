import os
import sys
from gree import I_rebooted

path = os.path.abspath(os.path.join('main.py'))
os.startfile(path)
I_rebooted()
sys.exit()