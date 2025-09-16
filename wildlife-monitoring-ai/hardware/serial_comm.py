import serial

class ActionDevice:
    def __init__(self, port='COM4', baudrate=9600):
        self.ser = serial.Serial(port, baudrate, timeout=1)

    def trigger_buzzer(self):
        self.ser.write(b'BUZZER_ON')

    def trigger_light(self):
        self.ser.write(b'LIGHT_ON')