from microbit import uart, display, sleep

uart.init(9600)

def read_serial():
    if uart.any():
        msg_encoded = uart.readline()
        if msg_encoded:
            text = msg_encoded.decode("utf-8").rstrip()
            return text

def write_serial(message):
    uart.write(message.encode('utf-8'))

while True:
    write_serial('hi')
    """text = read_serial()
    if text is not None:
        display.scroll(text)"""
