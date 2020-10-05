import RPi.GPIO as IO
import time



pwmPin = 19
dirPin = 13



IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(pwmPin, IO.OUT)
IO.setup(dirPin,IO.OUT)



p = IO.PWM(pwmPin, 100)
p.start(0)


try:
    while 1:
        '''
        IO.output(dirPin, True)
        for x in range (100):
            p.ChangeDutyCycle(x)
            time.sleep(0.1)
        time.sleep(0.5)
        for x in range (100, 0, -1):
            p.ChangeDutyCycle(x)
            time.sleep(0.1)
        time.sleep(0.5)
        IO.output(dirPin, False)   
        for x in range (100):
            p.ChangeDutyCycle(x)
            time.sleep(0.1)
        time.sleep(0.5)
        for x in range (100, 0, -1):
            p.ChangeDutyCycle(x)
            time.sleep(0.1)
        '''
        p.ChangeDutyCycle(20)
        time.sleep(2)
        p.ChangeDutyCycle(40)
        time.sleep(2)
        p.ChangeDutyCycle(60)
        time.sleep(2)
        p.ChangeDutyCycle(80)
        time.sleep(2)
        p.ChangeDutyCycle(100)
        time.sleep(2)
except KeyboardInterrupt:
     IO.output(dirPin, False) 
     IO.output(pwmPin, False)
     IO.cleanup() 
