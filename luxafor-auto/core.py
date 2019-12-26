import os
import time
from color import Color
from lux import Lux

def run():
    running = False
    lux = Lux()

    color = Color(0, 255, 0)
    options = {
        "action": "color",
        "led": 255,
    }
    lux.setLight(color, options)

    while True:
        device_status = os.popen('cat /proc/asound/card*/pcm0p/sub0/status').read()
        if device_status.find("RUNNING") != -1:
            if running == False:
                color = Color(237, 190, 0)
                options = {
                    "action": "strobe",
                    "led": 255,
                    "speed": 120,
                    "repeat": 255,
                }
                lux.setLight(color, options)
                running = True
        else:
            if running == True:
                color = Color(0, 255, 0)
                options = {
                    "action": "color",
                    "led": 255,
                }
                lux.setLight(color, options)
                running = False
        time.sleep(.1)
