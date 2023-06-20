import keyboard
import mouse 
import time

print("press alt + T to turn on")
isClicking = False

def set_clicer():
    global isClicking
    if isClicking:
        isClicking =False
        print("off")
    else:
        isClicking = True
        print("on")

keyboard.add_hotkey('alt + t',set_clicer)

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)
