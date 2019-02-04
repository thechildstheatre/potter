import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 1
time.sleep(10)
kit.continuous_servo[0].throttle =  0.13
time.sleep(15)

kit.servo[2].angle = 0
time.sleep(10)

kit.continuous_servo[1].throttle = -1
time.sleep(0.6)
kit.continuous_servo[1].throttle =  0.13
time.sleep(15)
kit.continuous_servo[1].throttle =  1
time.sleep(0.615)
kit.continuous_servo[1].throttle =  0.13
time.sleep(1)
