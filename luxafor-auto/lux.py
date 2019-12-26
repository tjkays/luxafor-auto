from color import Color
from device import Device

class Lux:
    def __init__(self):
        self.device = Device(None)
        self.device.setupDevice()

    def setLight(self, color, options): 
        led = options["led"]
        action = options["action"]

        # Determine which action
        if action == 'color':
            self.setColor(led, color)
        elif action == 'fade':
            self.setFade(led, color, options["speed"])
        elif action == 'strobe':
            self.setStrobe(led, color, options["speed"], options["repeat"])
        elif action == 'wave':
            self.setWave(options["wave"], color, options["repeat"], options["speed"])
        elif action == 'pattern':
            self.setPattern(options["pattern"], options["repeat"])

    def setPattern(self, pattern, repeat):
        self.device.writeValue( [6,pattern,repeat,0,0,0,0] )

    def setWave(self, wave, color, repeat, speed):
        self.device.writeValue( [4,wave,color.red,color.green,color.blue,0,repeat,speed] )

    def setStrobe(self, led, color, speed, repeat):
        self.device.writeValue( [3,led,color.red,color.green,color.blue,speed,0,repeat] )

    def setFade(self, led, color, speed):
        self.device.writeValue( [2,led,color.red,color.green,color.blue,speed,0] )

    def setColor(self, led, color):
        self.device.writeValue( [1,led,color.red,color.green,color.blue,0,0] )
