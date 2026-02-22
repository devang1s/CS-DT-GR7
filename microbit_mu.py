from microbit import uart, display, sleep

uart.init(9600)  # Match your Python baudrate

while True:
    if uart.any():
        msg_encoded = uart.readline()
        if msg_encoded:
            text = msg_encoded.decode("utf-8").rstrip()
            display.scroll(text)  # Scrolls received text
    sleep(100)
