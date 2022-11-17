# -*- coding: utf-8 -*-
import os
import sys
from gree import I_rebooted
import subprocess

# здесь закрываем файл main
path = os.path.join("jarvis.exe")
subprocess.call("taskkill /f /im {app}".format(app=path, encoding="utf-8"))


# здесь открываем файл main и закрываем файл reboot_down
I_rebooted()
subprocess.Popen(path)
