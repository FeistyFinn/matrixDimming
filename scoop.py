import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.OUT)
servo_scoop=GPIO.PWM(12,50)

servo_scoop.start(0)
time.sleep(1)
servo_scoop.ChangeDutyCycle(5)
time.sleep(5)
servo_scoop.ChangeDutyCycle(2)
time.sleep(5)
servo_scoop.stop()
GPIO.cleanup()


