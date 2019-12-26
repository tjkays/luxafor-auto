from colour import Color
from device import Device

class Lux:
    def __init__(self):
        self.device = Device(None)

    def setLight(self, color, options):
        self.device.setupDevice()

        led = options["led"]
        action = options["action"]

        # Determine which action
        if action == 'color':
            setColor(led, color)
        elif action == 'fade':
            setFade(led, color, options["speed"])
        elif action == 'strobe':
            setStrobe(led, color, options["speed"])
        elif action == 'wave':
            setWave(options["wave"], color, options["repeat"], options["speed"])
        elif action == 'pattern':
            setPattern(options["pattern"], options["repeat"])

    def setPattern(self, pattern, repeat):
        self.device.writeValue( [6,pattern,repeat,0,0,0,0] )

    def setWave(self, wave, color, repeat, speed):
        self.device.writeValue( [4,wave,color.red,color.green,color.blue,0,repeat,speed] )

    def setStrobe(self, led, color, speed, repeat):
        self.device.writeValue( [3,led,color.green,color.blue,speed,0,repeat] )

    def setFade(self, led, color, speed):
        self.device.writeValue( [2,led,color.green,color.blue,speed,0] )

    def setColor(self, led, color):
        self.device.writeValue( [1,led,color.green,color.blue,0,0] )
