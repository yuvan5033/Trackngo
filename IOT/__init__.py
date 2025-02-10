import serial
import time

class GPSModule:
    def __init__(self, port="/dev/ttyS0", baud_rate=9600):
        self.serial_port = serial.Serial(port, baud_rate, timeout=1)
        if not self.serial_port.is_open:
            self.serial_port.open()
        print("GPS module initialized")

    def read_raw_data(self):
        if self.serial_port.in_waiting:
            line = self.serial_port.readline().decode('utf-8', errors='ignore').strip()
            return line
        return None

    def close(self):
        self.serial_port.close()
