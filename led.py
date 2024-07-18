import RPi.GPIO as GPIO
import time

def state(Gled, Rled, how_far):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Gled, GPIO.OUT, initial = GPIO.LOW) # 초록led 출력 초기출력-LOW
    GPIO.setup(Rled, GPIO.OUT, initial = GPIO.LOW) # 빨강led 출력 초기출력-LOW

    if how_far <= 10:
        GPIO.output(Gled, GPIO.HIGH)
        GPIO.output(Rled, GPIO.LOW)
        print("Gled : on, Rled : off")
    else:
        GPIO.output(Gled, GPIO.LOW)
        GPIO.output(Rled, GPIO.HIGH)
        print("Gled : off, Rled : on")
    