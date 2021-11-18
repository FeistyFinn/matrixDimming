import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

servo1=GPIO.PWM(11,50)
servo2=GPIO.PWM(13,50)
servo3=GPIO.PWM(12,50)

servo1.start(0)
servo2.start(0)
servo3.start(0)
print("Hello")
time.sleep(2)

print("Hello1")

servo3.ChangeDutyCycle(3)
duty=2
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    servo2.ChangeDutyCycle(duty)
    print(duty)
    time.sleep(1)
    duty = duty + 1
time.sleep(2)
print("Hello2")
servo1.ChangeDutyCycle(7)
servo2.ChangeDutyCycle(5)
time.sleep(1)
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(4)
servo1.stop()
servo2.stop()
servo3.stop()
GPIO.cleanup()
print("Bye!")


