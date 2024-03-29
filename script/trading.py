import pyautogui as p
import keyboard
import time as t

DEFAULT_PAUSE = 0
SAFETY_PAUSE = 0.3
ITERATIONS = 100
IMAGE_PATH = 'script/pictures/trading/'
IMAGE_FORMAT = '.png'
POSITION_PATH = 'script/positions.txt'

emerald_counter = 0
esc_counter = 0

#Functions
def is_in_inventory():
    inventory_color = p.pixelMatchesColor(inside_inventory[0], inside_inventory[1], (198,198,198))
    return inventory_color

def click(x, y):
    if is_in_inventory():
        p.moveTo(x, y)
        if is_in_inventory():
            p.click()

def safety():
    start_time = t.time()
    while t.time() - start_time < SAFETY_PAUSE and not is_in_inventory():
        ...

def end_program():
    print("Ending program...")
    p.moveTo(0,0)

def leave_inventory():
    if is_in_inventory():
        p.press('esc')

def craft():
    if is_in_inventory():
        with p.hold('shift'):
            x1, y1 = recipe
            x2, y2 = finish_craft
            click(x1, y1)
            click(x2, y2)

def trade():
    x1, y1 = trade_to_emerald
    x2, y2 = execute_trade
    x3, y3 = throw_out
    click(x1, y1)
    click(x2, y2)
    click(x2, y2)
    click(x2, y2)
    click(x3, y3)

def throw_emerald_out():
    try:
        file = IMAGE_PATH + 'bed' + IMAGE_FORMAT
        p.locateCenterOnScreen(file)
        p.typewrite('zzz')
        p.press('enter')
    except p.ImageNotFoundException:
        try:
            p.press('e')
            safety()
            p.moveTo(0, p.position().y)
            p.sleep(0.1)
            file = IMAGE_PATH + 'emerald_inventory' + IMAGE_FORMAT
            x1, y1 = p.locateCenterOnScreen(file, confidence = 0.9)
            click(x1, y1)
            x2, y2 = throw_out
            click(x2, y2)
            p.press('e')
            global emerald_counter
            emerald_counter += 1
            print(f"Emeralds, {t.ctime()}: {emerald_counter}")
        except p.ImageNotFoundException:
            ...
            
def exit_menu():
    try:
        file = IMAGE_PATH + 'esc' + IMAGE_FORMAT
        p.locateOnScreen(file)
        p.press('esc')
        global esc_counter
        esc_counter += 1
        print(f"Esc, {t.ctime()}: {esc_counter}")
    except p.ImageNotFoundException:
        ...

def rejoin():
    try:
        file = IMAGE_PATH + 'lost_connection' + IMAGE_FORMAT
        p.locateOnScreen(file)
        p.press('tab')
        p.press('enter')
        p.press('enter')
    except p.ImageNotFoundException:
        ...

#Program start
# keyboard.add_hotkey('shift', end_program)
keyboard.add_hotkey('pause', end_program)

p.FAILSAFE = True
p.PAUSE = DEFAULT_PAUSE

try:
    with open(POSITION_PATH) as f:
        positions = f.read().split('\n')
        recipe = (int(positions[0].split(' ')[0]), int(positions[0].split(' ')[1]))
        finish_craft = (int(positions[1].split(' ')[0]), int(positions[1].split(' ')[1]))
        trade_to_emerald = (int(positions[2].split(' ')[0]), int(positions[2].split(' ')[1]))
        execute_trade = (int(positions[3].split(' ')[0]), int(positions[3].split(' ')[1]))
        throw_out = (int(positions[4].split(' ')[0]), int(positions[4].split(' ')[1]))
        inside_inventory = (int(positions[5].split(' ')[0]), int(positions[5].split(' ')[1]))

except FileNotFoundError:
    #Crafting
    p.alert('Paper in recipe book')
    recipe = p.position()
    p.alert('Paper in finish crafting')
    finish_craft = p.position()

    #Trading
    p.alert('Right side of trade to emerald')
    trade_to_emerald = p.position()
    p.alert('Execute trade')
    execute_trade = p.position()
    p.alert('Throw out')
    throw_out = p.position()

    #Inside inventory
    p.alert('Position that is the same light grey color in both crafting table and villager')
    inside_inventory = p.position()

    #Write to file
    positions = f'''{recipe[0]} {recipe[1]}
{finish_craft[0]} {finish_craft[1]}
{trade_to_emerald[0]} {trade_to_emerald[1]}
{execute_trade[0]} {execute_trade[1]}
{throw_out[0]} {throw_out[1]}
{inside_inventory[0]} {inside_inventory[1]}'''
    with open(POSITION_PATH, 'w') as f:
        positions = f.write(positions)

def main():
    p.alert('Ready?')
    p.rightClick()

    #Main loop
    try:
        while True:
            for _ in range(ITERATIONS):
                #Enter crafting table, villager, etc...
                if not is_in_inventory():
                    p.rightClick()
                    safety()
                    if is_in_inventory():
                        craft()
                        for _ in range(6):
                            trade()
                        leave_inventory()
            throw_emerald_out()
            exit_menu()
            leave_inventory()
            rejoin()
    except Exception as e:
        #print(e.with_traceback())
        ...
    finally:
        keyboard.unhook_all()
        print('successfully ended.')

main()   