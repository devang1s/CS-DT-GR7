from microbit import *
import radio
import music

# ---- Simple servo helpers for pins 1 and 2 ----
# angle ≈ 0–180 mapped to PWM value for ~0.5–2.5 ms pulse
def set_servo(pin, angle):
    # Clamp angle
    if angle < 0:
        angle = 0
    if angle > 180:
        angle = 180
    # MicroPython servo-ish mapping (tweak if needed)
    # 0deg ≈ 40, 90deg ≈ 77, 180deg ≈ 115 (these are approximate)
    value = int(40 + (angle / 180) * (115 - 40))
    pin.set_analog_period(20)      # 20 ms period for servo
    pin.write_analog(value)

def set_servo_p1(angle):
    set_servo(pin1, angle)

def set_servo_p2(angle):
    set_servo(pin2, angle)

# ---- Radio setup ----
radio.on()
radio.config(group=255, power=7)

# Center servos at 90 degrees
set_servo_p1(90)
set_servo_p2(90)

# Enable built-in speaker (Microbit V2 only)
music.set_tempo(ticks=4, bpm=180)  # Just to match speed a bit


def handle_received_string(received):
    if received == "wet":
        display.show("1")
        set_servo_p1(125)
        sleep(10000)
        set_servo_p1(90)
        sleep(5000)
        set_servo_p2(125)
        sleep(10000)
        set_servo_p2(90)
        sleep(5000)

    elif received == "dry":
        display.show("2")
        set_servo_p1(125)
        sleep(10000)
        set_servo_p1(90)
        sleep(5000)
        set_servo_p2(55)
        sleep(10000)
        set_servo_p2(90)
        sleep(5000)

    elif received == "recyclable":
        display.show("3")
        set_servo_p1(55)
        sleep(10000)
        set_servo_p1(90)
        sleep(5000)

    elif received == "dangerous":
        display.show("4")
        # Roughly mimic the C5-C5-C5-C5 pattern
        # (MicroPython can't use music.string_playable directly)
        for _ in range(4):
            music.pitch(523, 180)  # C5 ≈ 523 Hz
            sleep(180)


# ---- Main loop: poll radio for strings ----
while True:
    msg = radio.receive()
    if msg:
        handle_received_string(msg)
    sleep(100)
