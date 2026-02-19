# Write your code here :-)
from microbit import *
import utime

while True:
    # Example: send accelerometer data over serial
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    z = accelerometer.get_z()

    # Send comma-separated values
    print("{},{},{}".format(x, y, z))

    utime.sleep_ms(500)  # Send every 0.5 seconds
