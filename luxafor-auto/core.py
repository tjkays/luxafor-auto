import os
import time
from configobj import ConfigObj
from color import Color
from lux import Lux

def run():
    running = False

    dirname = os.path.dirname(__file__)
    config_file = os.path.join(dirname, '../sys/config')
    config = ConfigObj(config_file)

    lux = Lux()
    lux.setLight(
        Color(config["Idle"]["Color"]), 
        config["Idle"]["Options"]
    )

    while True:
        device_status = os.popen('cat /proc/asound/card*/pcm0p/sub0/status').read()
        if device_status.find("RUNNING") != -1:
            if running == False:
                lux.setLight(
                    Color(config["Running"]["Color"]), 
                    config["Running"]["Options"]
                )
                running = True
        else:
            if running == True:
                options = {
                    "action": "color",
                    "led": 255,
                }
                lux.setLight(
                    Color(config["Idle"]["Color"]), 
                    config["Idle"]["Options"]
                )
                running = False
        time.sleep(.1)
