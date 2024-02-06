import pyautogui
import time

pyautogui.PAUSE = .05
pyautogui.click(1750, 950)


with pyautogui.hold('shift'):
    for _ in range(10):
        pyautogui.leftClick(513, 360)
        pyautogui.leftClick(1441, 368)