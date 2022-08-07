print(__package__)

from ..utils.utils import Logger
from ..utils.localconfig import Config
from ..api.client import Client

CONFIG_FILE_NAME = ".sensorconfig.yaml"

logger = Logger()
config = Config(logger, CONFIG_FILE_NAME)
api = Client()




