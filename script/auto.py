import pyautogui
import time

pyautogui.alert("Choose first location")
first = pyautogui.position()
pyautogui.alert("Choose second location")
second = pyautogui.position()

pyautogui.PAUSE = .1
pyautogui.click()


with pyautogui.hold('shift'):
    for _ in range(9):
        pyautogui.leftClick(first.x, first.y)
        pyautogui.leftClick(second.x, second.y)