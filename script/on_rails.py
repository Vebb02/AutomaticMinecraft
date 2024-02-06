import pyautogui
import time
import keyboard

DEFAULT_PAUSE = 0.04

#Functions
def isInInventory():
    pyautogui.PAUSE = .0005
    x = pyautogui.pixelMatchesColor(1456, 245, (198,198,198))
    pyautogui.PAUSE = DEFAULT_PAUSE
    return x

def click(x, y):
    pyautogui.moveTo(x, y)
    if isInInventory():
        pyautogui.click()

def end_program():
    print("Ending program...")
    pyautogui.moveTo(0,0)

def leave_inventory():
    if isInInventory():
        pyautogui.press('esc')

def craft():
    if isInInventory():
        with pyautogui.hold('shift'):
            click(471,367)
            click(1450, 365)

def trade():
    click(754, 387)
    click(1310, 372)
    click(1310, 372)
    click(1700, 400)

def throw_emerald_out():
    try:
        pyautogui.locateCenterOnScreen('bed.png')
    except pyautogui.ImageNotFoundException:
        try:
            pyautogui.press('e')
            x, y = pyautogui.locateCenterOnScreen('emerald_inventory.png')
            click(x, y)
            click(1700, 400)
            pyautogui.press('e')
        except pyautogui.ImageNotFoundException:
            ...
            
def exit_menu():
    try:
        pyautogui.locateOnScreen('esc.png')
        pyautogui.press('esc')
    except pyautogui.ImageNotFoundException:
        ...


#Program start
keyboard.add_hotkey('shift', end_program)

pyautogui.FAILSAFE = True
pyautogui.PAUSE = DEFAULT_PAUSE
pyautogui.moveTo(1750, 950)

#Main loop
try:
    while True:
        for _ in range(100):
            #Enter crafting table, villager, etc...
            pyautogui.rightClick()
            craft()
            trade()
            leave_inventory()
        throw_emerald_out()
        exit_menu()
        leave_inventory()
except Exception as e:
    ...
finally:
    keyboard.unhook_all()
    print('successfully ended.')