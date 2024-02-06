import pyautogui
import time
import keyboard

def isInInventory():
    return pyautogui.pixelMatchesColor(1456, 245, (198,198,198))

def click(x, y):
    pyautogui.moveTo(x, y)
    if isInInventory():
        pyautogui.click()

def end_program():
    print("Ending program...")
    #pyautogui.PAUSE = 2
    pyautogui.moveTo(0,0)

keyboard.add_hotkey('shift', end_program)

pyautogui.FAILSAFE = True
pyautogui.PAUSE = .025
pyautogui.moveTo(1750, 950)
try:
    while True:
        for _ in range(100):
            pyautogui.rightClick()
            if isInInventory():
                try:
                    with pyautogui.hold('shift'):
                        x1, y1 = pyautogui.locateCenterOnScreen('select_paper.png')
                        x2, y2 = pyautogui.locateCenterOnScreen('craft_paper.png')
                        while isInInventory():
                            click(x1,y1)
                            click(x2, y2)
                except:
                    ...
                try:
                    x, y = pyautogui.locateCenterOnScreen('paper_to_emerald.png')
                    click(x, y)
                    x, y = pyautogui.locateCenterOnScreen('emerald_villager.png')
                    click(x, y)
                    click(x, y)
                    x, y = pyautogui.locateCenterOnScreen('librarian.png')
                    click(x, y-50)
                except:
                    ...
                if isInInventory():
                    pyautogui.press('esc')
        try:
            pyautogui.press('e')
            t = time.time()
            x, y = pyautogui.locateCenterOnScreen('emerald_inventory.png')
            click(x, y)
            x, y = pyautogui.locateCenterOnScreen('crafting.png')
            click(x, y-50)
            pyautogui.press('e')
        except pyautogui.ImageNotFoundException:
            ...
        try:
            x = pyautogui.locateOnScreen('esc.png')
            pyautogui.press('esc')
        except pyautogui.ImageNotFoundException:
            ...
except Exception as e:
    ...
finally:
    keyboard.unhook_all()