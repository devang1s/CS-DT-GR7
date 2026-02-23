import serial
import serial.tools.list_ports
import time

def list_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"{port.device}: {port.description}")

def write_to_port(port, message):

    """
    Write a message to serial port.
    
    Args:
        port (str): COM port like 'COM5'.
        message (str): Text to send.
    
    Returns:
        None
    """

    ser = serial.Serial(port, 9600, timeout=1)
    ser.write(message.encode('utf-8'))

def read_from_port(port):
    """
    Read a message from a serial port
    
    Args:
        port (str): COM port like 'COM5'.
    
    Returns:
        str: Returns data from serial port
    """
    ser = serial.Serial(port, 9600, timeout=1)
    line = ser.readline()
    """try:
        return line.decode('utf-8').rstrip()
    except UnicodeDecodeError:
        return None """
    return line.decode('utf-8').rstrip()

while True:
    """     try:
        print(read_from_port('COM5'))
    except serial.  serialutil.SerialException:
        print('none')
        time.sleep(0.1) """
    time.sleep(1)
    print(read_from_port('COM5'))
    write_to_port('COM5', 'hi') 

""" list_ports() """