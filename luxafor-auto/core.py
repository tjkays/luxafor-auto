import os
import time
from color import Color
from lux import Lux

def run():
    running = True
    lux = Lux()
    while True:
        device_status = os.popen('cat /proc/asound/card*/pcm0p/sub0/status').read()
        if device_status.find("RUNNING") != -1:
            if running == False:
                color = Color(255, 0, 0)
                options = {
                    "action": "strobe",
                    "led": 255,
                    "speed": 100,
                    "repeat": 200
                }
                lux.setLight(color, options)
                running = True
        else:
            if running == True:
                color = Color(0, 255, 0)
                options = {
                    "action": "color",
                    "led": 255,
                    "color": color,
                }
                lux.setLight(color, options)
                running = False
        time.sleep(.1)
