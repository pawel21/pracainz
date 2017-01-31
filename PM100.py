from IODevice import IODevice

class PM100:
    def __init__(self, path_to_usb_path):
        self.device = IODevice(path_to_usb_path)

    def set_wavelength_in_nm(self, value):
        self.device.write("CORRection:WAVelength " + str(value))

    def get_power(self):
        self.device.write("INITiate")
        self.device.write("MEASure:POWer")
        self.device.write("FETCh?")
        value = self.device.read(100)
        return float(value)
