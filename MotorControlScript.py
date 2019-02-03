import time
import RPi.GPIO as GPIO

PWMA=21
INA1=20
INA2=16
STBY=19
PWMB=13
INB1=6
INB2=5

def main():
    setup()
    stopAll()
    GPIO.output(STBY, GPIO.HIGH)

    time.sleep(5)
    forwardA()
    time.sleep(5)
    stopA()
    forwardB()
    time.sleep(5)
    stopB()
    stopAll()

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(STBY, GPIO.OUT)
    GPIO.setup(PWMA, GPIO.OUT)
    GPIO.setup(INA1, GPIO.OUT)
    GPIO.setup(INA2, GPIO.OUT)
    GPIO.setup(PWMB, GPIO.OUT)
    GPIO.setup(INB1, GPIO.OUT)
    GPIO.setup(INB2, GPIO.OUT)
    GPIO.setup(STBY, GPIO.OUT)

def stopA():
    GPIO.output(INA1, GPIO.LOW)
    GPIO.output(INA1, GPIO.LOW)

def stopB():
    GPIO.output(INB1, GPIO.LOW)
    GPIO.output(INB2, GPIO.LOW)

def stopAll():
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

if __name__ == "__main__":
    main()
