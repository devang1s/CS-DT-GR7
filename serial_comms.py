'''
Code for serial communication with the microbit
'''

import serial.tools.list_ports
import time

def find_microbit_port():
    """
    Try to auto-detect the micro:bit serial port.
    Returns the port name if found, else None.
    """
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if "micro:bit" in port.description.lower() or "mbed" in port.description.lower():
            return port.device
    return None

try:
    port = find_microbit_port()
    if not port:
        raise Exception("Micro:bit not found. Check USB connection.")

    # Open serial connection
    ser = serial.Serial(port, baudrate=115200, timeout=1)
    time.sleep(2)  # Wait for micro:bit to reset

    print(f"Connected to micro:bit on {port}")
    print("Reading data... Press Ctrl+C to stop.")

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                x, y, z = map(int, line.split(','))
                print(f"X={x}, Y={y}, Z={z}")
            except ValueError:
                print(f"Invalid data: {line}")

except KeyboardInterrupt:
    print("\nStopped by user.")
except Exception as e:
    print(f"Error: {e}")
finally:
    try:
        ser.close()
    except:
        pass