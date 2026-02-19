''''''
""" Code for serial communication with the microbit """
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
        pass'''

import serial
import serial.tools.list_ports
import sys
import time

def list_serial_ports():
    """
    List all available serial ports.
    Returns:
        list: A list of port names (e.g., ['COM3', '/dev/ttyUSB0']).
    """
    ports = serial.tools.list_ports.comports()
    return [port.device for port in ports]

def write_to_serial(port_name, baud_rate, message):
    """
    Write a message to the specified serial port.
    Args:
        port_name (str): Serial port name.
        baud_rate (int): Baud rate.
        message (str): Message to send.
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with serial.Serial(port=port_name, baudrate=baud_rate, timeout=1) as ser:
            if not ser.is_open:
                print(f"Failed to open port {port_name}")
                return False

            if isinstance(message, str):
                message = message.encode('utf-8')

            ser.write(message)
            ser.flush()
            print(f"Sent to {port_name}: {message}")
            return True

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return False

def read_from_serial(port_name, baud_rate, read_timeout=1):
    """
    Read a single line of data from the specified serial port.
    Args:
        port_name (str): Serial port name.
        baud_rate (int): Baud rate.
        read_timeout (int): Timeout in seconds for reading.
    Returns:
        str: The received message, or None if no data.
    """
    try:
        with serial.Serial(port=port_name, baudrate=baud_rate, timeout=read_timeout) as ser:
            if not ser.is_open:
                print(f"Failed to open port {port_name}")
                return None

            data = ser.readline().decode('utf-8', errors='ignore').strip()
            if data:
                print(f"Received from {port_name}: {data}")
                return data
            else:
                print("No data received.")
                return None

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

if __name__ == "__main__":
    # Step 1: List available ports
    ports = list_serial_ports()
    if not ports:
        print("No serial ports found.")
        sys.exit(1)

    print("Available ports:", ports)

    # Example usage
    selected_port = ports[0]  # Pick the first available port
    baud = 9600

    # Step 2: Write to the port
    write_to_serial(selected_port, baud, "Hello Device\n")

    # Step 3: Read from the port
    time.sleep(1)  # Give device time to respond
    read_from_serial(selected_port, baud)