print(__package__)

from ..utils.utils import Logger
from ..utils.localconfig import Config
from ..api.client import Client

logger = Logger()
config = Config(logger)
api = Client()




