import os


class IODevice:
    def __init__(self, path_to_device):
        self.device = path_to_device
        self.file_descriptor = os.open(path_to_device, os.O_RDWR | os.O_NOCTTY)

    def write(self, command):
        os.write(self.file_descriptor, command.encode())

    def read(self, length=4000):
        return os.read(self.file_descriptor, length)

    def close(self):
        os.close(self.file_descriptor)

    def __del__(self):
        self.close()
