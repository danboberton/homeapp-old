from datetime import datetime
import os


class Logger:

    def __init__(self):
        now = datetime.now().strftime("%Y-%m-%d-%H%M%S")
        self.logfile = None
        try:
            self.logfile = open("logs/" + now + ".log", "x")
        except:
            print("Exception building log file.")
            return
        pwd = os.getcwd()
        self.log("logfile " + pwd + "/" + self.logfile.name + " built.", printLog=True)


    def log(self, string, printLog=True):
        message = self.__logFormat(string)
        self.logfile.write(message)
        if printLog:
            print(self.__printFormat(string))

    def __printFormat(self, string):
        return str(f"*** {string} ***\n")

    def __logFormat(self, string):
        curtime = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
        return str(f"[{curtime}] {string}\n")
