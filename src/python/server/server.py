print(__package__)

from ..utils.utils import Logger
from ..utils.localconfig import Config
from ..api.server import LoggingService
from time import sleep

CONFIG_FILE_NAME = ".serverconfig.yaml"

config = Config(CONFIG_FILE_NAME)
logger = Logger(config)
api = LoggingService(logger, config)
api.runServer()
