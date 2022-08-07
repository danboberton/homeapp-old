from zeep import Client

client = Client('http://localhost:8000/?wsdl')
result = client.service.say_hello("Dave", 5)
print(result)

class Client:
    def __init__(self, logger, config):

        try:
            self.client = Client(f"http://{config.serverIP}:{config.serverPort}/?wsdl")
        except:
            logger.log("Error connecting to client", printLog=True)