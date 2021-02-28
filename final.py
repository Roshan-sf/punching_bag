from gpiozero import LED, Button
import RPi.GPIO as GPIO
from playsound import playsound
import time
import random
buttonPressed = 0
led1 = LED(21)
led2 = LED(20)
led3 = LED(16)
led4 = LED(12)
led5 = LED(1)

def b1(channel):
    global buttonPressed
    buttonPressed=1
    print("1 pressed")
def b2(channel):
    global buttonPressed
    buttonPressed=2
    print("2 pressed")
def b3(channel):
    global buttonPressed
    buttonPressed=3
    print("3 pressed")
def b4(channel):
    global buttonPressed
    buttonPressed=4
    print("4 pressed")
def b5(channel):
    global buttonPressed
    buttonPressed=5
    print("5 pressed")
    
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set up for buttons
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(24,GPIO.RISING,callback=b1) # Setup event for button 1
GPIO.add_event_detect(23,GPIO.RISING,callback=b2) # Setup event for button 2
GPIO.add_event_detect(18,GPIO.RISING,callback=b3) # Setup event for button 3
GPIO.add_event_detect(15,GPIO.RISING,callback=b4) #etc
GPIO.add_event_detect(14,GPIO.RISING,callback=b5)

def getButtonPressed():
    global buttonPressed
    print("getting button")
    if buttonPressed == 0:
        while buttonPressed == 0:
            time.sleep(.01)
    time.sleep(.2)
    return buttonPressed

def getAnswer(length):
    global buttonPressed
    print("getting answer")
    answer = []
    for x in range(length):
        y = getButtonPressed()
        buttonPressed = 0
        answer.append(y)
    return answer

def getRandoms(length):
    randoms = []
    for x in range(length):
        y = random.randint(1,5)
        randoms.append(y)
    print(randoms)
    return randoms

def signify(theList):
    for x in theList:
        if x == 1:
            playsound('Head.mp3') #audio replacement here roshan
            time.sleep(.5)
        elif x == 2:
            playsound('Top_Right.mp3') #audio replacement here roshan
            time.sleep(.5)
        elif x == 3:
            playsound('Top_Left.mp3') #audio replacement here roshan
            time.sleep(.5)
        elif x == 4:
            playsound('Bottom_Right.mp3') #audio replacement here roshan
            time.sleep(.5)
        elif x == 5:
            playsound('Bottom_Left.mp3') #audio replacement here roshan
            time.sleep(.5)


game = True
num = 2
while game == True:
    correct = getRandoms(num)
    print(correct)
    signify(correct)
    response = getAnswer(num)
    print(response)
    if correct != response:
        game = False
        print("game over")
    num += 1