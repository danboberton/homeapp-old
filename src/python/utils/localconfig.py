# load info from local config file
from yaml import load, dump, Loader, Dumper

CONFIG_FILE_NAME = ".config.yaml"

class Config:
    def __init__(self, logger):
        try:
            self.configFile = open(CONFIG_FILE_NAME, "r")
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


