import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,100)

servo1.start(0)

servo1.mid()
time.sleep(3)
servo1.min()
time.sleep(3)
servo1.stop()
GPIO.cleanup()






