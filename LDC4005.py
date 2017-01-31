from IODevice import IODevice


class LDC4005:
    def __init__(self, path_to_usb_path):
        self.device = IODevice(path_to_usb_path)

    def on(self):
        self.device.write("OUTPut ON")

    def off(self):
        self.device.write("OUTPut OFF")

    def set_ld_current_in_amper(self, value):
        self.device.write("SOURce:CURRent:LEVel:AMPLitude %s" % value)

    def ld_current_reading(self):
        self.device.write("INITiate")
        self.device.write("MEASure:CURRent")
        self.device.write("FETCh:CURRent?")
        value = self.device.read(100)
        return float(value)

    def ld_voltage_reading(self):
        self.device.write("INITiate")
        self.device.write("MEASure:VOLTage")
        self.device.write("FETCh:VOLTage?")
        value = self.device.read(100)
        return float(value)
