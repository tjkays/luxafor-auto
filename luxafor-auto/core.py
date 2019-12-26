import os
import time
from colour import Color
from lux import Lux

def run():
    while True:
        device_status = os.popen('cat /proc/asound/card*/pcm0p/sub0/status').read()
        lux = Lux()
        if device_status.find("RUNNING") != -1:
            color = Color(rgb=(1,0,0))
            options = {
                "action": "strobe",
                "led": 255,
                "speed": 100,
                "repeat": 200
            }
            lux.setLight(color, options)
        else:
            color = Color(rgb=(0,1,0))
            options = {
                "action": "color",
                "led": 255,
                "color": color,
            }
            lux.setLight(color, options)
        time.sleep()
