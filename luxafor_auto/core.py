#stdLib
import os
import time

#3rd party
from configobj import ConfigObj

#local
from luxafor_auto.lux import Lux

def run():
    running = False

    dirname = os.path.dirname('/opt/lux-auto/')
    config_file = os.path.join(dirname, 'sys/config')
    config = ConfigObj(config_file)

    lux = Lux()
    lux.setLight(
        config["Idle"]["Color"], 
        config["Idle"]["Options"]
    )

    while True:
        device_status = os.popen('cat /proc/asound/card*/pcm0p/sub0/status').read()
        if device_status.find("RUNNING") != -1:
            if running == False:
                lux.setLight(
                    config["Running"]["Color"], 
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
                    config["Idle"]["Color"], 
                    config["Idle"]["Options"]
                )
                running = False
        time.sleep(.75)

def kill():
    dirname = os.path.dirname('/opt/lux-auto/')
    config_file = os.path.join(dirname, 'sys/config')
    config = ConfigObj(config_file)

    lux = Lux()
    lux.setLight(
        {"red": 0, "green": 0, "blue": 0},
        config["Idle"]["Options"]
    )
