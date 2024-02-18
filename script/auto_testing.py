import pyautogui as p

p.FAILSAFE = True


print(p.pixel(1111,897))
p.alert()
print(p.position())

#p.rightClick()
"""
while True:
    p.sleep(1)
    if p.pixel(961,572)[0] > 100:
        p.click()
"""