import pyautogui
import time
import subprocess


subprocess.call(['code'])

while(True):
    screenshot = pyautogui.screenshot()
    screenshot.save(f"./log/log{time.asctime()}.png")
    time.sleep(6)
