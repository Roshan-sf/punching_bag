from gpiozero import LED, Button
import time
import random

button0 = Button(14)
button1 = Button(15)
LED0 = LED(12)
LED1 = LED(16)
red = LED(21)
green = LED(20)
answer = [2,2]
guess = [2,2]
ongoing = True
def fillslot():
    value = 2
    while value == 2:
        print(value)
        if button0.is_pressed:
            LED0.on()
            value = 0
            button0.wait_for_release()
            LED0.off()
        elif button1.is_pressed:
            LED1.on()
            value = 1
            button1.wait_for_release()
            LED1.off()
    return value
    
while ongoing == True:
    green.on()
    time.sleep(2)
    green.off()
    print("green off")
    for y in range(len(answer)):
        x = answer[y]
        x = random.randint(0,1)
        answer[y] = x
        if x == 0:
            LED0.on()
            time.sleep(1)
            LED0.off()
        elif x == 1:
            LED1.on()
            time.sleep(1)
            LED1.off()
    print(answer)
    for x in guess:
        x = fillslot()
    if answer != guess:
        ongoing == False
    
    
red.on()
sleep(2)
#ending code
LED0.off()
LED1.off()
red.off()
green.off()