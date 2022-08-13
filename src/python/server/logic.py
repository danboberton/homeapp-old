class UserDefinedContext(object):
    def __init__(self, Logger, Config):
        self.logger = Logger
        self.config = Config

    # User def endpoint
    def logEvent(self, key, value):
        self.logger.log(f"{key} : {value}")