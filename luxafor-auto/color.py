class Color:
    def __init__(self, rgbString):
        rgbArray = rgbString.split(",")
        self.red = int(rgbArray[0])
        self.green = int(rgbArray[1])
        self.blue = int(rgbArray[2])
