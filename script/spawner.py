import pyautogui as p
import keyboard
import time as t

DEFAULT_PAUSE = 0.5
SAFETY_PAUSE = 0.3
ITERATIONS = 100
IMAGE_PATH = 'script/pictures/spawner/'
IMAGE_FORMAT = '.png'

def is_in_inventory():
    inventory_color = p.pixelMatchesColor(1475, 288, (198,198,198))
    return inventory_color

def safety():
    start_time = t.time()
    while t.time() - start_time < SAFETY_PAUSE and not is_in_inventory():
        ...

def end_program():
    print("Ending program...")
    p.moveTo(0,0)


def eat():
    try:
        p.press('e')
        p.moveTo(0, p.position().y)
        file = IMAGE_PATH + 'steak' + IMAGE_FORMAT
        x1, y1 = p.locateCenterOnScreen(file, confidence = 0.9)
        p.moveTo(x1, y1)
        p.press('2')
        p.press('e')
        p.press('2')
        p.mouseDown(button = 'right')
        while is_hungry():
            ...
        p.mouseUp(button = 'right')
        p.press('1')
    except p.ImageNotFoundException:
        end_program()         

def rejoin():
    try:
        file = IMAGE_PATH + 'lost_connection' + IMAGE_FORMAT
        p.locateOnScreen(file)
        p.press('tab')
        p.press('enter')
        p.press('enter')
    except p.ImageNotFoundException:
        ...

def is_hungry():
    return p.pixel(1111,897) == (40, 40, 40)

#Program start
keyboard.add_hotkey('shift', end_program)

p.FAILSAFE = True
p.PAUSE = DEFAULT_PAUSE

def main():
    p.alert('Ready?')
    p.rightClick()

    #Main loop
    try:
        while True:
            for i in range(ITERATIONS):
                print(f'\r{i}', end='')
                p.sleep(0.5)
                if p.pixel(961,572)[0] > 100:
                    p.click()
            if is_hungry():
                eat()
            rejoin()
    except Exception as e:
        #print(e.with_traceback())
        ...
    finally:
        keyboard.unhook_all()
        print('successfully ended.')

main()