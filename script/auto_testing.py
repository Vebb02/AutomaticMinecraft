import pyautogui
import time

t = time.time()
try:
    x, y = pyautogui.locateCenterOnScreen('paper_to_emerald.png')
    print(x, y)
except:
    ...
print(time.time() - t)
#print(time.time() - t)
