import pyautogui
import time

pyautogui.PAUSE = .05
pyautogui.click(1750, 950)


with pyautogui.hold('shift'):
    for _ in range(9):
        pyautogui.leftClick(625, 395)
        pyautogui.leftClick(1310, 371)