import time
from colour import Color
from . import lux

def run():
    while true:
        device_status = os.system("cat /proc/asound/card*/pcm0p/sub0/status");
        if device_status.find("RUNNING") != -1:
            color = Color(rgb=(255,0,0))
            options = {
                "action": "strobe",
                "led": 255,
                "speed": 100,
                "repeat": 200
            }
            lux.setLight(color, options)
        else:
            color = Color(rgb=(0,255,0))
            options = {
                "action": "color",
                "led": 255,
                "color": color,
            }
            lux.setLight(color, options)
        time.sleep()
