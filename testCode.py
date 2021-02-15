from gpiozero import LED, Button
import time
import random

button = Button(14)
red = LED(21)
green = LED(20)
indicator = LED(16)
timeOn = 50
timeOnCurrent = 0
StillGoing = True
won = False
pressed = False

red.off()
green.off()
indicator.off()

while StillGoing == True:
    indicator.on()
    while timeOnCurrent < timeOn and pressed == False:
        if button.is_pressed:
            print("pressed")
            pressed = True
        else:
            time.sleep(.1)
            timeOnCurrent+=1
    indicator.off()
    print("indication done")
    
    if timeOnCurrent == timeOn and timeOn==0:
        won = True
        StillGoing = False
    elif timeOnCurrent == timeOn:
        red.on()
        time.sleep(5)
        StillGoing = False
    elif pressed == True:
        green.on()
        time.sleep(2)
        green.off()
        time.sleep(1)
        pressed = False

    timeOn = timeOn-1
    timeOnCurrent = 0
    
    wait = random.randint(5,70)
    print(wait)
    wait = wait*.1
if won == True:
    green.blink()