import time
import RPi.GPIO as GPIO
from evdev import InputDevice, categorize, ecodes

PWMA=21
INA1=20
INA2=16
STBY=19
PWMB=13
INB1=6
INB2=5

A=304
B=305
R1=311
R2=313
L1=310
L2=312
START=315
SELECT=314

gameOver = False

gamepad = InputDevice('/dev/input/event0')

def main():
    setup()
    stopAll()
    gameLoop()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(STBY, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)
    GPIO.setup(INA1, GPIO.OUT)
    GPIO.setup(INA2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)
    GPIO.setup(INB1, GPIO.OUT)
    GPIO.setup(INB2, GPIO.OUT)
    GPIO.output(STBY, GPIO.HIGH)
    print(gamepad)

def gameLoop():
    while not gameOver:
        for event in gamepad.read_loop():
            if event.type == ecodes.EV_KEY:
                if event.value == 1:
                    if event.code == A:
                        forwardAll()
                        time.sleep(0.05)
                    elif event.code == B:
                        reverseAll()
                        time.sleep(0.05)
                    elif event.code == R1 or event.code == R2:
                        turnRight()
                        time.sleep(0.05)
                    elif event.code == L1 or event.code == L2:
                        turnLeft()
                        time.sleep(0.05)
                elif event.value == 0:
                    stopAll()
                time.sleep(0.10)


def stopA():
    GPIO.output(INA1, GPIO.LOW)
    GPIO.output(INA2, GPIO.LOW)

def stopB():
    GPIO.output(INB1, GPIO.LOW)
    GPIO.output(INB2, GPIO.LOW)

def stopAll():
    print("Pause")
    stopA();
    stopB();

def forwardA():
    GPIO.output(INA1, GPIO.HIGH)
    GPIO.output(INA2, GPIO.LOW)
    GPIO.output(PWMA, GPIO.HIGH)

def reverseA():
    GPIO.output(INA1, GPIO.LOW)
    GPIO.output(INA2, GPIO.HIGH)
    GPIO.output(PWMA, GPIO.HIGH)

def forwardB():
    GPIO.output(INB1, GPIO.HIGH)
    GPIO.output(INB2, GPIO.LOW)
    GPIO.output(PWMB, GPIO.HIGH)

def reverseB():
    GPIO.output(INB1, GPIO.LOW)
    GPIO.output(INB2, GPIO.HIGH)
    GPIO.output(PWMB, GPIO.HIGH)

def forwardAll():
    print("Moving Forward")
    forwardA()
    forwardB()

def reverseAll():
    print("Reversing Car")
    reverseA()
    reverseB()

def turnRight():
    print("Going Right")
    reverseA()
    forwardB()

def turnLeft():
    print("Going Left")
    reverseB()
    forwardA()

if __name__ == "__main__":
    main()
