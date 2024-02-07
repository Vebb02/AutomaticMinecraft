import pyautogui as p
import keyboard

DEFAULT_PAUSE = 0.0005
ITERATIONS = 100
IMAGE_PATH = 'script/pictures/'
IMAGE_FORMAT = '.png'
POSITION_PATH = 'script/positions.txt'

#Functions
def isInInventory():
    x = p.pixelMatchesColor(inside_inventory[0], inside_inventory[1], (198,198,198))
    return x

def click(x, y):
    if isInInventory():
        p.moveTo(x, y)
        if isInInventory():
            p.click()

def end_program():
    print("Ending program...")
    p.moveTo(0,0)

def leave_inventory():
    if isInInventory():
        p.press('esc')

def craft():
    if isInInventory():
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
    click(x3, y3)

def throw_emerald_out():
    p.sleep(0.1)
    try:
        file = IMAGE_PATH + 'bed' + IMAGE_FORMAT
        p.locateCenterOnScreen(file)
    except p.ImageNotFoundException:
        try:
            p.press('e')
            p.sleep(0.1)
            p.move(-50, 0)
            file = IMAGE_PATH + 'emerald_inventory' + IMAGE_FORMAT
            x1, y1 = p.locateCenterOnScreen(file, confidence = 0.9)
            click(x1, y1)
            x2, y2 = throw_out
            click(x2, y2)
            p.press('e')
        except p.ImageNotFoundException:
            ...
            
def exit_menu():
    try:
        file = IMAGE_PATH + 'esc' + IMAGE_FORMAT
        p.locateOnScreen(file)
        p.press('esc')
    except p.ImageNotFoundException:
        ...


#Program start
keyboard.add_hotkey('shift', end_program)

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

p.alert('Ready?')
p.rightClick()

#Main loop
try:
    while True:
        for _ in range(ITERATIONS):
            #Enter crafting table, villager, etc...
            p.rightClick()
            p.sleep(0.1)
            craft()
            trade()
            leave_inventory()
        throw_emerald_out()
        exit_menu()
        leave_inventory()
except Exception as e:
    #print(e.with_traceback())
    ...
finally:
    keyboard.unhook_all()
    print('successfully ended.')