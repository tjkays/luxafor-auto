#stdLib
import os
import time

#3rd party
from configobj import ConfigObj

#local
from luxafor_auto.lux import Lux
from luxafor_auto.color import Color

def run():
    running = False

    dirname = os.path.dirname('/opt/lux-auto/')
    config_file = os.path.join(dirname, 'sys/config')
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
