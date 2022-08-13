from zeep import Client

# client = Client('http://localhost:8000/?wsdl')
# result = client.service.say_hello("Dave", 5)
# print(result)

class SensorClient:
    def __init__(self, logger, config):

        try:
            conString = str(f"http://{config.serverIP}:{config.serverPort}/?wsdl")
            self.client = Client('http://localhost:8000/?wsdl')
        except:
            logger.log("Error connecting to client", printLog=True)

    def logEvent(self, key, value):
        result = self.client.service.logEvent(key, value)
        return result