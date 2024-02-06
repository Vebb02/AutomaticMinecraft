import pyautogui
import time

def isInInventory():
    return pyautogui.pixelMatchesColor(1456, 245, (198,198,198))

def click(x, y):
    if isInInventory():
        pyautogui.moveTo(x, y)
        pyautogui.click()

pyautogui.FAILSAFE = True
pyautogui.PAUSE = .025
pyautogui.click(1750, 950)

while True:
    pyautogui.rightClick( )
    time.sleep(1)
    with pyautogui.hold('shift'):
        click(471,367)
        click(1450, 365)
    
    click(754, 387)
    click(1310, 372)
    while not pyautogui.pixelMatchesColor(913, 109, (21, 21, 21), 1) and isInInventory():
        ...
    click(1700, 400)

    if pyautogui.pixelMatchesColor(1326, 476, (198,198,198)):    
        pyautogui.press('esc')

    time.sleep(2)