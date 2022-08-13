from datetime import datetime
import os


class Logger:

    def __init__(self, Config):
        now = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        self.logfile = None
        self.config = Config
        try:
            self.logfile = open("logs/" + now + ".log", "x")
        except:
            print("Exception building log file.")
            return
        pwd = os.getcwd()
        self.log(f"logfile {pwd}/{self.logfile.name} built.", printLog=True)

    def log(self, string, printLog=False):
        message = self.__logFormat(string)
        self.logfile.write(message)
        self.logfile.flush()
        if printLog:
            print(self.__printFormat(string))

    @staticmethod
    def __printFormat(string):
        return str(f"*** {string} ***")


    def __logFormat(self, string):
        curtime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        return str(f"[{curtime}][{self.config.name}]{string}\n")
