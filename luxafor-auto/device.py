import usb.core

class Device:
    def __init__(self, device):
        self.device = device

    def setupDevice(self):
        self.device = usb.core.find(idVendor=0x04d8, idProduct=0xf372)

        # Device found?
        if self.device is None:
            raise ValueError('Device not found')

        # Linux kernel sets up a device driver for USB device, which you have to detach.
        # Otherwise trying to interact with the device gives a 'Resource Busy' error.
        try:
          self.device.detach_kernel_driver(0)
        except Exception:
          pass
         
        self.device.set_configuration()

    def writeValue(values):
        self.device.write(1, values)
        self.device.write(1, values) # Run it again to ensure it works.

