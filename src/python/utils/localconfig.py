# load info from local config file
from yaml import load, dump, Loader, Dumper

class Config:
    def __init__(self, configFileName):
        try:
            self.configFile = open(configFileName, "r")
        except:
            print("Error opening config file")

        try:
            data = load(self.configFile,  Loader=Loader)
        except:
            print("Exception opening config file")

        # Load config Vars
        self.name = data["sensor-name"]
        self.serverIP = data["serverIP"]
        self.serverPort = data["serverPort"]
        print("Config Loaded: " + str(data))


