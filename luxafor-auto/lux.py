from colour import Color
from device import Device

def setLight(color, options):
    device = Device(None)
    device.setupDevice()

    led = options["led"]
    action = options["action"]

    # Determine which action
    if action == 'color':
        setColor(led, color, device)
    elif action == 'fade':
        setFade(led, color, options["speed"], device)
    elif action == 'strobe':
        setStrobe(led, color, options["speed"], device)
    elif action == 'wave':
        setWave(options["wave"], color, options["repeat"], options["speed"], device)
    elif action == 'pattern':
        setPattern(options["pattern"], options["repeat"], device)

def setPattern(pattern, repeat, device):
    writeValue( [6,pattern,repeat,0,0,0,0] )

def setWave(wave, color, repeat, speed, device):
    writeValue( [4,wave,color.red,color.green,color.blue,0,repeat,speed] )

def setStrobe(led, color, speed, repeat, device):
    writeValue( [3,led,color.green,color.blue,speed,0,repeat] )

def setFade(led, color, speed, device):
    writeValue( [2,led,color.green,color.blue,speed,0] )

def setColor(led, color, device):
    writeValue( [1,led,color.green,color.blue,0,0] )

if __name__ == '__main__':
    main()
