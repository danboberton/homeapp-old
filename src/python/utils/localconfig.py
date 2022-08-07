# load info from local config file
from yaml import load, dump, Loader, Dumper

class Config:
    def __init__(self, logger, configFileName):
        try:
            self.configFile = open(configFileName, "r")
        except:
            logger.log("Error opening config file")

        try:
            data = load(self.configFile,  Loader=Loader)
        except:
            logger.log("Exception opening config file")

        # Load config Vars
        self.name = data["sensor-name"]
        self.serverIP = data["serverIP"]
        self.serverPort = data["serverPort"]
        logger.log("Config Loaded: " + str(data))
        print(data)


