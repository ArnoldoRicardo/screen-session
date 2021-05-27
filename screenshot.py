import pyautogui
import time
import os
import subprocess

import os.path

script_dir = os.path.dirname(os.path.abspath(__file__))
#im = Image.open)

CHROME = os.path.join('C:\\', 'Program Files', 'Google', 'Chrome', 'Application', 'chrome.exe')
#os.system('taskkill /im chrome.exe')
subprocess.call([CHROME])
# subprocess.call([CHROME, '--kiosk'])
# subprocess.call(['code'])

while(True):
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{time.time()}.png")
    time.sleep(6)
