import serial
import serial.tools.list_ports

def list_ports():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"{port.device}: {port.description}")

def write_to_port(port, message):
    ser = serial.Serial(port, 9600, timeout=1)
    ser.write(message.encode('utf-8'))

write_to_port('COM5',"hi")