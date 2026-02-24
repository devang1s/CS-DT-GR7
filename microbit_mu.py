from microbit import pin0, sleep

pin0.set_analog_period(20)  # 20ms PWM period for servos

while True:
    pin0.write_analog(100)  # ~0° (1ms pulse)
    sleep(1000)
    pin0.write_analog(150)  # 90° (1.5ms)
    sleep(1000)
    pin0.write_analog(200)  # 180° (2ms)
    sleep(1000)
