from pynput import mouse
import time
import pyautogui


def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    print('captura de pantalla')
    screenshot = pyautogui.screenshot()
    screenshot.save("{time}.png".format(time=time.time()))


# Collect events until released
with mouse.Listener(
        on_click=on_click, ) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_click=on_click,
    )
listener.start()
