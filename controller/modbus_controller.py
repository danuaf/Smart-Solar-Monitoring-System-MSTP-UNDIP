from minimalmodbus import Instrument

class ModbusController:
    def __init__(self, com='COM3', slave_address=1):
        self.com = com
        self.slave_address = slave_address
        self.instrument = Instrument(self.com, self.slave_address)
        self.instrument.serial.baudrate = 9600

    def read_register(self, address, decimals=0):
        try:
            value = self.instrument.read_register(address, decimals)
            return value
        except Exception as e:
            print(f"Error reading register {address}: {e}")
            return None
