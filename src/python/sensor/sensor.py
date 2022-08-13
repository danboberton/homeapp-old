print(__package__)

from ..utils.utils import Logger
from ..utils.localconfig import Config
from ..api.client import SensorClient

CONFIG_FILE_NAME = ".sensorconfig.yaml"

config = Config(CONFIG_FILE_NAME)
logger = Logger(config)

api = SensorClient(logger, config)

i = 0
while i < 20:
    result = api.logEvent("Key", i)
    i += 1
    print(result)




