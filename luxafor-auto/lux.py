from color import Color
from device import Device

class Lux:
    def __init__(self):
        self.device = Device(None)
        self.device.setupDevice()
        self.color = Color("0,0,0")

    def setLight(self, color, options): 
        led = int(options["led"])  
        action = options["action"]
        self.color = color

        # Determine which action
        if action == 'color':
            self.setColor(led)
        elif action == 'fade':
            speed = int(options["speed"])
            self.setFade(led, speed)
        elif action == 'strobe':
            speed = int(options["speed"])
            repeat = int(options["repeat"])
            self.setStrobe(led, speed, repeat)
        elif action == 'wave':
            speed = int(options["speed"])
            repeat = int(options["repeat"])
            wave = int(options["wave"])
            self.setWave(wave, repeat, speed)
        elif action == 'pattern':
            pattern = int(options["pattern"])
            repeat = int(options["repeat"])
            self.setPattern(pattern, repeat)

    def setPattern(self, pattern, repeat):
        self.device.writeValue([6,pattern,repeat,0,0,0,0])

    def setWave(self, wave, color, repeat, speed):
        color = self.color
        self.device.writeValue([4,wave,color.red,color.green,color.blue,0,repeat,speed])

    def setStrobe(self, led, speed, repeat):
        color = self.color
        self.device.writeValue([3,led,color.red,color.green,color.blue,speed,0,repeat])

    def setFade(self, led, speed):
        color = self.color
        self.device.writeValue([2,led,color.red,color.green,color.blue,speed,0])

    def setColor(self, led):
        color = self.color
        self.device.writeValue([1,led,color.red,color.green,color.blue,0,0])
